import sys
from PyQt5.QtWidgets import QToolTip, QPushButton, QApplication, QWidget
from PyQt5.QtGui import QFont


class ToolTipMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 16))
        self.setGeometry(400, 400, 500, 400)
        self.setToolTip('窗口提示')
        self.setWindowTitle('窗口')
        btn = QPushButton('按钮', self)
        btn.move(50, 50)
        btn.setToolTip('控件提示')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = ToolTipMainWindow()
    widget.show()
    sys.exit(app.exec_())
