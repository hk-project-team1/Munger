import sys
from types import DynamicClassAttribute 
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
import pythoncom

class Kiwoom:
    def __init__(self):
        self.login = False
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self.OnEventConnect)
        self.ocx.OnReceiveTrData.connect(self.OnReceiveTrDate)

    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")
        while not self.login:
            pythoncom.PumpWaitingMessages()
    
    def OnReceiveTrDate(self, screen, rqname, trcode, record, next):
        print(screen, rqname, trcode, record, next)
        per = self.GetCommData(trcode, rqname, 0, "PER")
        pbr = self.GetCommData(trcode, rqname, 0, "PBR")
        print(per, pbr)
    
    def GetMasterCodeName(self, code):
        name = self.ocx.dynamicCall("GetMasterCodeName(QString)", code)
        return name
    
    def OnEventConnect(self, err_code):
        self.login = True
    
    def SetInputValue(self, id, value):
        self.ocx.dynamicCall("SetInputValue(QString, QString)", id, value)
    
    def CommRqData(self, trcode, next, screen):
        self.ocx.dynamicCall("CommRqData(Qstring, Qstring, int, Qstring)", rqname, trcode, next, screen)
    
    def GetCommData(self, trcode, rqname, index, item):
        data = self.ocx.dynamicCall("GetCommData(Qstring, QString, int, Qstring)", trcode, rqname, index, item)

class MungerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.kiwoom = Kiwoom()
        self.kiwoom.CommConnect()

        # tr request
        self.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MungerWindow()
    window.show()
    app.exec_()