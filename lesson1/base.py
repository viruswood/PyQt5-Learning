import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建应用程序对象，sys.argv为参数列表，从命令行输入参数
    app = QApplication(sys.argv)
    # QWidget 是 所有用户对象的基类，为Qwidget 提供构造函数，没有父类
    w = QWidget()
    w.resize(600, 500)
    # 调整窗口大小
    w.move(300, 300)
    # 移动到窗口位置
    w.setWindowTitle('Simple')
    # 设置窗口标题
    w.show()
    # 显示在屏幕上
    # exit 保证程序干净退出
    # 执行是一个关键词用exec_代替
    sys.exit(app.exec_())
