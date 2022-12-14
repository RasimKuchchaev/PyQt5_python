import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Windows')
        self.resize(400, 200)

        self.ledTitle = QLineEdit(self.windowTitle(), self)
        self.ledTitle.setPlaceholderText('Enter a new windows title')  # подсказка
        # self.ledTitle.setReadOnly(True)             # только для чтения
        self.ledTitle.setEchoMode(QLineEdit.Password)       # для работы с паролями
        # self.ledTitle.setAlignment(Qt.AlignRight)           # выравнивание текста по правому краю
        self.ledTitle.setAlignment(Qt.AlignCenter)           # выравнивание текста по центру
        self.ledTitle.move(50, 50)
        self.btnUpdate = QPushButton('Update Title', self)
        self.btnUpdate.move(150, 100)
        self.btnUpdate.clicked.connect(self.evt_btn_update_clicked)         # сигнал clicked
        self.ledTitle.textChanged.connect(self.evt_led_title_text_change)   # сигнал textChanged от программы

    def evt_led_title_text_change(self, title):
        self.setWindowTitle(title)

    def evt_btn_update_clicked(self):
        res = QMessageBox.question(self, 'Title Editing', 'Do you want to change the title to"'
                                   + self.ledTitle.text() + '"?')
        if res==QMessageBox.Yes:
            self.setWindowTitle(self.ledTitle.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)        # create application
    dlgMain = DlgMain()                 # create main GUI windows
    dlgMain.show()                      # show GUI
    sys.exit(app.exec_())               # execute the application
