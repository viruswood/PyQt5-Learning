import mainWindowVerticalLayout
from PyQt5.QtWidgets import QApplication,QMainWindow

import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = mainWindowVerticalLayout.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())