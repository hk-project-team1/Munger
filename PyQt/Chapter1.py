import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#app = QApplication(sys.argv)

#버튼 만들기
#button = QPushButton("Button")
#button.show()

# 라벨 만들기
#label = QLabel("Label")
#label.show()

# 윈도우 만들기
#class MyWindow(QMainWindow):
#    def __init__(self):
#        super().__init__()
#        self.setWindowTitle("My HTS v1.0")
# super()의 의미
# 부모클래스를 의미한다. QMainWindow 클래스를 상속받는데, 생성자에서 부모클래스인 QMainWindow의 생성자를 호출해줘야한다.


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Munger HTS v.10 by MS")
        self.setGeometry(300, 300, 400, 400)
        # 아이콘 넣을 때, root부터 넣기 아래처럼 c로 시작하게끔
        self.setWindowIcon(QIcon('c:/Workspace/Munger/PyQt/eagle16.png'))
        btn1 = QPushButton(text="매수", parent=self)
        btn1.move(10, 10)
        btn1.clicked.connect(self.buy)

        btn2 = QPushButton(text="Quit", parent=self)
        btn2.move(10,50)
        btn2.clicked.connect(self.btn_clicked)
    
    def buy(self):
        print("몽땅 매수")

    def btn_clicked(self):
        QApplication.instance().quit()

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
