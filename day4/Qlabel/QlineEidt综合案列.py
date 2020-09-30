from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import sys


class QLabelDemo(QWidget):
    def __init__(self):
        super(QLabelDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel综合案例')

        edit1 = QLineEdit()
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)
        edit1.setAlignment(Qt.AlignRight)
        # edit1.setFont(QFont('Arial', 16))

        edit2 = QLineEdit()
        edit2.setValidator(QDoubleValidator(0.0, 99.99, 2))

        edit3 = QLineEdit()
        edit3.setInputMask('99_9999_999999;#')

        edit4 = QLineEdit()
        edit4.textChanged.connect(self.textChange)

        edit5 = QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)
        edit5.editingFinished.connect(self.enterPress)
        edit6 = QLineEdit('Hello world')
        edit6.setReadOnly(True)
        formLayout = QFormLayout(self)
        formLayout.addRow('整数校验', edit1)
        formLayout.addRow('浮点数', edit2)
        formLayout.addRow('input_mask', edit3)
        formLayout.addRow('文本变化', edit4)
        formLayout.addRow('密码', edit5)
        formLayout.addRow('只读', edit6)
        self.setLayout(formLayout)
    def textChange(self,text):
        print('输入的内容' + text)
    def enterPress(self):
        print('已输入')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QLabelDemo()
    widget.show()
    sys.exit(app.exec_())
