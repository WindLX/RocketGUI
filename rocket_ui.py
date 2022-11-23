import collections
import random
import re
import pandas as pd
from datetime import datetime

import PyQt5.QtCore
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QUrl, pyqtSignal, QTimer
from PyQt5.QtWebEngineWidgets import *
import requests
from PyQt5.QtWidgets import QAction, QDialog, QAbstractItemView, QTableWidgetItem, QCheckBox, QGridLayout, QVBoxLayout, \
    QFrame, QWidget, QLabel

import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkIOGeometry import vtkSTLReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer, vtkCamera
)

from monitor import GetRawMsgThread
from data import data_slice, msg_slice
from RocketMonitor import Ui_MainWindow
from MapUpdateFreq import Ui_Form

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

matplotlib.use('Qt5Agg')


class RocketUi(PyQt5.QtCore.QObject, Ui_MainWindow):
    msg_add_signal = pyqtSignal(str)
    map_update_signal = pyqtSignal(list)
    plot_data_signal = pyqtSignal()
    model_rotation_signal = pyqtSignal(list)

    def __init__(self):
        super(RocketUi, self).__init__()
        self.map_update_counter = 0
        self.map_update_frequency = 1
        self.set_map = SetMapUi()
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.plot_data = []
        self.data_frame = collections.deque(maxlen=50)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)
        _translate = QtCore.QCoreApplication.translate

        self.state.setGeometry(QtCore.QRect(790, 70, 80, 15))

        MainWindow.setWindowTitle(_translate("MainWindow", "Rocket"))
        MainWindow.setWindowIcon(QtGui.QIcon("Rocket.ico"))

        self.delay.setText(_translate("MainWindow", "0 ms"))
        self.state.setText(_translate("MainWindow", "Disconnect"))

        self.temperature.setText(_translate("MainWindow", "0°"))
        self.pressure.setText(_translate("MainWindow", "0 Pa"))
        self.altitude.setText(_translate("MainWindow", "0 m"))

        self.time.setText(_translate("MainWindow", "0-0-0 0:0:0"))
        self.lat.setText(_translate("MainWindow", "0°0'0\" N"))
        self.lon.setText(_translate("MainWindow", "0°0'0\" E"))

        self.acc_z.setText(_translate("MainWindow", "0 m/s^2"))
        self.acc_y.setText(_translate("MainWindow", "0 m/s^2"))
        self.acc_x.setText(_translate("MainWindow", "0 m/s^2"))

        self.angspe_z.setText(_translate("MainWindow", "0 °/s"))
        self.angspe_y.setText(_translate("MainWindow", "0 °/s"))
        self.angspe_x.setText(_translate("MainWindow", "0 °/s"))

        self.roll_ang.setText(_translate("MainWindow", "0 °"))
        self.pitch_ang.setText(_translate("MainWindow", "0 °"))
        self.yaw_ang.setText(_translate("MainWindow", "0 °"))

        # page
        self.tabWidget.setCurrentIndex(0)

        # status bar
        self.statusbar.showMessage("Disconnect")

        # menu bar
        file_menu = self.menubar.addMenu("File")
        setting_menu = self.menubar.addMenu("Setting")
        memory_menu = self.menubar.addMenu("Memory")

        import_action = QAction('Import...', self)
        import_action.triggered.connect(self.import_action)
        file_menu.addAction(import_action)

        file_menu.addSeparator()

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(MainWindow.close)
        file_menu.addAction(exit_action)

        map_freq_action = QAction('Map Update Frequency', self)
        map_freq_action.triggered.connect(self.map_freq_action)
        setting_menu.addAction(map_freq_action)

        clear_memory_action = QAction('Clear', self)
        clear_memory_action.triggered.connect(self.clear_memory_action)
        memory_menu.addAction(clear_memory_action)

        # connect
        self.connect_thread = GetRawMsgThread()
        self.connect_thread.data_add_signal.connect(self.update_data_slot)

        # data update
        self.msg_add_signal.connect(self.update_msg_slot)

        # map
        self.map = QWebEngineView(self.groupBox_2)
        self.map.setGeometry(QtCore.QRect(70, 90, 811, 351))
        self.map.setObjectName("map")
        self.map_update_signal.connect(self.update_map_slot)

        # plot
        self.plot = QGridLayout(self.plot_box)
        self.plot.setObjectName("plot")
        self.plot.addWidget(self.canvas, 0, 1)

        # model
        self.tab_2 = QWidget()
        self.tabWidget_2.addTab(self.tab_2, "Posture")
        self.vl = QVBoxLayout()

        self.vtkWidget = QVTKRenderWindowInteractor(self.tab_2)
        self.vl.addWidget(self.vtkWidget)

        self.ren = vtkRenderer()
        self.ren.SetBackground(1.0, 1.0, 1.0)
        self.ren.SetBackground2(0.1, 0.2, 0.4)
        self.ren.SetGradientBackground(1)
        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

        # Create source
        source = vtkSTLReader()
        source.SetFileName("rocket.STL")

        # Create a mapper
        mapper = vtkPolyDataMapper()
        mapper.SetInputConnection(source.GetOutputPort())

        # Create an actor
        self.actor = vtkActor()
        self.actor.SetMapper(mapper)
        self.actor.SetOrigin(0, 0, 230)

        # camera
        camera = vtkCamera()
        camera.SetPosition(-850, 0, 480)
        camera.SetFocalPoint(0, 0, 480)
        self.ren.SetActiveCamera(camera)

        self.ren.AddActor(self.actor)
        self.tab_2.setLayout(self.vl)
        self.iren.Initialize()

        # button
        self.connect.clicked.connect(self.connect_cloud_slot)
        self.clear.clicked.connect(self.textBrowser.clear)
        self.data_clear.clicked.connect(self.clear_data_slot)
        self.data_save.clicked.connect(self.save_data_slot)
        self.plot_select.clicked.connect(self.select_plot_data_slot)
        self.plot_save.clicked.connect(self.save_plot_slot)
        self.plot_clear.clicked.connect(self.clear_plot_slot)
        self.plot_data_signal.connect(self.draw_plot_slot)
        self.model_rotation_signal.connect(self.model_rotation_slot)

        # time
        self.local_time.setText(_translate("MainWindow", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        self.init_timer()

        # data table
        self.data.setColumnCount(15)
        self.data.setHorizontalHeaderLabels(
            ["UTC", "Temperature", "Pressure", "Altitude", "Lat", "Lon", "RollAngle", "PitchAngle", "YawAngle", "AccX",
             "AccY", "AccZ", "AnguSpeX", "AnguSpeY", "AnguSpeZ"])
        self.data.verticalHeader().setDisabled(True)
        self.data.horizontalHeader().setDisabled(True)
        self.data.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def init_timer(self):
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.update_time)

    def update_time(self):
        self.local_time.setText(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def connect_cloud_slot(self):
        self.connect.setEnabled(False)
        self.statusbar.showMessage("Try connect...")
        self.connect_thread.start()

    def update_data_slot(self, raw_data):
        if not raw_data or data_slice(raw_data)["cmd"] == "-1":
            self.statusbar.showMessage("Connect Failed!")
            self.state.setText("Disconnect")
            self.connect.setEnabled(True)
        else:
            self.statusbar.showMessage("Connecting")
            self.state.setText("Connecting")
            self.textBrowser.append(raw_data)
            try:
                msg = data_slice(raw_data)['msg']
            except KeyError:
                pass
            else:
                self.msg_add_signal.emit(msg)
            finally:
                pass

    def update_msg_slot(self, raw_msg):
        msg_dict = msg_slice(raw_msg)
        if msg_dict == {}:
            msg_dict = {
                "UTC": self.data_frame[-1][0],
                "Temperature": self.data_frame[-1][1],
                "Pressure": self.data_frame[-1][2],
                "Altitude": self.data_frame[-1][3],
                "Lat": self.data_frame[-1][4],
                "Lon": self.data_frame[-1][5],
                "RollAngle": self.data_frame[-1][6],
                "PitchAngle": self.data_frame[-1][7],
                "YawAngle": self.data_frame[-1][8],
                "AccX": self.data_frame[-1][9],
                "AccY": self.data_frame[-1][10],
                "AccZ": self.data_frame[-1][11],
                "AnguSpeX": self.data_frame[-1][12],
                "AnguSpeY": self.data_frame[-1][13],
                "AnguSpeZ": self.data_frame[-1][14]
            }
        # TODO utc_time = f"{msg_dict['UTC'][0:2]}:{msg_dict['UTC'][2:4]}:{msg_dict['UTC'][4:6]}"
        utc_time = msg_dict['UTC']
        raw_lat = msg_dict['Lat']
        raw_lon = msg_dict['Lon']
        lat = round(float(raw_lat[1:raw_lat.find('.') - 2]) + float(raw_lat[raw_lat.find('.') - 2:]) / 60, 5)
        lon = round(float(raw_lon[1:raw_lon.find('.') - 2]) + float(raw_lon[raw_lon.find('.') - 2:]) / 60, 5)
        lat_dfm = f"{raw_lat[1:raw_lat.find('.') - 2]}°{raw_lat[raw_lat.find('.') - 2:raw_lat.find('.')]}'{str(int(float('0' + raw_lat[raw_lat.find('.'):]) * 60))}\""
        s = '0' + raw_lon[raw_lon.find('.'):]
        pattern = re.compile(r'\s+')
        s = re.sub(pattern, '', s)
        lon_dfm = f"{raw_lon[1:raw_lon.find('.') - 2]}°{raw_lon[raw_lon.find('.') - 2:raw_lon.find('.')]}'{str(int(float(s) * 60))}\""

        _translate = QtCore.QCoreApplication.translate

        self.delay.setText(_translate("MainWindow", "0 ms"))

        if self.tabWidget.currentIndex() == 1:
            self.temperature.setText(_translate("MainWindow", f"{msg_dict['Temperature']}°C"))
            self.pressure.setText(_translate("MainWindow", f"{msg_dict['Pressure']} Pa"))
            self.altitude.setText(_translate("MainWindow", f"{msg_dict['Altitude']} m"))

            self.time.setText(_translate("MainWindow", f"{utc_time}"))
            self.lat.setText(_translate("MainWindow", f"{lat_dfm}\" {raw_lat[0]}"))
            self.lon.setText(_translate("MainWindow", f"{lon_dfm}\" {raw_lon[0]}"))

            self.acc_z.setText(_translate("MainWindow", f"{msg_dict['AccZ']} m/s^2"))
            self.acc_y.setText(_translate("MainWindow", f"{msg_dict['AccY']} m/s^2"))
            self.acc_x.setText(_translate("MainWindow", f"{msg_dict['AccX']} m/s^2"))

            self.angspe_z.setText(_translate("MainWindow", f"{msg_dict['AnguSpeZ']}°/s"))
            self.angspe_y.setText(_translate("MainWindow", f"{msg_dict['AnguSpeY']}°/s"))
            self.angspe_x.setText(_translate("MainWindow", f"{msg_dict['AnguSpeX']}°/s"))

            self.roll_ang.setText(_translate("MainWindow", f"{msg_dict['RollAngle']}°"))
            self.pitch_ang.setText(_translate("MainWindow", f"{msg_dict['PitchAngle']}°"))
            self.yaw_ang.setText(_translate("MainWindow", f"{msg_dict['YawAngle']}°"))

        self.map_update_counter += 1
        if self.map_update_counter >= self.map_update_frequency:
            if self.tabWidget.currentIndex() == 1 and self.tabWidget_2.currentIndex() == 0:
                self.map_update_signal.emit([lat, lon])
            self.map_update_counter = 0

        self.data.setRowCount(self.data.rowCount() + 1)
        data_list = [utc_time, msg_dict["Temperature"], msg_dict["Pressure"], msg_dict["Altitude"], str(lat), str(lon),
                     msg_dict["RollAngle"], msg_dict["PitchAngle"], msg_dict["YawAngle"], msg_dict["AccX"],
                     msg_dict["AccY"], msg_dict["AccZ"], msg_dict["AnguSpeX"], msg_dict["AnguSpeY"],
                     msg_dict["AnguSpeZ"]]
        for i in range(15):
            self.data.setItem(self.data.rowCount() - 1, i, QTableWidgetItem(data_list[i]))
        self.data_frame.append(data_list)
        if self.tabWidget.currentIndex() == 3:
            self.plot_data_signal.emit()
        if self.tabWidget.currentIndex() == 1 and self.tabWidget_2.currentIndex() == 1:
            self.model_rotation_signal.emit([msg_dict["RollAngle"], msg_dict["PitchAngle"], msg_dict["YawAngle"]])

    def update_map_slot(self, location):
        key = "04b77c62516855fdc4db68485faf2541"
        zoom = str(self.zoom_slider.value())
        params = {
            'location': f"{location[1]},{location[0]}",
            'zoom': zoom,
            'size': "811*351",
            'key': key,
            'markers': f"mid,0xFF0000,A:{location[1]},{location[0]}"
        }
        url = "https://restapi.amap.com/v3/staticmap?"
        j = requests.get(url=url, params=params).url
        self.map.load(QUrl(j))

    def import_action(self):
        pass

    def clear_data_slot(self):
        self.data.clear()
        self.data.setColumnCount(15)
        self.data.setRowCount(0)
        self.data.setHorizontalHeaderLabels(
            ["UTC", "Temperature", "Pressure", "Altitude", "Lat", "Lon", "RollAngle", "PitchAngle", "YawAngle", "AccX",
             "AccY", "AccZ", "AnguSpeX", "AnguSpeY", "AnguSpeZ"])
        self.data.verticalHeader().setDisabled(True)
        self.data.horizontalHeader().setDisabled(True)
        self.data.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def save_data_slot(self):
        column_headers = []
        for j in range(self.data.columnCount()):
            column_headers.append(self.data.horizontalHeaderItem(j).text())
        df = pd.DataFrame(columns=column_headers)

        for row in range(self.data.rowCount()):
            for col in range(self.data.columnCount()):
                item = self.data.item(row, col)
                df.at[row, column_headers[col]] = item.text() if item is not None else ""
        df.to_csv('rocket.csv', index=False)

    def map_freq_action(self):
        map_freq_setting = QDialog()
        self.set_map.setupUi(map_freq_setting)
        self.set_map.map_freq_signal.connect(self.set_freq)
        map_freq_setting.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        map_freq_setting.show()
        map_freq_setting.exec_()

    def set_freq(self, freq):
        self.map_update_frequency = freq
        self.freq.setText(str(self.map_update_frequency))

    def clear_memory_action(self):
        self.data_frame.clear()

    def select_plot_data_slot(self):
        page_index = self.data_select.currentIndex()
        if page_index == 0:
            self.plot_data = [self.BMP180_combo.currentText()]
        elif page_index == 1 or 2 or 3:
            l = self.data_select.currentWidget().findChildren(QCheckBox)
            self.plot_data = [str(self.data_select.tabText(self.data_select.currentIndex())) + " " + l[i].text() for i
                              in range(3) if l[i].isChecked()]

    def draw_plot_slot(self):
        para = {"Temperature": 1,
                "Pressure": 2,
                "Altitude": 3,
                "Posture Roll": 6,
                "Posture Pitch": 7,
                "Posture Yaw": 8,
                "Acc X-axis": 9,
                "Acc Y-axis": 10,
                "Acc Z-axis": 11,
                "Angu Speed X-axis": 12,
                "Angu Speed Y-axis": 13,
                "Angu Speed Z-axis": 14
                }
        para_2 = {"Temperature": "°C",
                  "Pressure": "Pa",
                  "Altitude": "m",
                  "Posture Roll": "°",
                  "Posture Pitch": "°",
                  "Posture Yaw": "°",
                  "Acc X-axis": "m/s^2",
                  "Acc Y-axis": "m/s^2",
                  "Acc Z-axis": "m/s^2",
                  "Angu Speed X-axis": "°/s",
                  "Angu Speed Y-axis": "°/s",
                  "Angu Speed Z-axis": "°/s"
                  }
        self.figure.clf()
        ax = self.figure.subplots()
        ax.clear()
        ax.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%0.3f'))
        ax.yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(15))
        ax.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%d'))
        ax.xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(8))
        ax.set_xlim(int(self.data_frame[0][0][-4:]), int(self.data_frame[-1][0][-4:]))
        x = [int(self.data_frame[i][0][-4:]) for i in range(len(self.data_frame))]
        # x = [i for i in range(len(self.data_frame))]
        if self.plot_data:
            y = [[self.data_frame[j][para[self.plot_data[i]]] for j in range(len(self.data_frame))] for i in
                 range(len(self.plot_data))]
            for i in range(len(y)):
                yy = list(map(float, y[i]))
                ax.plot(x, yy, label=self.plot_data[i])
            ax.set_xlabel("UTC time")
            s = " "
            ax.set_ylabel(para_2[self.plot_data[0]])
            ax.set_title(s.join(self.plot_data) + " Plot")
            ax.legend()
        self.canvas.draw()

    def save_plot_slot(self):
        s = " "
        if self.plot_data and self.data_frame:
            self.figure.savefig(s.join(self.plot_data) + " Plot" + ".png")

    def clear_plot_slot(self):
        self.clear_memory_action()

    def model_rotation_slot(self, angle):
        self.actor.SetOrientation(float(angle[0]), float(angle[1]), float(angle[2]))
        # self.actor.SetOrientation(random.uniform(-5.0, 5.0), random.uniform(-5.0, 5.0), random.uniform(-5.0, 5.0))
        self.ren.AddActor(self.actor)
        self.iren.Initialize()


class SetMapUi(PyQt5.QtCore.QObject, Ui_Form):
    map_freq_signal = pyqtSignal(int)

    def setupUi(self, Form):
        super().setupUi(Form)

    def retranslateUi(self, Form):
        super().retranslateUi(Form)
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Setting"))
        Form.setWindowIcon(QtGui.QIcon("Rocket.ico"))
        self.pushButton.clicked.connect(self.set)

    def set(self):
        freq = self.spinBox.value()
        self.map_freq_signal.emit(freq)
