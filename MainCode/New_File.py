import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog , QUndoStack, QUndoCommand 
from PyQt5 import uic
class MyCommand(QUndoCommand):
    def __init__(self, text_edit, old_text, new_text):
        super(MyCommand, self).__init__()
        self.text_edit = text_edit
        self.old_text = old_text
        self.new_text = new_text
class NEWFILE(QMainWindow):
    def __init__(self):
        super(NEWFILE, self).__init__()

        self.N_UI = uic.loadUi('UI/Text_edit.ui', self)
        self.N_UI.show()

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
        selected_text = self.textEdit.textCursor().selectedText()
        clipboard = QApplication.clipboard()
        clipboard.setText(selected_text)
        self.textEdit.textCursor().removeSelectedText()

    def pasteText(self):
        clipboard = QApplication.clipboard()
        text_to_paste = clipboard.text()
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
    def keyPressEvent(self, event):
        # ذخیره تغییرات در UndoStack به صورت خودکار هر زمان که یک کلید فشار داده شود
        if event.modifiers() & Qt.ControlModifier and event.key() == Qt.Key_Z:
            self.undo_stack.undo()
        elif event.modifiers() & QApplication.ControlModifier and event.key() == Qt.Key_Y:
            self.undo_stack.redo()
        else:
            super(NEW_PY, self).keyPressEvent(event)

if __name__ == '__main__':
    window = NEWFILE()
    sys.exit(app.exec_())
