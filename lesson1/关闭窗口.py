import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        # 设置窗口的提示语
        self.setToolTip('this is a <b>Qwidget</b> widget')
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        # 按钮的提示语
        qbtn.setToolTip('this is a <b>QPushButton</b> widget')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('ToolTip')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
