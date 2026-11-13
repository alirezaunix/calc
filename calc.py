from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base,sessionmaker

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("calc.ui", self)
        
        styleFile=open("/Users/alireza/Desktop/prj2/style.qss")
        styleText=styleFile.read()
        self.setStyleSheet(styleText)
        styleFile.close()
        
        self.b_1.clicked.connect(lambda : self.textEnter("1"))
        self.b_2.clicked.connect(lambda : self.textEnter("2"))
        self.b_3.clicked.connect(lambda : self.textEnter("3"))
        self.b_4.clicked.connect(lambda : self.textEnter("4"))
        self.b_5.clicked.connect(lambda : self.textEnter("5"))
        self.b_6.clicked.connect(lambda : self.textEnter("6"))
        self.b_7.clicked.connect(lambda : self.textEnter("7"))
        self.b_8.clicked.connect(lambda : self.textEnter("8"))
        self.b_9.clicked.connect(lambda : self.textEnter("9"))
        self.b_dot.clicked.connect(lambda : self.textEnter("."))
        
        self.b_a.clicked.connect(lambda : self.textEnter("+"))
        self.b_m.clicked.connect(lambda : self.textEnter("-"))
        self.b_z.clicked.connect(lambda : self.textEnter("*"))
        self.b_d.clicked.connect(lambda : self.textEnter("/"))
        
        self.b_e.setObjectName("b_e")
        self.b_e.clicked.connect(self.eq)
        
        self.b_ac.clicked.connect(self.ac)
        
        self.b_back.clicked.connect(self.back)
        
        

    def textEnter(self,c):
        self.lcd.setText(self.lcd.text()+c)
    
    def eq(self):
        self.lcd.setText(str(eval(self.lcd.text())))
    
    def ac(self):
        self.lcd.setText("")
        
    def back(self):
        self.lcd.setText(self.lcd.text()[:-1])
    
app = QtWidgets.QApplication([])
w = MainWindow()
w.show()
app.exec()