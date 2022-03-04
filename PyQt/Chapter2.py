import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # label
        #self.label = QLabel("메시지: ",self)
        #self.label.move(10,10)
        label = QLabel()
        label.setPixmap(QPixmap("eagle16.png"))
        self.setCentralWidget(label)
        # button
        self.btn = QPushButton("click", self)
        self.btn.move(10, 40)
        #self.btn.resize(100, 100)   # 사이즈 변경
        #self.btn.setEnabled(True)   # 활성화
        #self.btn.setDisabled(True)  # 비활성화
        self.btn.clicked.connect(self.btn_clicked)
    
    def btn_clicked(self):
        self.label.clear()                  # 지우기
        self.label.setText("버튼 클릭")     # 텍스트 출력
        

app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()