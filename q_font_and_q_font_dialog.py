import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Choose font', self)
        self.btn.move(35, 50)
        font = QFont('Arial', 12, 75, True)
        self.btn.setFont(font)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        font, b_ok = QFontDialog.getFont()
        print(font, b_ok)
        if b_ok:
            print(font.family())
            print(font.italic())
            print(font.bold())
            print(font.weight())
            print(font.pointSize())
            self.btn.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)        # create application
    dlgMain = DlgMain()                 # create main GUI windows
    dlgMain.show()                      # show GUI
    sys.exit(app.exec_())               # execute the application
