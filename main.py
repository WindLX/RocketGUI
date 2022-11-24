import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import rocket_ui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = rocket_ui.RocketUi()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
