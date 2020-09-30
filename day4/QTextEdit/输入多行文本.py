'''
QTextEdit
'''
from PyQt5.QtWidgets import *
import sys


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTextEdit控件')
        self.resize(300, 200)
        self.textEidt = QTextEdit()
        self.buttonText = QPushButton('显示文本')
        self.buttonHtml = QPushButton('显示Html')
        self.buttonText.clicked.connect(self.onClickButtonText)
        self.buttonHtml.clicked.connect(self.onClickButotnHtml)

        layout = QVBoxLayout()
        layout.addWidget(self.textEidt)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHtml)
        self.setLayout(layout)
    def onClickButtonText(self):
        self.textEidt.setPlainText('Hello word')

    def onClickButotnHtml(self):
        self.textEidt.setHtml('<font color="blue" size="5">hello World</font>')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Demo()
    widget.show()
    sys.exit(app.exec_())
