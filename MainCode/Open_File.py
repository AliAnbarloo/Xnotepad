from New_File import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QVBoxLayout, QWidget
import sys

"""Open_File is used to find the file address and then open it in a New_File"""

class OPENFILE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.XX = ""
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)", options=options)

        if file_name:
            print("Selected File:", file_name)
            self.XX = file_name
            New_File_Module = NEWFILE()
            New_File_Module.loadFile(self.XX)
            New_File_Module.show()

if __name__ == '__main__':
    window = OPENFILE()
    window.show()
    sys.exit(app.exec_())

