import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

from untitled import *
from command import *
from wrong import *
from result import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    dialog = QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    ui1 = Ui_Dialog()
    ui1.setupUi(dialog)
    ui2 = Ui_Dialog2()
    dialog2 = QDialog()
    ui2.setupUi(dialog2)
    dialog3 = QDialog()
    ui3 = Ui_Dialog3()
    ui3.setupUi(dialog3)
    mainWindow.show()
    # ui是登录界面，ui1是成功后输入指令的界面，ui2是序列号错误后的页面，u3是最后的输出
    ui.pushButton.clicked.connect(mainWindow.close)
    # if right
    ui.pushButton.clicked.connect(dialog.show)
    # if command right
    ui1.pushButton.clicked.connect(dialog.close)
    ui1.pushButton.clicked.connect(dialog3.show)
    ui3.pushButton.clicked.connect(dialog3.close)
    # if wrong
    ui.pushButton.clicked.connect(dialog2.show)
    ui2.pushButton1.clicked.connect(mainWindow.show)
    ui2.pushButton1.clicked.connect(dialog2.close)
    ui2.pushButton2.clicked.connect(dialog2.close)
    sys.exit(app.exec_())
