import sys , os
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5 import uic
from Open_File import OPENFILE
from New_File import NEWFILE
from main_UI import MyWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())