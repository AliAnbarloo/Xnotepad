import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5 import uic
from Open_File import OPENFILE
from New_File import NEWFILE
from New_C import NEW_C
from New_Py import NEW_PY



class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        """
        Main window class for the application.

        Initializes the main window, connects actions to their respective
        methods, and sets up the user interface.

        Attributes:
        - open_action (QAction): Action to open a file.
        - new_action (QAction): Action to create a new file.
        """

        self.M_UI = uic.loadUi('UI/Main.ui', self)
        self.M_UI.show()
        self.New_File.clicked.connect(self.showCustomDialog)
        self.Open_File.clicked.connect(self.showCustomDialog)
        self.actionAbout.triggered.connect(self.showAboutDialog)
        self.actionHow_to_use.triggered.connect(self.showHowToUseDialog)
        self.actionNew_File.triggered.connect(self.showCustomDialog)
        self.actionOpen_File.triggered.connect(self.OpenFile)

    def OpenFile(self):

        """
        Method to handle the "Open" action.

        Opens the file dialog to allow the user to select a file.
        If a file is selected, it creates an instance of OPENFILE
        and displays the file content.
        """
        
        Open_Module = OPENFILE()   
        Open_Module.show()

    def NewFile(self):

        """
        Method to handle the "New" action.

        Creates an instance of NEWFILE and displays the new file interface.
        """

        New_Module = NEWFILE()   
        New_Module.show()
    def showAboutDialog(self):
        about_dialog = uic.loadUi('UI/Dialog/About.ui')
        about_dialog.exec_()

    def showHowToUseDialog(self):
        how_to_use_dialog = uic.loadUi('UI/Dialog/How_To_Use.ui')
        how_to_use_dialog.exec_()

    def showCustomDialog(self):
        custom_dialog = uic.loadUi('UI/Dialog/Cho.ui')

        # Connect buttons to empty functions
        custom_dialog.Normal.clicked.connect(self.NewFile)
        custom_dialog.Python.clicked.connect(self.pythonButtonClicked)
        custom_dialog.C_Bu.clicked.connect(self.cBuButtonClicked)
        custom_dialog.MarkDown.clicked.connect(self.NewFile)

        custom_dialog.exec_()

    # Empty functions for dialog buttons

    def pythonButtonClicked(self):
        New_Module_py = NEW_PY()   
        New_Module_py.show()

    def cBuButtonClicked(self):
        New_Module_C = NEW_C()   
        New_Module_C.show()


    def create_qapp():
        return QApplication([])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
