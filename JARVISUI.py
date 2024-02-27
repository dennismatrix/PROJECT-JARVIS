# from pyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets

class ui_jarvisUi(object):
    def setupUi(self, jarvisUi):
        jarvisUi.setObjectName("jarvisUi")
        jarvisUi.resize(1059, 666)
        self.centralWidget = QtWidgets.QTabWidget(jarvisUi)
        self.centralWidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1061, 671))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("path to iron.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(840, 620, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QPushButton(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10,401,91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("path to initial.gif"))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(590, 20, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)    
        font.setBold(True)
        font.setWeight(75) 
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background:transparent;\n"
 "*border-radius:none;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(810, 20, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"boarder-radius:none;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        jarvisUi.setCentralWidget(self.centralWidget)



        self.retranslateUi(jarvisUi)
        QtCore.QMetaObject.connectSlotsByName(jarvisUi)


        def retranslateUi(self, jarvisUi):
            _translate = QtCore.QCoreApplication.translate
            jarvisUi.setWindowTitle(_translate("jarvisUi", "MainWindow"))
            self.pushButton.setText(_translate("jarvisUi", "Run"))
            self.pushButton_2.setText(_translate("jarvisUi", "Exit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jarvisUi = QtWidgets.QMainWindow()
    ui = ui_jarvisUi()
    ui.setupUi(jarvisUi)
    jarvisUi.show()
    sys.exit(app.exec_())
    


        


