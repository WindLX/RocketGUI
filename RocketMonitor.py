# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RocketMonitor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 720)
        MainWindow.setMinimumSize(QtCore.QSize(960, 720))
        MainWindow.setMaximumSize(QtCore.QSize(960, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 940, 680))
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.connect_widget = QtWidgets.QWidget()
        self.connect_widget.setObjectName("connect_widget")
        self.connect = QtWidgets.QPushButton(self.connect_widget)
        self.connect.setGeometry(QtCore.QRect(50, 30, 93, 28))
        self.connect.setObjectName("connect")
        self.clear = QtWidgets.QPushButton(self.connect_widget)
        self.clear.setEnabled(True)
        self.clear.setGeometry(QtCore.QRect(420, 610, 93, 28))
        self.clear.setCheckable(False)
        self.clear.setAutoDefault(False)
        self.clear.setObjectName("clear")
        self.label_4 = QtWidgets.QLabel(self.connect_widget)
        self.label_4.setGeometry(QtCore.QRect(60, 70, 200, 15))
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.connect_widget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 90, 831, 511))
        self.textBrowser.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(self.connect_widget)
        self.label_5.setGeometry(QtCore.QRect(720, 40, 72, 15))
        self.label_5.setObjectName("label_5")
        self.delay = QtWidgets.QLabel(self.connect_widget)
        self.delay.setGeometry(QtCore.QRect(790, 40, 72, 15))
        self.delay.setObjectName("delay")
        self.label_12 = QtWidgets.QLabel(self.connect_widget)
        self.label_12.setGeometry(QtCore.QRect(720, 70, 72, 15))
        self.label_12.setObjectName("label_12")
        self.state = QtWidgets.QLabel(self.connect_widget)
        self.state.setGeometry(QtCore.QRect(790, 70, 72, 15))
        self.state.setObjectName("state")
        self.local_time = QtWidgets.QLabel(self.connect_widget)
        self.local_time.setGeometry(QtCore.QRect(570, 70, 130, 16))
        self.local_time.setObjectName("local_time")
        self.label_16 = QtWidgets.QLabel(self.connect_widget)
        self.label_16.setGeometry(QtCore.QRect(480, 70, 71, 16))
        self.label_16.setObjectName("label_16")
        self.tabWidget.addTab(self.connect_widget, "")
        self.rocket_widget = QtWidgets.QWidget()
        self.rocket_widget.setObjectName("rocket_widget")
        self.groupBox = QtWidgets.QGroupBox(self.rocket_widget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 211, 151))
        self.groupBox.setObjectName("groupBox")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 110, 81, 15))
        self.label_8.setObjectName("label_8")
        self.temperature = QtWidgets.QLabel(self.groupBox)
        self.temperature.setGeometry(QtCore.QRect(110, 30, 81, 16))
        self.temperature.setObjectName("temperature")
        self.pressure = QtWidgets.QLabel(self.groupBox)
        self.pressure.setGeometry(QtCore.QRect(110, 70, 81, 16))
        self.pressure.setObjectName("pressure")
        self.altitude = QtWidgets.QLabel(self.groupBox)
        self.altitude.setGeometry(QtCore.QRect(110, 110, 81, 16))
        self.altitude.setObjectName("altitude")
        self.groupBox_3 = QtWidgets.QGroupBox(self.rocket_widget)
        self.groupBox_3.setGeometry(QtCore.QRect(250, 20, 211, 151))
        self.groupBox_3.setObjectName("groupBox_3")
        self.acc_z = QtWidgets.QLabel(self.groupBox_3)
        self.acc_z.setGeometry(QtCore.QRect(80, 110, 111, 16))
        self.acc_z.setObjectName("acc_z")
        self.acc_y = QtWidgets.QLabel(self.groupBox_3)
        self.acc_y.setGeometry(QtCore.QRect(80, 70, 111, 16))
        self.acc_y.setObjectName("acc_y")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(20, 70, 51, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(20, 30, 51, 16))
        self.label_14.setObjectName("label_14")
        self.acc_x = QtWidgets.QLabel(self.groupBox_3)
        self.acc_x.setGeometry(QtCore.QRect(80, 30, 111, 16))
        self.acc_x.setObjectName("acc_x")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(20, 110, 51, 16))
        self.label_15.setObjectName("label_15")
        self.groupBox_4 = QtWidgets.QGroupBox(self.rocket_widget)
        self.groupBox_4.setGeometry(QtCore.QRect(490, 20, 201, 151))
        self.groupBox_4.setObjectName("groupBox_4")
        self.angspe_z = QtWidgets.QLabel(self.groupBox_4)
        self.angspe_z.setGeometry(QtCore.QRect(80, 110, 111, 16))
        self.angspe_z.setObjectName("angspe_z")
        self.angspe_y = QtWidgets.QLabel(self.groupBox_4)
        self.angspe_y.setGeometry(QtCore.QRect(80, 70, 111, 16))
        self.angspe_y.setObjectName("angspe_y")
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setGeometry(QtCore.QRect(20, 70, 51, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_4)
        self.label_20.setGeometry(QtCore.QRect(20, 30, 51, 16))
        self.label_20.setObjectName("label_20")
        self.angspe_x = QtWidgets.QLabel(self.groupBox_4)
        self.angspe_x.setGeometry(QtCore.QRect(80, 30, 111, 16))
        self.angspe_x.setObjectName("angspe_x")
        self.label_21 = QtWidgets.QLabel(self.groupBox_4)
        self.label_21.setGeometry(QtCore.QRect(20, 110, 51, 16))
        self.label_21.setObjectName("label_21")
        self.groupBox_5 = QtWidgets.QGroupBox(self.rocket_widget)
        self.groupBox_5.setGeometry(QtCore.QRect(710, 20, 221, 151))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_24 = QtWidgets.QLabel(self.groupBox_5)
        self.label_24.setGeometry(QtCore.QRect(40, 110, 31, 16))
        self.label_24.setObjectName("label_24")
        self.label_22 = QtWidgets.QLabel(self.groupBox_5)
        self.label_22.setGeometry(QtCore.QRect(40, 70, 41, 16))
        self.label_22.setObjectName("label_22")
        self.roll_ang = QtWidgets.QLabel(self.groupBox_5)
        self.roll_ang.setGeometry(QtCore.QRect(100, 30, 91, 16))
        self.roll_ang.setObjectName("roll_ang")
        self.label_23 = QtWidgets.QLabel(self.groupBox_5)
        self.label_23.setGeometry(QtCore.QRect(40, 30, 41, 16))
        self.label_23.setObjectName("label_23")
        self.pitch_ang = QtWidgets.QLabel(self.groupBox_5)
        self.pitch_ang.setGeometry(QtCore.QRect(100, 70, 91, 16))
        self.pitch_ang.setObjectName("pitch_ang")
        self.yaw_ang = QtWidgets.QLabel(self.groupBox_5)
        self.yaw_ang.setGeometry(QtCore.QRect(100, 110, 91, 16))
        self.yaw_ang.setObjectName("yaw_ang")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.rocket_widget)
        self.tabWidget_2.setGeometry(QtCore.QRect(20, 170, 901, 481))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 881, 451))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(30, 30, 72, 15))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(30, 60, 72, 15))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(310, 60, 72, 15))
        self.label_11.setObjectName("label_11")
        self.time = QtWidgets.QLabel(self.groupBox_2)
        self.time.setGeometry(QtCore.QRect(100, 30, 191, 16))
        self.time.setObjectName("time")
        self.lat = QtWidgets.QLabel(self.groupBox_2)
        self.lat.setGeometry(QtCore.QRect(100, 60, 191, 16))
        self.lat.setObjectName("lat")
        self.lon = QtWidgets.QLabel(self.groupBox_2)
        self.lon.setGeometry(QtCore.QRect(380, 60, 181, 16))
        self.lon.setObjectName("lon")
        self.zoom_slider = QtWidgets.QSlider(self.groupBox_2)
        self.zoom_slider.setGeometry(QtCore.QRect(10, 160, 22, 160))
        self.zoom_slider.setMinimum(3)
        self.zoom_slider.setMaximum(17)
        self.zoom_slider.setPageStep(1)
        self.zoom_slider.setOrientation(QtCore.Qt.Vertical)
        self.zoom_slider.setObjectName("zoom_slider")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(310, 30, 72, 15))
        self.label_17.setObjectName("label_17")
        self.freq = QtWidgets.QLabel(self.groupBox_2)
        self.freq.setGeometry(QtCore.QRect(380, 30, 181, 16))
        self.freq.setObjectName("freq")
        self.tabWidget_2.addTab(self.tab, "")
        self.tabWidget.addTab(self.rocket_widget, "")
        self.data_widget = QtWidgets.QWidget()
        self.data_widget.setObjectName("data_widget")
        self.data = QtWidgets.QTableWidget(self.data_widget)
        self.data.setGeometry(QtCore.QRect(20, 20, 891, 581))
        self.data.setObjectName("data")
        self.data.setColumnCount(0)
        self.data.setRowCount(0)
        self.data_save = QtWidgets.QPushButton(self.data_widget)
        self.data_save.setGeometry(QtCore.QRect(270, 610, 93, 28))
        self.data_save.setObjectName("data_save")
        self.data_clear = QtWidgets.QPushButton(self.data_widget)
        self.data_clear.setGeometry(QtCore.QRect(550, 610, 93, 28))
        self.data_clear.setObjectName("data_clear")
        self.tabWidget.addTab(self.data_widget, "")
        self.plot_widget = QtWidgets.QWidget()
        self.plot_widget.setObjectName("plot_widget")
        self.plot_save = QtWidgets.QPushButton(self.plot_widget)
        self.plot_save.setGeometry(QtCore.QRect(360, 620, 93, 28))
        self.plot_save.setObjectName("plot_save")
        self.plot_clear = QtWidgets.QPushButton(self.plot_widget)
        self.plot_clear.setGeometry(QtCore.QRect(640, 620, 93, 28))
        self.plot_clear.setObjectName("plot_clear")
        self.groupBox_6 = QtWidgets.QGroupBox(self.plot_widget)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 10, 181, 631))
        self.groupBox_6.setObjectName("groupBox_6")
        self.data_select = QtWidgets.QTabWidget(self.groupBox_6)
        self.data_select.setGeometry(QtCore.QRect(10, 20, 161, 561))
        self.data_select.setTabPosition(QtWidgets.QTabWidget.West)
        self.data_select.setObjectName("data_select")
        self.BMP180 = QtWidgets.QWidget()
        self.BMP180.setObjectName("BMP180")
        self.BMP180_combo = QtWidgets.QComboBox(self.BMP180)
        self.BMP180_combo.setGeometry(QtCore.QRect(10, 10, 121, 21))
        self.BMP180_combo.setObjectName("BMP180_combo")
        self.BMP180_combo.addItem("")
        self.BMP180_combo.addItem("")
        self.BMP180_combo.addItem("")
        self.data_select.addTab(self.BMP180, "")
        self.acc = QtWidgets.QWidget()
        self.acc.setObjectName("acc")
        self.acc_x_check = QtWidgets.QCheckBox(self.acc)
        self.acc_x_check.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.acc_x_check.setChecked(False)
        self.acc_x_check.setTristate(False)
        self.acc_x_check.setObjectName("acc_x_check")
        self.acc_y_check = QtWidgets.QCheckBox(self.acc)
        self.acc_y_check.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.acc_y_check.setObjectName("acc_y_check")
        self.acc_z_check = QtWidgets.QCheckBox(self.acc)
        self.acc_z_check.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.acc_z_check.setObjectName("acc_z_check")
        self.data_select.addTab(self.acc, "")
        self.angle_speed = QtWidgets.QWidget()
        self.angle_speed.setObjectName("angle_speed")
        self.angspe_x_check = QtWidgets.QCheckBox(self.angle_speed)
        self.angspe_x_check.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.angspe_x_check.setObjectName("angspe_x_check")
        self.angspe_y_check = QtWidgets.QCheckBox(self.angle_speed)
        self.angspe_y_check.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.angspe_y_check.setObjectName("angspe_y_check")
        self.angspe_z_check = QtWidgets.QCheckBox(self.angle_speed)
        self.angspe_z_check.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.angspe_z_check.setObjectName("angspe_z_check")
        self.data_select.addTab(self.angle_speed, "")
        self.posture = QtWidgets.QWidget()
        self.posture.setObjectName("posture")
        self.roll_check = QtWidgets.QCheckBox(self.posture)
        self.roll_check.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.roll_check.setObjectName("roll_check")
        self.pitch_check = QtWidgets.QCheckBox(self.posture)
        self.pitch_check.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.pitch_check.setObjectName("pitch_check")
        self.yaw_check = QtWidgets.QCheckBox(self.posture)
        self.yaw_check.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.yaw_check.setObjectName("yaw_check")
        self.data_select.addTab(self.posture, "")
        self.plot_select = QtWidgets.QPushButton(self.groupBox_6)
        self.plot_select.setGeometry(QtCore.QRect(50, 590, 93, 28))
        self.plot_select.setObjectName("plot_select")
        self.plot_box = QtWidgets.QGroupBox(self.plot_widget)
        self.plot_box.setGeometry(QtCore.QRect(200, 10, 721, 601))
        self.plot_box.setObjectName("plot_box")
        self.tabWidget.addTab(self.plot_widget, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.data_select.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.connect.setText(_translate("MainWindow", "Connect"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.label_4.setText(_translate("MainWindow", "Raw Message"))
        self.label_5.setText(_translate("MainWindow", "Delay"))
        self.delay.setText(_translate("MainWindow", "TextLabel"))
        self.label_12.setText(_translate("MainWindow", "State"))
        self.state.setText(_translate("MainWindow", "TextLabel"))
        self.local_time.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "Local Time"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.connect_widget), _translate("MainWindow", "Connect"))
        self.groupBox.setTitle(_translate("MainWindow", "BMP180"))
        self.label_6.setText(_translate("MainWindow", "Temperature"))
        self.label_7.setText(_translate("MainWindow", "Pressure"))
        self.label_8.setText(_translate("MainWindow", "Altitude"))
        self.temperature.setText(_translate("MainWindow", "TextLabel"))
        self.pressure.setText(_translate("MainWindow", "TextLabel"))
        self.altitude.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Acc"))
        self.acc_z.setText(_translate("MainWindow", "TextLabel"))
        self.acc_y.setText(_translate("MainWindow", "TextLabel"))
        self.label_13.setText(_translate("MainWindow", "Y-axis"))
        self.label_14.setText(_translate("MainWindow", "X-axis"))
        self.acc_x.setText(_translate("MainWindow", "TextLabel"))
        self.label_15.setText(_translate("MainWindow", "Z-axis"))
        self.groupBox_4.setTitle(_translate("MainWindow", "AnguSpeed"))
        self.angspe_z.setText(_translate("MainWindow", "TextLabel"))
        self.angspe_y.setText(_translate("MainWindow", "TextLabel"))
        self.label_19.setText(_translate("MainWindow", "Y-axis"))
        self.label_20.setText(_translate("MainWindow", "X-axis"))
        self.angspe_x.setText(_translate("MainWindow", "TextLabel"))
        self.label_21.setText(_translate("MainWindow", "Z-axis"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Posture"))
        self.label_24.setText(_translate("MainWindow", "Yaw"))
        self.label_22.setText(_translate("MainWindow", "Pitch"))
        self.roll_ang.setText(_translate("MainWindow", "TextLabel"))
        self.label_23.setText(_translate("MainWindow", "Roll"))
        self.pitch_ang.setText(_translate("MainWindow", "TextLabel"))
        self.yaw_ang.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GPS"))
        self.label_9.setText(_translate("MainWindow", "UTC"))
        self.label_10.setText(_translate("MainWindow", "Lat"))
        self.label_11.setText(_translate("MainWindow", "Lon"))
        self.time.setText(_translate("MainWindow", "TextLabel"))
        self.lat.setText(_translate("MainWindow", "TextLabel"))
        self.lon.setText(_translate("MainWindow", "TextLabel"))
        self.label_17.setText(_translate("MainWindow", "Freq"))
        self.freq.setText(_translate("MainWindow", "1"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Map"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rocket_widget), _translate("MainWindow", "Rocket"))
        self.data_save.setText(_translate("MainWindow", "Save"))
        self.data_clear.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.data_widget), _translate("MainWindow", "Data"))
        self.plot_save.setText(_translate("MainWindow", "Save"))
        self.plot_clear.setText(_translate("MainWindow", "Clear"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Data Select"))
        self.BMP180_combo.setItemText(0, _translate("MainWindow", "Temperature"))
        self.BMP180_combo.setItemText(1, _translate("MainWindow", "Pressure"))
        self.BMP180_combo.setItemText(2, _translate("MainWindow", "Altitude"))
        self.data_select.setTabText(self.data_select.indexOf(self.BMP180), _translate("MainWindow", "BMP180"))
        self.acc_x_check.setText(_translate("MainWindow", "X-axis"))
        self.acc_y_check.setText(_translate("MainWindow", "Y-axis"))
        self.acc_z_check.setText(_translate("MainWindow", "Z-axis"))
        self.data_select.setTabText(self.data_select.indexOf(self.acc), _translate("MainWindow", "Acc"))
        self.angspe_x_check.setText(_translate("MainWindow", "X-axis"))
        self.angspe_y_check.setText(_translate("MainWindow", "Y-axis"))
        self.angspe_z_check.setText(_translate("MainWindow", "Z-axis"))
        self.data_select.setTabText(self.data_select.indexOf(self.angle_speed), _translate("MainWindow", "Angu Speed"))
        self.roll_check.setText(_translate("MainWindow", "Roll"))
        self.pitch_check.setText(_translate("MainWindow", "Pitch"))
        self.yaw_check.setText(_translate("MainWindow", "Yaw"))
        self.data_select.setTabText(self.data_select.indexOf(self.posture), _translate("MainWindow", "Posture"))
        self.plot_select.setText(_translate("MainWindow", "OK"))
        self.plot_box.setTitle(_translate("MainWindow", "Plot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.plot_widget), _translate("MainWindow", "Plot"))
