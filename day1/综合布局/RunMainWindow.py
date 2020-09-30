import sys
import MainWindowHorizentalLayout
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    # 应用程序
    app = QApplication(sys.argv)
    # 主窗口
    mainWindow = QMainWindow()
    #
    ui = MainWindowHorizentalLayout.Ui_MainWindow()
    # 接受主窗口参数，添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
