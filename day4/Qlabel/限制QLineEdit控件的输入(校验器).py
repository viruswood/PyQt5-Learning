'''
限制QLineEidt控件的输入（校验器）
1 只能输入证书、浮点数或满足一定条件的字符串
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys


class QLineEditVlidator(QWidget):
    def __init__(self):
        super(QLineEditVlidator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QlineLabel校验器')
        formlayout = QFormLayout(self)
        intLineEdit = QLineEdit()
        doubleLineEidt = QLineEdit()
        validatorLineEdit = QLineEdit()

        formlayout.addRow('整数类型', intLineEdit)
        formlayout.addRow('浮点数 ', doubleLineEidt)
        formlayout.addRow('数字字母', validatorLineEdit)

        intLineEdit.setPlaceholderText('整数')
        doubleLineEidt.setPlaceholderText('浮点数')
        validatorLineEdit.setPlaceholderText('字母')

        # 整数校验器
        intValidator = QIntValidator(self)
        intValidator.setRange(1, 99)
        doubleValidator = QDoubleValidator(self)

        doubleValidator.setRange(-360, 360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        intLineEdit.setValidator(intValidator)
        doubleLineEidt.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QLineEditVlidator()
    widget.show()
    sys.exit(app.exec_())
