import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Windows')
        self.resize(400, 200)

        self.cmbState = QComboBox(self)
        self.cmbState.move(50, 50)
        # self.cmbState.addItems(['AL', 'AR', 'MA', 'MO', 'MI'])
        # self.cmbState.currentTextChanged.connect(self.evt_cmb_state_changed)
        self.cmbState.addItem('Alabama', 'AL')
        self.cmbState.addItem('Alaska', 'AL')
        self.cmbState.addItem('Minnesota', 'MA')
        self.cmbState.addItem('Missouri', 'MO')
        self.cmbState.addItem('Michigan', 'MI')
        self.cmbState.currentIndexChanged.connect(self.evt_cmb_state_changed_index)
        self.cmbState.highlighted.connect(self.evt_cmb_state_highlighted)   # highlighted сигнал выбора

        self.lblAbrr = QLabel('State Abbreviation AL', self)
        self.lblAbrr.resize(150, 30)
        self.lblAbrr.move(170, 50)

    def evt_cmb_state_highlighted(self, idx):
        self.lblAbrr.setText('State Abbreviation {}'.format(self.cmbState.itemData(idx)))

    def evt_cmb_state_changed(self, txt):
        QMessageBox.information(self, 'ComboBox', 'You have selected {}'.format(txt))

    def evt_cmb_state_changed_index(self, idx):
        QMessageBox.information(self, 'ComboBox', 'You have selected {}'.format(self.cmbState.itemData(idx)))


if __name__ == '__main__':
    app = QApplication(sys.argv)        # create application
    dlgMain = DlgMain()                 # create main GUI windows
    dlgMain.show()                      # show GUI
    sys.exit(app.exec_())               # execute the application
