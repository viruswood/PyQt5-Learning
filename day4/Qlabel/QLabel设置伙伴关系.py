'''
QLabel与伙伴控件

mainLayout.addWidget(控件对象，rowIndex行位置，columnIndex列位置，行大小row，列大小column)

'''

from PyQt5.QtWidgets import *
import sys


class DemoLabel(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Qlabel与伙伴关系')
        nameLabel = QLabel("&Name", self)
        nameLineEdit = QLineEdit(self)
        nameLabel.setBuddy(nameLineEdit)
        passwordLabel = QLabel("&password", self)
        passwordLineEdit = QLineEdit(self)
        passwordLabel.setBuddy(passwordLineEdit)
        btnOK = QPushButton("&OK")
        btnCancel = QPushButton("&Cancel")
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)
        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(passwordLineEdit, 1, 1, 1, 2)
        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = DemoLabel()
    widget.show()
    sys.exit(app.exec_())
