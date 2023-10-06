import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5 import uic
from Open_File import OPENFILE
from New_File import NEWFILE

# ...

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        # Load the UI file 
        self.M_UI = uic.loadUi('UI/Main.ui', self)
        self.M_UI.show()
        self.New_File.clicked.connect(self.NewFile)
        self.Open_File.clicked.connect(self.OpenFile)
        self.actionAbout.triggered.connect(self.showAboutDialog)
        self.actionHow_to_use.triggered.connect(self.showHowToUseDialog)
        self.actionNew_File.triggered.connect(self.NewFile)
        self.actionOpen_File.triggered.connect(self.OpenFile)

    def OpenFile(self):
        Open_Module = OPENFILE()   
        Open_Module.show()

    def NewFile(self):
        New_Module = NEWFILE()   
        New_Module.show()
    def showAboutDialog(self):
        about_dialog = uic.loadUi('UI/Dialog/About.ui')
        about_dialog.exec_()

    def showHowToUseDialog(self):
        how_to_use_dialog = uic.loadUi('UI/Dialog/How_To_Use.ui')
        how_to_use_dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
