import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 200, 300, 300)

        # 1. QCheckBox
        #self.cbox = QCheckBox("미수", self)
        #self.cbox.move(10, 10)
        #self.cbox.stateChanged.connect(self.slot)
        
        # 2. QSpinBox
        #self.spinbox = QSpinBox(self)
        #self.spinbox.move(10, 10)
        #self.spinbox.valueChanged.connect(self.spinbox_value_changed)

        #3 QTableWidget
        #self.tableWidget = QTableWidget(self)
        #self.tableWidget.resize(290,290)
        #self.tableWidget.verticalHeader().setVisible(False)
        #self.tableWidget.setColumnCount(2)
        #self.tableWidget.setRowCount(3)
        #labels = ["종목명", "종목코드"]
        #self.tableWidget.setHorizontalHeaderLabels(labels)
        #self.tableWidget.setItem(0, 0, QTableWidgetItem("삼성전자"))
        #self.tableWidget.setItem(0, 1, QTableWidgetItem("005930"))
        #self.tableWidget.setItem(1, 0, QTableWidgetItem("SK하이닉스"))
        #self.tableWidget.setItem(1, 1, QTableWidgetItem("000660"))
        #self.tableWidget.setItem(2, 0, QTableWidgetItem("Naver"))
        #self.tableWidget.setItem(2, 1, QTableWidgetItem("035420"))

        # 4. slider
        #self.slider = QSlider(Qt.Horizontal, self)
        #self.slider.setRange(0, 100)
        #self.slider.move(10,10)
        #self.slider.valueChanged.connect(self.slider_value_changed)

        # 5. combo box
        self.combo = QComboBox(self)
        self.combo.resize(200, 30)
        self.combo.move(10, 10)

        self.combo.addItem("보통")
        self.combo.addItem("시장가")
        self.combo.addItem("조건부 지정가")
        self.combo.currentTextChanged.connect(self.slot)
    #def slot(self, state):
    #    if state == Qt.Checked:
    #        print("미수")
    #    else:
    #        print("보통")

    #def spinbox_value_changed(self):
    #    value = self.spinbox.value()
    #    print(value)

    #def slider_value_changed(self):
    #    value = self.slider.value()
    #    print(value)

    def slot(self, text):
        print(text)
#if __name__ == "__main__":
app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()