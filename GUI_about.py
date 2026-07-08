from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1079, 592)
        MainWindow.setMinimumSize(QtCore.QSize(1079, 592))
        MainWindow.setMaximumSize(QtCore.QSize(1079, 592))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1081, 591))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("about_contact.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(251, 40, 101, 41))
        self.pushButton_1.setStyleSheet("QPushButton#pushButton_1{\n"
"background-color:white;\n"
"font-size:20px;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton#pushButton_1:hover{\n"
"background-color:#274E69;\n"
"font-size:25px;\n"
"border-radius:4px;\n"
"color:white;}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(381, 40, 110, 41))
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"background-color:#274E69;\n"
"font-size:20px;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"background-color:#274E69;\n"
"font-size:25px;\n"
"border-radius:4px;\n"
"color:white;}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(521, 40, 151, 41))
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3{\n"
"background-color:white;\n"
"font-size:20px;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton#pushButton_3:hover{\n"
"background-color:#274E69;\n"
"font-size:25px;\n"
"border-radius:4px;\n"
"color:white;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 40, 161, 41))
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4{\n"
"background-color:white;\n"
"font-size:20px;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton#pushButton_4:hover{\n"
"background-color:#274E69;\n"
"font-size:25px;\n"
"border-radius:4px;\n"
"color:white;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 100, 161, 71))
        self.label_2.setStyleSheet("font-size:50px;\n"
"color:white;\n"
"font-weight:bold;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 200, 501, 171))
        self.label_3.setStyleSheet("color:white;\n"
"font-size:20px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 410, 281, 16))
        self.label_4.setStyleSheet("color:white;\n"
"font-size:18px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 480, 281, 16))
        self.label_5.setStyleSheet("color:white;\n"
"font-size:18px;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 540, 281, 16))
        self.label_6.setStyleSheet("color:white;\n"
"font-size:18px")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(580, 410, 281, 16))
        self.label_7.setStyleSheet("color:white;\n"
"font-size:18px;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(580, 480, 281, 16))
        self.label_8.setStyleSheet("color:white;\n"
"font-size:18px;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(580, 540, 281, 16))
        self.label_9.setStyleSheet("color:white;\n"
"font-size:18px;")
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def open_start(self):
        print('get start')
        from GUI_start import Ui_MainWindow as start_window
        self.MainWindow1 = QtWidgets.QMainWindow() 
        self.ui = start_window()
        self.ui.setupUi(self.MainWindow1)
        self.MainWindow1.show()
        self.centralwidget.parent().close()  
    def open_contact(self):
        from GUI_contact import Ui_MainWindow as contact_window
        self.MainWindow2 = QtWidgets.QMainWindow()
        self.ui = contact_window()
        self.ui.setupUi(self.MainWindow2)
        self.MainWindow2.show()
        self.centralwidget.parent().close()
     
    def get_started(self): 
            print("get started")      
        
    def open_home(self):
        from GUI import Ui_MainWindow as home_window
        self.MainWindow3 = QtWidgets.QMainWindow()
        self.ui = home_window()
        self.ui.setupUi(self.MainWindow3)
        self.MainWindow3.show()
        self.centralwidget.parent().close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_1.setText(_translate("MainWindow", "Home"))
        self.pushButton_1.clicked.connect(self.open_home)
        self.pushButton_3.clicked.connect(self.open_contact)
        self.pushButton_4.clicked.connect(self.open_start)
        self.pushButton_2.setText(_translate("MainWindow", "About"))
        self.pushButton_3.setText(_translate("MainWindow", "Contact us"))
        self.pushButton_4.setText(_translate("MainWindow", "Get Started"))
        
        
        self.label_2.setText(_translate("MainWindow", "About"))
        self.label_3.setText(_translate("MainWindow", "Closed-circuit television (CCTV) \n"
"uses cameras to transmit signals to specific monitors, \n"
"typically for surveillance in secure or monitored areas. \n"
"Unlike broadcast TV, CCTV signals are not openly \n"
"transmitted and may use wired, wireless, or mesh \n"
"links. It is commonly used for security,\n"
"not videotelephony."))
        self.label_4.setText(_translate("MainWindow", "Hashir"))
        self.label_7.setText(_translate("MainWindow", "123456789"))

                 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
