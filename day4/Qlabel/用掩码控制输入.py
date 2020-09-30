from PyQt5.QtWidgets import *
import sys

class QLineEidtMask(QWidget):
    def __init__(self):
        super(QLineEidtMask, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('掩码限制输入')
        formLayout = QFormLayout(self)
        ipLineEdit = QLineEdit()
        mackLineEdit = QLineEdit()
        dateLineEdit = QLineEdit()
        linceseLineEidt = QLineEdit()

        ipLineEdit.setInputMask('000.000.000.000;_')
        mackLineEdit.setInputMask('HH:HH:HH:HH:HH:HH;_')
        dateLineEdit.setInputMask('0000-00-00')
        linceseLineEidt.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')

        formLayout.addRow('数字掩码', ipLineEdit)
        formLayout.addRow('mac掩码', mackLineEdit)
        formLayout.addRow('日期掩码', dateLineEdit)
        formLayout.addRow('许可证掩码', linceseLineEidt)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QLineEidtMask()
    widget.show()
    sys.exit(app.exec_())
