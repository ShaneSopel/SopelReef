# Developed by Shane Sopel
# Sopel Reef Gui Main Window

from PyQt5 import QtCore, QtGui, QtWidgets
from TempWindow import Ui_TempWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        MainWindow.setStyleSheet("background-color: rgb(56, 182, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #
        # Sopel Reef Label
        #
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 0, 141, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/Sopel Reef.png"))
        self.label.setObjectName("label")

        #
        # Temp Button
        #
        self.tempButton = QtWidgets.QPushButton(self.centralwidget)
        self.tempButton.setGeometry(QtCore.QRect(0, 160, 101, 101))
        self.tempButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.7 rgba(56, 182, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 10px;")
        self.tempButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/temp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tempButton.setIcon(icon)
        self.tempButton.setIconSize(QtCore.QSize(80, 80))
        self.tempButton.setObjectName("tempButton")
        self.tempButton.clicked.connect(self.TempButtonPush)
        
        #
        # PH Button
        #
        self.phButton = QtWidgets.QPushButton(self.centralwidget)
        self.phButton.setGeometry(QtCore.QRect(120, 160, 101, 101))
        self.phButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.7 rgba(56, 182, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 10px;")
        self.phButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/ph_.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.phButton.setIcon(icon1)
        self.phButton.setIconSize(QtCore.QSize(80, 80))
        self.phButton.setObjectName("phButton")
        #self.phButton.clicked.connect(self.addButtonPush)
        
        #
        # Health Stat Button
        #
        self.healthstatButton = QtWidgets.QPushButton(self.centralwidget)
        self.healthstatButton.setGeometry(QtCore.QRect(240, 160, 101, 101))
        self.healthstatButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.7 rgba(56, 182, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 10px;")
        self.healthstatButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/healthstatus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.healthstatButton.setIcon(icon2)
        self.healthstatButton.setIconSize(QtCore.QSize(80, 80))
        self.healthstatButton.setObjectName("healthstatButton")
        #self.healthstatButton.clicked.connect(self.addButtonPush)

        #
        # LED Button
        #
        self.ledButton = QtWidgets.QPushButton(self.centralwidget)
        self.ledButton.setGeometry(QtCore.QRect(360, 160, 101, 101))
        self.ledButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.7 rgba(56, 182, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border: 1px solid grey;\n"
"border-radius: 10px;")
        self.ledButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/lightbulb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ledButton.setIcon(icon3)
        self.ledButton.setIconSize(QtCore.QSize(80, 80))
        self.ledButton.setObjectName("ledButton")
        #self.ledButton.clicked.connect(self.addButtonPush)

        #
        # Menu
        #
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
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
    # TempButtonPushed 
    #
    def TempButtonPush(self):
        #self.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TempWindow()
        self.ui.setupUi(self.window)
        self.window.show()

#
# main loop
#
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())


