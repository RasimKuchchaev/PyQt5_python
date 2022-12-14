import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Choose color', self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        # color = QColorDialog.getColor(QColor('red'), self, 'Choose color')
        # color = QColorDialog.getColor(QColor('#FF0000'), self, 'Choose color')
        # color = QColorDialog.getColor(QColor(255, 0, 0), self, 'Choose color')
        color = QColorDialog.getColor(QColor(255, 0, 0, 255), self, 'Choose color')
        print(color)



if __name__ == '__main__':
    app = QApplication(sys.argv)        # create application
    dlgMain = DlgMain()                 # create main GUI windows
    dlgMain.show()                      # show GUI
    sys.exit(app.exec_())               # execute the application
