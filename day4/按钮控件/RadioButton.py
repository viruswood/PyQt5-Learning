from PyQt5.QtWidgets import *
import sys

class RadioButton(QWidget):
    def __init__(self):
        super(RadioButton, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QRadioButton')
        layout = QHBoxLayout(self)
        self.button1 = QRadioButton('单选1')
        self.button1.setChecked(True)
        self.button1.toggled.connect(self.buttonState)
        layout.addWidget(self.button1)

        self.button2 = QRadioButton('单选2')
        self.button2.toggled.connect(self.buttonState)
        layout.addWidget(self.button2)
        self.setLayout(layout)

    def buttonState(self):
        radioButton = self.sender()
        print(radioButton.text())
        print(radioButton.isChecked())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = RadioButton()
    widget.show()
    sys.exit(app.exec_())
