import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # label
        #self.label = QLabel("메시지: ",self)
        #self.label.move(10,10)
        

        # 1. 이미지 출력 Qpixmap
        #self.label = QLabel()
        #self.label.setPixmap(QPixmap("eagle16.png"))
        #self.setCentralWidget(self.label)

        # 2. button
        #self.btn = QPushButton("click", self)
        #self.btn.move(10, 40)
        #self.btn.resize(100, 100)   # 사이즈 변경
        #self.btn.setEnabled(True)   # 활성화
        #self.btn.setDisabled(True)  # 비활성화
        #self.btn.clicked.connect(self.btn_clicked)

        # 3. 사용자로 부터 간단한 입력을 받을 때 사용, QLineEdit
        #self.line_edit = QLineEdit(" ", self)
        #self.line_edit.move(10,10)
        #self.line_edit.setEnabled(False)
        #self.line_edit.setText("Hello")
        #self.line_edit.textChanged.connect(self.text_changed)   # 텍스트 입력이 변경될 때

        # 4. 윈도우 하단에 간단한 메시지를 출력할 때 사용하는 위젯
        #self.statusbar = QStatusBar(self)       # QStatusBar 객체 생성
        #self.setStatusBar(self.statusbar)       # 위젯 배치
        #self.statusbar.showMessage("PYSTOCK v1.0")

        # 5. QCheckBox
        self.setGeometry(300, 300, 400, 300)

        self.cbox = QCheckBox("미수", self)
        self.cbox.move(10,10)
    
    
    #def text_changed(self):
    #    text = self.line_edit.text()                # QLineEdit 위젯에 입력된 텍스트 가져오기
    #    print(text)
    #def btn_clicked(self):
    #    self.label.clear()                  # 지우기
    #    self.label.setText("버튼 클릭")     # 텍스트 출력
        

app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()