import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 设置窗口的尺寸
    w.resize(300, 150)
    # 移动窗口
    w.move(300, 300)
    # 设置窗口的标题
    w.setWindowTitle("第一个基于PyQT5的应用")
    # 显示窗口
    w.show()

    # 进入主程序循环,并通过exit函数主循环安全的结束
    sys.exit(app.exec_())






