import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建QApplication实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    w.setWindowTitle('第一个应用')
    # w.resize(300,500)
    # w.move(300,300)
    w.setGeometry(300, 300, 500, 300)
    w.show()#显示
    # 进入程序的主循环、并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
