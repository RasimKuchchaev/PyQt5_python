import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Show Message', self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        # # # Method 1
        # # res = QMessageBox.information(self, 'Disk Full', 'Your disk drive is almost full')
        # # res = QMessageBox.warning(self, 'Disk Full', 'Your disk drive is almost full')
        # # res = QMessageBox.critical(self, 'Disk Full', 'Your disk drive is almost full')
        # res = QMessageBox.question(self, 'Disk Full', 'Your disk drive is almost full')
        # print(res)      # res code(int) button(OK, Cancel,...)
        # if res == QMessageBox.Yes:
        #     QMessageBox.information(self, 'clicked "Yes"', 'You ve clicked "Yes" button')
        # if res == QMessageBox.No:
        #     QMessageBox.information(self, 'clicked "No"', 'You ve clicked "No" button')


        # # # Method 2
        msgDiskFull = QMessageBox()
        msgDiskFull.setText('Your disk drive is almost full')
        msgDiskFull.setDetailedText('Please free up disk space')    # button show detail
        msgDiskFull.setIcon(QMessageBox.Information)
        msgDiskFull.setWindowTitle('Disk Full')
        msgDiskFull.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgDiskFull.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)        # create application
    dlgMain = DlgMain()                 # create main GUI windows
    dlgMain.show()                      # show GUI
    sys.exit(app.exec_())               # execute the application
