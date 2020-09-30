from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class PushButton(QDialog):
    def __init__(self):
        super(PushButton, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('按钮')

        layout = QVBoxLayout(self)
        self.button1 = QPushButton('第一个Buttion')
        self.button1.setCheckable(True)
        self.button1.toggle()
        # 只能传入一个参数，使用lambda硬编码
        self.button1.clicked.connect(lambda: self.whichButton(self.button1))
        self.button1.clicked.connect(self.buttonState)
        layout.addWidget(self.button1)

        # 文本前显示图像
        self.button2 = QPushButton('button2')
        self.button2.setIcon(QIcon(QPixmap('../../images/aaa.jpg')))
        self.button2.clicked.connect(lambda: self.whichButton(self.button2))
        layout.addWidget(self.button2)
        self.button3 = QPushButton('不可用的Button')
        self.button3.setEnabled(False)
        layout.addWidget(self.button3)

        self.button4 = QPushButton('&第四个button')
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda: self.whichButton(self.button4))
        layout.addWidget(self.button4)

        self.setLayout(layout)
        self.resize(400, 300)

    def whichButton(self, btn):
        print('被单击的按钮是' + btn.text())

    def buttonState(self):
        if self.button1.isChecked():
            print('按钮一已被选中')
        else:
            print('按钮一未被选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = PushButton()
    widget.show()
    sys.exit(app.exec_())
