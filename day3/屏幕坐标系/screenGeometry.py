import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QPushButton


def onClick():
    widget.setWindowTitle('屏幕坐标系')
    print("widget.x()=%d" % widget.x())
    print("widget.y()=%d" % widget.y())
    print("widget.width()=%d" % widget.width())
    print("widget.height()=%d" % widget.height())
    print("widget.geometry().x()=%d" % widget.geometry().x())
    print("widget.geometry().y()=%d" % widget.geometry().y())
    print("widget.geometry().width()=%d" % widget.geometry().width())
    print("widget.geometry().height()=%d" % widget.geometry().height())

app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton(widget)
btn.setText('按钮')
btn.clicked.connect(onClick)
btn.move(24, 52)
widget.resize(300, 240)
widget.move(250, 200)

widget.show()
sys.exit(app.exec_())
