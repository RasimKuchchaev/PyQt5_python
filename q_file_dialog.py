import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Open file', self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        # res = QFileDialog.getOpenFileName(self, 'Open file', 'C:\PythonCode\PyQt5_python', 'JPG File (*.jpg)')
        # res = QFileDialog.getOpenFileName(self, 'Open file', 'C:\PythonCode\PyQt5_python', 'JPG File (*.jpg);;Py File(*.py)')

        # res = QFileDialog.getSaveFileName(self, 'Save file', 'C:\PythonCode\PyQt5_python', 'JPG File (*.jpg);;Py File(*.py)')

        res = QFileDialog.getOpenFileNames(self, 'Open file', 'C:\PythonCode\PyQt5_python', 'JPG File (*.jpg);;Py File(*.py)')


        print(res)


if __name__ == '__main__':
    app = QApplication(sys.argv)        # create application
    dlgMain = DlgMain()                 # create main GUI windows
    dlgMain.show()                      # show GUI
    sys.exit(app.exec_())               # execute the application
