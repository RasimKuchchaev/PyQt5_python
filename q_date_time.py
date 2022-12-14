import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Dates', self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        dt = QDate.currentDate()
        print(dt.toString())
        print(dt.toJulianDay())
        print(dt.dayOfWeek())
        print(dt.dayOfYear())
        print(dt.addDays(21).toString())

        tm = QTime(13, 20)
        print(tm.toString())
        tm = QTime(13, 20, 25, 346)
        print(tm.toString())
        print(tm.msec())

        tm1 =QTime(13, 20)
        tm2 =QTime(15, 20)
        tm_a = tm2.addSecs(60)
        print(tm1.toString())
        print(tm_a.toString())
        print(tm1.secsTo(tm2))

        dtm = QDateTime.currentDateTime()
        print(dtm.toString())




if __name__ == '__main__':
    app = QApplication(sys.argv)        # create application
    dlgMain = DlgMain()                 # create main GUI windows
    dlgMain.show()                      # show GUI
    sys.exit(app.exec_())               # execute the application
