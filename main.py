from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import serial

class Ui_MainWindow(object):
    data = []
    counter = 3
    _translate = QtCore.QCoreApplication.translate

    def setData(self):
        ser = serial.Serial('COM3', baudrate = 9600)
        self.data = str(ser.readline()).replace("b'", '').replace("\\r\\n'", '').split(";")
        self.compareDatas()

    def updateData(self):
        t = threading.Timer(3, self.setData)
        t.start()

    def compareDatas(self):
        p1 = self.data[0]
        p2 = self.data[1]

        if(p1 == '10'):
            p1 = '01'
            
        if(p2 == '10'):
            p2 = '01'
            
        if(p1 == '00'):
            self.value_1.setPixmap(QtGui.QPixmap("imgs/rock.png"))
        if(p1 == '01'):
            self.value_1.setPixmap(QtGui.QPixmap("imgs/paper.png"))
        if(p1 == '11'):
            self.value_1.setPixmap(QtGui.QPixmap("imgs/scissors.png"))

        if(p2 == '00'):
            self.value_2.setPixmap(QtGui.QPixmap("imgs/rock.png"))
        if(p2 == '01'):
            self.value_2.setPixmap(QtGui.QPixmap("imgs/paper.png"))
        if(p2 == '11'):
            self.value_2.setPixmap(QtGui.QPixmap("imgs/scissors.png"))    
            
        if(p1 == p2):
            self.status.setText(self._translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ff5067;\">DRAW</span></p></body></html>"))

        elif(p1 == '00'):
            if(p2 == '11'):
                self.status.setText(self._translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ff5067;\">PLAYER 1 WON</span></p></body></html>"))
            elif(p2 == '01'):
                self.status.setText(self._translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ff5067;\">PLAYER 2 WON</span></p></body></html>"))
        elif(p1 == '01'):
            if(p2 == '00'):
                self.status.setText(self._translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ff5067;\">PLAYER 1 WON</span></p></body></html>"))
            if(p2 == '11'):
                self.status.setText(self._translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ff5067;\">PLAYER 2 WON</span></p></body></html>"))
        elif(p1 == '11'):
            if(p2 == '01'):
                self.status.setText(self._translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ff5067;\">PLAYER 1 WON</span></p></body></html>"))
            if(p2 == '00'):
                self.status.setText(self._translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ff5067;\">PLAYER 2 WON</span></p></body></html>"))
            
    def count(self):
        if(self.counter == 3):
            self.secs.setText(self._translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">03</span></p></body></html>"))
            self.counter = self.counter - 1
            return
        if(self.counter == 2):
            self.secs.setText(self._translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">02</span></p></body></html>"))
            self.counter = self.counter - 1
            return
        if(self.counter == 1):
            self.secs.setText(self._translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">01</span></p></body></html>"))
            self.counter = self.counter - 1
            return
            return
        if (self.counter == 0):
            self.secs.setText(self._translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">00</span></p></body></html>"))
            self.counter = 3
            return

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 758)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.value_1 = QtWidgets.QLabel(self.centralwidget)
        self.value_1.setGeometry(QtCore.QRect(190, 230, 255, 357))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.value_1.setFont(font)
        self.value_1.setText("")
        self.value_1.setPixmap(QtGui.QPixmap("imgs/p1.png"))
        self.value_1.setScaledContents(True)
        self.value_1.setObjectName("value_1")
        self.HEADER = QtWidgets.QLabel(self.centralwidget)
        self.HEADER.setGeometry(QtCore.QRect(0, 60, 1054, 61))
        font = QtGui.QFont()
        font.setFamily("Righteous")
        font.setPointSize(24)
        self.HEADER.setFont(font)
        self.HEADER.setAlignment(QtCore.Qt.AlignCenter)
        self.HEADER.setObjectName("HEADER")
        self.value_2 = QtWidgets.QLabel(self.centralwidget)
        self.value_2.setGeometry(QtCore.QRect(610, 230, 255, 357))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.value_2.setFont(font)
        self.value_2.setText("")
        self.value_2.setPixmap(QtGui.QPixmap("imgs/p2.png"))
        self.value_2.setScaledContents(True)
        self.value_2.setObjectName("value_2")
        self.player_1 = QtWidgets.QLabel(self.centralwidget)
        self.player_1.setGeometry(QtCore.QRect(270, 213, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Righteous")
        font.setPointSize(18)
        self.player_1.setFont(font)
        self.player_1.setObjectName("player_1")
        self.player_2 = QtWidgets.QLabel(self.centralwidget)
        self.player_2.setGeometry(QtCore.QRect(690, 210, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Righteous")
        font.setPointSize(18)
        self.player_2.setFont(font)
        self.player_2.setObjectName("player_2")
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(0, 130, 1051, 31))
        font = QtGui.QFont()
        font.setFamily("Righteous")
        font.setPointSize(18)
        self.time.setFont(font)
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time")
        self.secs = QtWidgets.QLabel(self.centralwidget)
        self.secs.setGeometry(QtCore.QRect(0, 160, 1051, 31))
        font = QtGui.QFont()
        font.setFamily("Righteous")
        font.setPointSize(16)
        self.secs.setFont(font)
        self.secs.setAlignment(QtCore.Qt.AlignCenter)
        self.secs.setObjectName("secs")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, -60, 1051, 821))
        self.bg.setStyleSheet("background-image: url(:/newPrefix/imgs/bg.png);")
        self.bg.setObjectName("bg")
        self.start = QtWidgets.QToolButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(480, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Righteous")
        font.setPointSize(16)
        self.start.setFont(font)
        self.start.setAutoFillBackground(False)
        self.start.setStyleSheet("color: rgb(255, 255, 255);\n"
"background: rgb(195,45,253);")
        self.start.setObjectName("start")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 450, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Righteous")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(380, 490, 300, 31))
        font = QtGui.QFont()
        font.setFamily("Righteous")
        self.status.setFont(font)
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        self.bg.raise_()
        self.value_1.raise_()
        self.HEADER.raise_()
        self.value_2.raise_()
        self.player_1.raise_()
        self.player_2.raise_()
        self.time.raise_()
        self.secs.raise_()
        self.start.raise_()
        self.label.raise_()
        self.status.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.start.clicked.connect(self.play)

    def retranslateUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self._translate("MainWindow", "MainWindow"))
        self.HEADER.setText(self._translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">ROCK  PAPER  SCISSORS</span></p></body></html>"))
        self.player_1.setText(self._translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">PLAYER 1</span></p></body></html>"))
        self.player_2.setText(self._translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">PLAYER 2</span></p></body></html>"))
        self.time.setText(self._translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">TIME</span></p></body></html>"))
        self.secs.setText(self._translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\"></span></p></body></html>"))
        self.bg.setText(self._translate("MainWindow", "TextLabel"))
        self.start.setToolTip(self._translate("MainWindow", "<html><head/><body><p></p></body></html>"))
        self.start.setWhatsThis(self._translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.start.setText(self._translate("MainWindow", "START"))
        self.label.setText(self._translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">STATUS</span></p></body></html>"))
        self.status.setText(self._translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ff5067;\">...</span></p></body></html>"))
    
    def play(self):
        # non-blocking thread code
        class ThreadJob(threading.Thread):
            def __init__(self, callback, event, interval):
                self.callback = callback
                self.event = event
                self.interval = interval
                super(ThreadJob, self).__init__()

            def run(self):
                while not self.event.wait(self.interval):
                    self.callback()

        event = threading.Event()
        # non-blocking thread code

        k = ThreadJob(self.count, event, 1)
        k.start()
        
        self.updateData()

import bg_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
