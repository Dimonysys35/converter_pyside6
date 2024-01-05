import sys
from PySide6 import QtWidgets
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator
from ui_converter import Ui_Converter
import json

with open("measurments.json", "r") as f:
    config = json.load(f)
#print(json.dumps(config,indent= 1))
measurments = ["length", "area", "volume", "mass", "temperature", "speed", "time"]
templist = ["K", "C", "F"]
measurment = ""
currentmeasurment = {}
currentindex = 0
number1 = 0
number2 = 0
measure1 = ""
measure2 = ""
converttemper = False

class Converter(QtWidgets.QMainWindow):
    def __init__(self):
        super(Converter, self).__init__()
        self.ui = Ui_Converter()
        self.ui.setupUi(self)
        #self.ui.MainWindow.setWindowTitle("Converter")
        self.ui.Measurments.currentIndexChanged.connect(self.fillboxes)
        self.ui.Measurments.currentIndexChanged.emit(self)
        self.ui.Select1.activated.connect(self.setsel1)
        self.ui.Select2.activated.connect(self.setsel2)
        validator = QRegularExpressionValidator("[+-]?([0-9]*[.])?[0-9]+", self)#QIntValidator(-2147483648, 2147483647)
        self.ui.Number1.setValidator(validator)
        self.ui.Number2.setValidator(validator)
        self.ui.Number1.textEdited.connect(self.number1changed)
        self.ui.Number2.textEdited.connect(self.number2changed)
    def fillboxes(self):
        global measurment, measure1, measure2, currentmeasurment
        # set new information to the comboboxes
        #get new items
        print("filling")
        currentindex = self.ui.Measurments.currentIndex()
        measurment = measurments[currentindex]
        if measurment == "temperature":
            converttemper = True
        currentmeasurment = config[measurment]
        keys = list(currentmeasurment.keys())
        #clear items
        self.ui.Select1.clear()
        self.ui.Select2.clear()
        self.ui.Number1.clear()
        self.ui.Number2.clear()
        #add new items
        for key in keys:
            self.ui.Select1.addItem(key)
            self.ui.Select2.addItem(key)
        self.ui.Select1.setCurrentIndex(0)
        self.ui.Select2.setCurrentIndex(0)
        #save measures
        measure1 = self.ui.Select1.currentText()
        measure2 = self.ui.Select2.currentText()
    def setsel1(self):
        global measure1
        measure1 = self.ui.Select1.currentText()
        #print(measure1)
        if self.ui.Number1.text != "":
            self.number1changed()#self.ui.Number1, self.ui.Number2)
    def setsel2(self):
        global measure2
        #print(self.ui.Select2.currentText())
        measure2 = self.ui.Select2.currentText()     
        #print(measure2, " swx")
        if self.ui.Number2.text != "":
            self.number2changed()
    def number1changed(self):
        global measurment, measure1, measure2, templist, number1, number2
#        print("number1changed " + str(self.ui.Number1.text()))
        #print(measure1, " ", measure2, " sas")
        if (measure1 != "" or measure2 != "") and self.ui.Number1.text() != '':
            if measurment != "temperature":
                to_needed = 0
                msr1 = currentmeasurment[measure1]
                msr2 = currentmeasurment[measure2]
                number1 = float(self.ui.Number1.text())
                to_base = number1 * msr1[0]
                number2 = to_base * msr2[1]
                self.ui.Number2.setText(str(number2))
            else:
                msr1 = currentmeasurment[measure1]
                formula = msr1[templist.index(measure2)]
                number1 = self.ui.Number1.text()
                if formula != '1':
                    number2 = eval(formula.replace('n', number1))
                else:
                    number2 = number1
                self.ui.Number2.setText(str(number2))
        else:
            number2 = ""
            self.ui.Number2.setText("")
    def number2changed(self):
        global measurment, measure1, measure2, templist
#        print("number2changed " + str(self.ui.Number2.text()))
        #print(measure1, " ", measure2, " sas")
        if (measure1 != "" or measure2 != "") and self.ui.Number2.text() != '':
            if measurment != "temperature":
                to_needed = 0
                msr1 = currentmeasurment[measure1]
                msr2 = currentmeasurment[measure2]
                number2 = float(self.ui.Number2.text())
                to_base = number2 * msr1[0]
                number1 = to_base * msr2[1]
                self.ui.Number1.setText(str(number1))
            else:
                msr1 = currentmeasurment[measure2]
                formula = msr1[templist.index(measure1)]
                number2 = self.ui.Number2.text()
                if formula != '1':
                    number1 = eval(formula.replace('n', self.ui.Number2.text()))
                else:
                    number1 = number2
                self.ui.Number1.setText(str(number1))
        else: 
            number1 = ""
            self.ui.Number1.setText(number1)
app = QtWidgets.QApplication(sys.argv)
window = Converter()
window.show()
#print(window.Measurments.currentText()) 
app.exec()