import sys , os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QTextEdit, QVBoxLayout, QWidget, QPushButton ,  QUndoStack, QUndoCommand 

class MyCommand(QUndoCommand):
    def __init__(self, text_edit, old_text, new_text):
        super(MyCommand, self).__init__()
        self.text_edit = text_edit
        self.old_text = old_text
        self.new_text = new_text

    def redo(self):
        self.text_edit.setPlainText(self.new_text)

    def undo(self):
        self.text_edit.setPlainText(self.old_text)
class NEW_PY(QMainWindow):
    def __init__(self):
        super(NEW_PY, self).__init__()

        self.N_UI = uic.loadUi('UI/PyCode.ui', self)
        self.N_UI.show()

        self.actionCopy.triggered.connect(self.copyText)
        self.actionCut.triggered.connect(self.cutText)
        self.actionPast.triggered.connect(self.pasteText)
        self.actionSelectAll.triggered.connect(self.selectAllText)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_As.triggered.connect(self.saveFileAs)
        self.actionRun.triggered.connect(self.runScript)

        self.file_path = None  # متغیری برای ذخیره مسیر فایل

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
                self.file_path = file_path  # تنظیم مسیر فایل
                self.addFileToRecentList(file_path)
        except Exception as e:
            print(f"Error loading file: {e}")

    def saveFile(self):
        if self.file_path:  # اگر فایل ذخیره شده است
            try:
                with open(self.file_path, 'w', encoding='utf-8') as file:
                    file.write(self.textEdit.toPlainText())
            except Exception as e:
                print(f"Error saving file: {e}")
        else:
            self.saveFileAs()  # اگر فایل ذخیره نشده باشد، از دیالوگ Save استفاده کنید

    def saveFileAs(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File As", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(self.textEdit.toPlainText())
                self.file_path = file_path  # تنظیم مسیر فایل
            except Exception as e:
                print(f"Error saving file: {e}")

    def runScript(self):
        cm = f"python3 {self.file_path}"
        if self.file_path:
            os.system(cm)
        else:
            self.saveFileAs()
            os.system(cm)
    def keyPressEvent(self, event):
        # ذخیره تغییرات در UndoStack به صورت خودکار هر زمان که یک کلید فشار داده شود
        if event.modifiers() & Qt.ControlModifier and event.key() == Qt.Key_Z:
            self.undo_stack.undo()
        elif event.modifiers() & QApplication.ControlModifier and event.key() == Qt.Key_Y:
            self.undo_stack.redo()
        else:
            super(NEW_PY, self).keyPressEvent(event)

if __name__ == '__main__':
    os.system("clear")
    app = QApplication(sys.argv)
    window = NEW_PY()
    sys.exit(app.exec_())
