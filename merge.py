from PyQt5 import QtCore, QtGui, QtWidgets

# First GUI
class Ui_FirstWindow(object):
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
        self.label.setPixmap(QtGui.QPixmap("edited.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(251, 40, 101, 41))
        self.pushButton_1.setStyleSheet("QPushButton#pushButton_1{\n"
                                        "background-color:#274E69;\n"
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
                                        "background-color:white;\n"
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the Contact Us button to open the second window
        self.pushButton_3.clicked.connect(self.open_second_window)

    def open_second_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        MainWindow.close()  # Close the first window
        self.window.show()  # Show the second window

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_1.setText(_translate("MainWindow", "Home"))
        self.pushButton_2.setText(_translate("MainWindow", "About"))
        self.pushButton_3.setText(_translate("MainWindow", "Contact us"))
        self.pushButton_4.setText(_translate("MainWindow", "Get Started"))


# Second Contact us 
class Ui_SecondWindow(object):
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

        # Buttons
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
                                        "background-color:white;\n"
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
                                        "background-color:#274E69;\n"
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

        # Labels and Inputs
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 120, 311, 71))
        self.label_2.setStyleSheet("font-size:50px;\n"
                                   "color:white;\n"
                                   "font-weight:bold;")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 230, 91, 31))
        self.label_3.setStyleSheet("color:white;\n"
                                   "font-size:30px;")
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 300, 81, 31))
        self.label_4.setStyleSheet("color:white;\n"
                                   "font-size:30px;")
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 360, 111, 41))
        self.label_5.setStyleSheet("color:white;\n"
                                   "font-size:30px;")
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 450, 121, 41))
        self.label_6.setStyleSheet("color:white;\n"
                                   "font-size:30px;")
        self.label_6.setObjectName("label_6")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(420, 460, 411, 111))
        self.textEdit.setStyleSheet("font-size:22px;\n"
                                    "border-radius:4px;\n"
                                    "padding:4px;\n"
                                    "color: black;")
        self.textEdit.setObjectName("textEdit")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(420, 360, 401, 51))
        self.lineEdit.setStyleSheet("font-size:22px;\n"
                                    "border-radius:4px;\n"
                                    "padding:4px;\n"
                                    "color: black;")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 290, 401, 51))
        self.lineEdit_2.setStyleSheet("font-size:22px;\n"
                                      "border-radius:4px;\n"
                                      "padding:4px;\n"
                                      "color: black;")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(420, 220, 401, 51))
        self.lineEdit_3.setStyleSheet("font-size:22px;\n"
                                      "border-radius:4px;\n"
                                      "padding:4px;\n"
                                      "color: black;")
        self.lineEdit_3.setObjectName("lineEdit_3")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Contact Us"))
        self.pushButton_1.setText(_translate("MainWindow", "Home"))
        self.pushButton_2.setText(_translate("MainWindow", "About"))
        self.pushButton_3.setText(_translate("MainWindow", "Contact us"))
        self.pushButton_4.setText(_translate("MainWindow", "Get Started"))
        self.label_2.setText(_translate("MainWindow", "Contact us"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Email"))
        self.label_5.setText(_translate("MainWindow", "Subject"))
        self.label_6.setText(_translate("MainWindow", "Message"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Enter Text"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Your Subject"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter Your Email"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Enter Your Name"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_FirstWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
