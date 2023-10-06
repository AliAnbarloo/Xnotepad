from New_File import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QVBoxLayout, QWidget
import sys

class OPENFILE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.XX = ""
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        # باز کردن پنجره انتخاب فایل
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)", options=options)

        if file_name:
            # نمایش آدرس فایل انتخاب شده در کنسول
            print("Selected File:", file_name)

            # ذخیره آدرس فایل در متغیر XX
            self.XX = file_name

            # ایجاد نمونه از کلاس NEWFILE
            New_File_Module = NEWFILE()
            
            # بارگذاری محتوای فایل به textEdit
            New_File_Module.loadFile(self.XX)
            
            # نمایش پنجره NEWFILE
            New_File_Module.show()
# ...

if __name__ == '__main__':
    # app = QApplication(sys.argv)  # حذف این خط
    window = OPENFILE()
    window.show()
    sys.exit(app.exec_())

