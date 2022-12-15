import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)

        self.btn = QPushButton('Disable Label ', self)
        self.btn.move(35, 50)
        self.btn.setIcon(QIcon(QPixmap('icon.png')))
        self.btn.clicked.connect(self.evt_btn_clicked)

        self.lbl = QLabel('Label Text', self)
        self.lbl.move(10, 100)
        self.lbl.resize(480, 319)
        font = QFont('Times New Roman', 24, 75, True)
        self.lbl.setFont(font)

    def evt_btn_clicked(self):
        if self.lbl.isEnabled():        # проверка доступен Label
            self.lbl.setDisabled(True)   # не доступен Label
            self.btn.setText('Enable Label')
        else:
            # self.lbl.setDisabled(False)
            self.lbl.setEnabled(True)
            self.btn.setText('Desable Label')


if __name__ == '__main__':
    app = QApplication(sys.argv)        # create application
    dlgMain = DlgMain()                 # create main GUI windows
    dlgMain.show()                      # show GUI
    sys.exit(app.exec_())               # execute the application
