import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QPushButton

from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QDesktopWidget


class QuitApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("退出程序，关闭窗口")
        self.resize(800, 600)
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息', 5000)
        self.center()
        self.button = QPushButton('退出应用程序')
        # self.button.move(50, 50)

        self.button.clicked.connect(self.onClickButton)
        layout = QHBoxLayout()
        layout.addWidget(self.button)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onClickButton(self):
        sender = self.sender()
        print(sender.text() + '按钮被点击')
        QApplication.instance().quit()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft, newTop)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QuitApplication()
    mainWindow.center()
    mainWindow.show()
    # app.setWindowIcon(QIcon())
    sys.exit(app.exec_())
