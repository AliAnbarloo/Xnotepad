import sys

from Open_File import OPENFILE
from New_File import NEWFILE
from New_C import NEW_C
from New_Py import NEW_PY

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction , QMessageBox
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5 import uic
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices


# Now

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
        self.Open_File.clicked.connect(self.OpenFile)
        self.we.clicked.connect(self.web)
        self.actionAbout.triggered.connect(self.showAboutDialog)
        self.actionHow_to_use.triggered.connect(self.showHowToUseDialog)
        self.actionNew_File.triggered.connect(self.showCustomDialog)
        self.actionOpen_File.triggered.connect(self.OpenFile)
        self.actionAll_Shortcuts.triggered.connect(self.AllShort)
        self.recent_files_model = QStandardItemModel()
        self.M_UI.listView.setModel(self.recent_files_model)
        self.M_UI.listView.clicked.connect(self.openRecentFile)

    def OpenFile(self):

        """
        Method to handle the "Open" action.

        Opens the file dialog to allow the user to select a file.
        If a file is selected, it creates an instance of OPENFILE
        and displays the file content.
        """
        
        Open_Module = OPENFILE()   
        Open_Module.show()

    def addFileToRecentList(self, file_path):
            item = QStandardItem(file_path)
            self.recent_files_model.appendRow(item)

    def openRecentFile(self, index):
        selected_item = self.recent_files_model.itemFromIndex(index)
        selected_file = selected_item.text()
        self.loadFile(selected_file)


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
        custom_dialog.Normal.clicked.connect(self.NewFile)
        custom_dialog.Python.clicked.connect(self.pythonButtonClicked)
        custom_dialog.C_Bu.clicked.connect(self.cBuButtonClicked)
        custom_dialog.MarkDown.clicked.connect(self.show_popup)

        custom_dialog.exec_()

    # Empty functions for dialog buttons

    def pythonButtonClicked(self):
        New_Module_py = NEW_PY()   
        New_Module_py.show()

    def cBuButtonClicked(self):
        New_Module_C = NEW_C()   
        New_Module_C.show()

    def show_popup(self):
        popup = QMessageBox()
        popup.setText('Coming Soon!')
        popup.setIcon(QMessageBox.Information)
        popup.addButton(QMessageBox.Ok)
        popup.exec_()

    def AllShort(self):
        All_Short_dialog = uic.loadUi('UI/Dialog/AllShort.ui')
        All_Short_dialog.exec_()

    def web(self):
        web_page_url = QUrl('https://www.github.com')
        QDesktopServices.openUrl(web_page_url)

    def create_qapp():
        return QApplication([])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
