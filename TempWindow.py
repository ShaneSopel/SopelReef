# Developed by Shane Sopel
# Sopel Reef Gui Temp Window

from PyQt5 import QtCore, QtGui, QtWidgets
#from MainWindow import Ui_MainWindow

class Ui_TempWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        MainWindow.setStyleSheet("background-color: rgb(56, 182, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #
        # Home Button
        #
        self.HomeButton = QtWidgets.QPushButton(self.centralwidget)
        self.HomeButton.setGeometry(QtCore.QRect(360, 160, 101, 101))
        self.HomeButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.7 rgba(56, 182, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 10px;")
        self.HomeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HomeButton.setIcon(icon)
        self.HomeButton.setIconSize(QtCore.QSize(80, 80))
        self.HomeButton.setObjectName("HomeButton")
        self.HomeButton.clicked.connect(self.HomeButtonPush)

        #
        # Menu
        #
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
    #
    # HomeButtonPushed 
    #
    def HomeButtonPush(self):
        #self.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window1)
        self.window1.show()


