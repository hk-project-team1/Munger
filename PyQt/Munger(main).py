import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTime, Qt, QDateTime, QDate

class Munger(QMainWindow):
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()
        widget=QWidget()
        layout = QVBoxLayout(widget)
        self.setCentralWidget(widget)

    def initUI(self):
        # 제목
        self.setWindowTitle('Munger version-0.1')
        
        # 아이콘
        self.setWindowIcon(QIcon('c:/workspace/Munger/PyQt/Owlicon.png'))
        self.setGeometry(300, 300, 300, 200)
        
        # 밑에 statusBar 날짜 창
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))  # 날짜표시
        
        # 메뉴바
        exitAction = QAction(QIcon('c:/workspace/Munger/PyQt/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        
        # 창크기
        self.resize(1000, 750)
        self.center()
        
        # 라벨박스
        self.lbl = QLabel('저PER모음', self)
        self.lbl.move(550,20)
        
        # 콤보 박스
        self.combo = QComboBox(self)
        self.combo.resize(300,30)
        self.combo.move(10,300)
        self.combo.addItem('저PER모음')
        self.combo.addItem('저PBR모음')
        self.combo.addItem('저PSR모음')
        self.combo.addItem('저PCR모음')
        # self.cb.currentTextChanged.connect(self.onActivated)
        self.combo.currentTextChanged.connect(self.onActivated)
        
        # QLabel(여러가지 경제지표)
        # Dollar Index (where)
        label1 = QLabel('Dollar Index: ', self)   # 텍스트에 함수넣어서 제시
        label1.setAlignment(Qt.AlignCenter)
        label1.move(10, 20)
        
        # U.S. 10Y
        label2 = QLabel('U.S. 10Y:', self)   # 텍스트에 함수넣어서 제시
        label2.setAlignment(Qt.AlignCenter)
        label2.move(10, 40)
        # U.S. 2Y
        label3 = QLabel('U.S. 2Y:', self)   # 텍스트에 함수넣어서 제시
        label3.setAlignment(Qt.AlignCenter)
        label3.move(10, 60)
        # Crude Oil WTI 
        label4 = QLabel('Crude Oil WTI:', self)   # 텍스트에 함수넣어서 제시
        label4.setAlignment(Qt.AlignCenter)
        label4.move(110, 20)
        # Gold
        label5 = QLabel('Gold: ', self)   # 텍스트에 함수넣어서 제시
        label5.setAlignment(Qt.AlignCenter)
        label5.move(110, 40)
        # S&P VIX
        label6 = QLabel('S&P VIX:', self)   # 텍스트에 함수넣어서 제시
        label6.setAlignment(Qt.AlignCenter)
        label6.move(110, 60)
        # S&P500
        label7 = QLabel('S&P500:', self)   # 텍스트에 함수넣어서 제시
        label7.setAlignment(Qt.AlignCenter)
        label7.move(210, 20)
        # Nasdaq
        label8 = QLabel('Nasdaq:', self)   # 텍스트에 함수넣어서 제시
        label8.setAlignment(Qt.AlignCenter)
        label8.move(210, 40)
        # Rusell2000
        label9 = QLabel('Rusell2000:', self)   # 텍스트에 함수넣어서 제시
        label9.setAlignment(Qt.AlignCenter)
        label9.move(210, 60)
        # Bitcoin
        label10 = QLabel('Bitcoin:', self)   # 텍스트에 함수넣어서 제시
        label10.setAlignment(Qt.AlignCenter)
        label10.move(310, 20)
        # Ethereum
        label11 = QLabel('Ethereum:', self)   # 텍스트에 함수넣어서 제시
        label11.setAlignment(Qt.AlignCenter)
        label11.move(310, 40)
        # KOSPI
        label12 = QLabel('KOSPI:', self)   # 텍스트에 함수넣어서 제시
        label12.setAlignment(Qt.AlignCenter)
        label12.move(310, 60)
        font1 = label1.font()
        font1.setPointSize(20)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def onActivated(self, text):
        print(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Munger()
    sys.exit(app.exec_())