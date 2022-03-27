import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sqlite3

from numpy import real

form_class = uic.loadUiType("C:/Workspace/Munger/KiwoomAPI/indextest.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableWidget.setHorizontalHeaderLabels(["Name","Last"])
        self.tableWidget_2.setColumnWidth(1,150)
        
        # Text Label
        self.label.setText("Index")
        
        # Combo box
        self.comboBox.addItems(["KosdaqLowPBR", "KosdaqLowPCR","KosdaqLowPSR","KosdaqLowPER","KosdaqROE","KospiLowPBR","KospiLowPCR","KospiLowPSR","KospiLowPER","KospiROE"])
        self.comboBox.currentTextChanged.connect(self.combobox_changed)
        
        
        # tableWidget 첫번째 테이블 위젯에 인덱스지표 삽입 함수
        self.loaddata()
        
        # tableWidget2 두번째 테이블 위젯에 다양한 데이터들 삽입

    def combobox_changed(self, item):
        self.loaddata2(item)

    def loaddata(self):
        con = sqlite3.connect("c:/Users/hkedu/Munger.db")
        cur  = con.cursor()
        sqlquery = "SELECT * From 'index' LIMIT 12"
        
        self.tableWidget.setRowCount(12)
        tablerow = 0
        
        for row in cur.execute(sqlquery):
            self.tableWidget.setItem(tablerow, 0, QTableWidgetItem(row[1]))
            a = QTableWidgetItem(str(row[2]))
            self.tableWidget.setItem(tablerow, 1, a)
            tablerow += 1

    def loaddata2(self, item): 
        con = sqlite3.connect("c:/Users/hkedu/Munger.db")  
        cur = con.cursor()
        sqlquery = f"SELECT * From {item} LIMIT 200"
        self.tableWidget_2.setRowCount(200)
        tablerow = 0
        for row in cur.execute(sqlquery):
            self.tableWidget_2.setItem(tablerow, 0, QTableWidgetItem(row[1]))
            a = QTableWidgetItem(str(row[2]))
            self.tableWidget_2.setItem(tablerow, 1, a)
            tablerow += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()