import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Windows')
        self.resize(400, 200)

        self.spbInt = QSpinBox(self)
        self.spbInt.move(50, 50)
        self.spbInt.setWrapping(True)   # 1, 0, 99 замкнутый цикл
        self.spbInt.setRange(0, 1000)   # диапозон мин, макс
        self.spbInt.setSingleStep(100)  # шаг 100
        self.spbInt.setValue(100)       # значение 100
        self.spbInt.valueChanged.connect(self.evt_spb_int_value_change)
        self.spbInt.editingFinished.connect(self.evt_spb_int_editing_finished)  # editingFinished сигнал окончание редактирования


        self.spbDbl = QDoubleSpinBox(self)
        self.spbDbl.move(50, 80)
        self.spbDbl.setDecimals(2)
        self.spbDbl.setSingleStep(0.01)
        self.spbDbl.setPrefix('Height ')    # строка до числа
        self.spbDbl.setSuffix(' meter')     # строка после числа
        self.spbDbl.setRange(0.40, 3.00)
        self.spbDbl.valueChanged.connect(self.evt_spb_dbl_value_change)

    def evt_spb_dbl_value_change(self, val):
        print(self.spbDbl.text())
        print(self.spbDbl.value())

    def evt_spb_int_value_change(self, val):
        print(val, val % 100)
        if val % 100:
            self.spbInt.setStyleSheet('color: red')
        else:
            self.spbInt.setStyleSheet('color: black')

    def evt_spb_int_editing_finished(self):
        if self.spbInt.value() % 100:
            QMessageBox.critical(self, 'Invalid number', 'Invalid value was entered \n\nMust be divisible by 100')

            self.spbInt.setFocus()      # установка фокуса на spbInt

if __name__ == '__main__':
    app = QApplication(sys.argv)        # create application
    dlgMain = DlgMain()                 # create main GUI windows
    dlgMain.show()                      # show GUI
    sys.exit(app.exec_())               # execute the application
