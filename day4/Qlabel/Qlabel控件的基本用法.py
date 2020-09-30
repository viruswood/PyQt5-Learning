'''
setAlignment() :设置文本对齐方式
setIndent()：设置文本缩进
text()获取文本内容
setBuddy设置伙伴关系
selectedText()返回选择的字符
setWordWrap()设置是否允许换行


Qlabel常用的信号（事件）
鼠标滑过 linkHovered
鼠标点击 linkActivated
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPalette, QFont, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout


class QlabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        label1.setText('<font color=yellow>这是一个文本标签</font>')
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)

        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)
        label2.setAutoFillBackground(True)
        palette2 = QPalette()
        palette2.setColor(QPalette.Window, Qt.green)
        label2.setPalette(palette2)
        label2.setText('<font color=yellow>欢迎GUI程序</font>')
        # label2.setFont()
        label2.setAlignment(Qt.AlignCenter)
        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片')
        label3.setPixmap(QPixmap('../../images/aaa.jpg'))
        label4.setText("<a href ='http://code.py40.com/pyqt5/22.html'>sssz</a>")
        label4.setToolTip('这是一个超链接')

        label4.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)
        label4.setAlignment(Qt.AlignCenter)



        vBox = QVBoxLayout()
        vBox.addWidget(label1)
        vBox.addWidget(label2)
        vBox.addWidget(label3)
        vBox.addWidget(label4)

        self.setLayout(vBox)
        self.setWindowTitle('Qlabel控件演示')

    def linkHovered(self):
        print('鼠标滑过label2,出发事件')

    def linkClicked(self):
        print('鼠标点击label4,出发事件')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QlabelDemo()
    widget.show()
    sys.exit(app.exec_())

