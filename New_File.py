import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog
from PyQt5 import uic

class NEWFILE(QMainWindow):
    def __init__(self):
        super(NEWFILE, self).__init__()
        self.N_UI = uic.loadUi('UI/Text_edit.ui', self)
        self.N_UI.show()

        # Connect actions to their respective methods
        self.actionCopy.triggered.connect(self.copyText)
        self.actionCut.triggered.connect(self.cutText)
        self.actionPaste.triggered.connect(self.pasteText)
        self.actionSelectAll.triggered.connect(self.selectAllText)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_As.triggered.connect(self.saveFileAs)
        self.actionAbout.triggered.connect(self.showAboutDialog)
        self.actionHow_to_use.triggered.connect(self.showHowToUseDialog)

    def copyText(self):
        selected_text = self.textEdit.textCursor().selectedText()
        clipboard = QApplication.clipboard()
        clipboard.setText(selected_text)

    def cutText(self):
        # Get the selected text
        selected_text = self.textEdit.textCursor().selectedText()

        # Copy the selected text to the clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText(selected_text)

        # Delete the selected text from the textEdit
        self.textEdit.textCursor().removeSelectedText()

    def pasteText(self):
        # Get the text from the clipboard
        clipboard = QApplication.clipboard()
        text_to_paste = clipboard.text()

        # Insert the text from the clipboard at the current cursor position
        self.textEdit.textCursor().insertText(text_to_paste)
    def selectAllText(self):
        self.textEdit.selectAll()
    def loadFile(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                self.textEdit.setPlainText(file_content)
        except Exception as e:
            print(f"Error loading file: {e}")
    def saveFile(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(self.textEdit.toPlainText())
            except Exception as e:
                print(f"Error saving file: {e}")

    def saveFileAs(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File As", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(self.textEdit.toPlainText())
            except Exception as e:
                print(f"Error saving file: {e}")
    def showAboutDialog(self):
        about_dialog = uic.loadUi('UI/Dialog/About.ui')
        about_dialog.exec_()

    def showHowToUseDialog(self):
        how_to_use_dialog = uic.loadUi('UI/Dialog/How_To_Use.ui')
        how_to_use_dialog.exec_()


# ...

if __name__ == '__main__':
    # app = QApplication(sys.argv)  # حذف این خط
    window = NEWFILE()
    sys.exit(app.exec_())
