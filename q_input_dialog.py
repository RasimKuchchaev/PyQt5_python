import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Show Input', self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        # res = QInputDialog.getText(self, 'Title', 'Enter you name:')
        # print(res)

        # s_name, b_ok = QInputDialog.getText(self, 'Title', 'Enter you name:')
        # if b_ok:
        #     QMessageBox.information(self, 'Name', 'Your name is: ' + s_name)
        # else:
        #     QMessageBox.critical(self, 'Canceled', 'User have clicked "Cancel"')

        # i_age, b_ok = QInputDialog.getInt(self, 'Title', 'Enter you age: ', 18, 18, 65, 1)
        # if b_ok:
        #     QMessageBox.information(self, 'Age', 'Your age is: ' +str(i_age))
        # else:
        #     QMessageBox.critical(self, 'Canceled', 'User have clicked "Cancel"')

        # d_height, b_ok = QInputDialog.getDouble(self, 'Title', 'Enter you height in meters: ', 1.70, 0.60, 2.50, 2)
        # if b_ok:
        #     QMessageBox.information(self, 'Height', 'Your height is: ' +str(d_height))
        # else:
        #     QMessageBox.critical(self, 'Canceled', 'User have clicked "Cancel"')

        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
        s_color, b_ok = QInputDialog.getItem(self, 'Title', 'Enter you color: ', colors, editable=True)     # editable - edit input dialog
        if b_ok:
            QMessageBox.information(self, 'Color', 'Your color is: ' + s_color)
        else:
            QMessageBox.critical(self, 'Canceled', 'User have clicked "Cancel"')


if __name__ == '__main__':
    app = QApplication(sys.argv)        # create application
    dlgMain = DlgMain()                 # create main GUI windows
    dlgMain.show()                      # show GUI
    sys.exit(app.exec_())               # execute the application
