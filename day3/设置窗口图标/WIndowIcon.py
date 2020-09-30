import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon


class IconForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('设置窗口图标')
        self.setWindowIcon(QIcon('../../images/aaa.jpg'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = IconForm()
    widget.show()
    sys.exit(app.exec_())
