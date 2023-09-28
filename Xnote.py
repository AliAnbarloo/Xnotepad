import sys , os , random
from playsound import playsound
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow

os.system("clear")
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(500,500,300,300)
        self.setWindowTitle("GOD DAMN IT")
        self.intUI()
    def intUI(self):
        self.la = QtWidgets.QLabel(self)
        self.la.setText("Polish cow")
        self.la.adjustSize()
        self.la.move(30,30)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("play") , self.b1.move(160,160) , self.b1.clicked.connect(self.goddamn_clicked)
    def goddamn_clicked(self):
        self.la.setText("playing polish cow...")
        self.updater()
        playsound("/home/ubuntu/بارگیری‌ها/yt1s.io - Polish Cow (Full Version) (128 kbps).mp3")
    def updater(self):
        self.la.adjustSize()


def start():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
start()