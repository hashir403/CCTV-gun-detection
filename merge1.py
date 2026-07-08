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
        self.pushButton_3.clicked.connect(lambda: self.open_second_window(MainWindow))

    def open_second_window(self, current_window):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window, current_window)  # Pass the reference of the first window
        current_window.close()  # Close the first window
        self.window.show()  # Show the second window

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_1.setText(_translate("MainWindow", "Home"))
        self.pushButton_2.setText(_translate("MainWindow", "About"))
        self.pushButton_3.setText(_translate("MainWindow", "Contact us"))
        self.pushButton_4.setText(_translate("MainWindow", "Get Started"))


# Second GUI (Contact Us)
class Ui_SecondWindow(object):
    def setupUi(self, MainWindow, first_window):
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

        # Connect "Home" button to navigate back to the first window
        self.pushButton_1.clicked.connect(lambda: self.open_first_window(MainWindow, first_window))

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_first_window(self, current_window, first_window):
        current_window.close()  # Close the current window
        first_window.show()  # Reopen the first window

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Contact Us"))
        self.pushButton_1.setText(_translate("MainWindow", "Home"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_FirstWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())





# self.pushButton_3.clicked.connect(lambda: self.open_second_window(MainWindow))
