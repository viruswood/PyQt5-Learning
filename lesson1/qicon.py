from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        # 界面绘制交给initUI方法
        self.initUI()

    def initUI(self):
        # 设置窗口位置和大小
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        # 引用 data目录下的aaa.jpg图片
        self.setWindowIcon(QIcon('data/aaa.jpg'))
        self.show()


if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
