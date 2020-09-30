import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QDesktopWidget


class CenterMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口居中")
        self.resize(800, 600)
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息', 5000)
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width()-size.width())/2
        newTop = (screen.height()-size.height())/2
        self.move(newLeft,newTop)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = CenterMainWindow()
    # mainWindow.center()
    mainWindow.show()

    # app.setWindowIcon(QIcon())
    sys.exit(app.exec_())
