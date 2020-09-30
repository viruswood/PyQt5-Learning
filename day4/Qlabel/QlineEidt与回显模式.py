'''
基本功能：输入单行的文本
EchoMode 回显模式
4种回显模式
1 Normal
2 NoEcho
3 Password
4 PasswordEchoEdit
'''

from PyQt5.QtWidgets import *
import sys


class QlineEditEchoMode(QWidget):
    def __init__(self):
        super(QlineEditEchoMode, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本框输入的回显模式')

        formLayout = QFormLayout(self)
        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordNoEchoLineEdit = QLineEdit()

        formLayout.addRow("Normal", normalLineEdit)
        formLayout.addRow("NoEcho", noEchoLineEdit)
        formLayout.addRow("Password", passwordLineEdit)
        formLayout.addRow("passwordNoEcho", passwordNoEchoLineEdit)
        # placeholdertext
        normalLineEdit.setPlaceholderText("normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordNoEchoLineEdit.setPlaceholderText("passwordNoEcho")

        #setEchoMode
        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordNoEchoLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QlineEditEchoMode()
    widget.show()
    sys.exit(app.exec_())
