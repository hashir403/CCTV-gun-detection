from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox

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
        self.pushButton_1.setStyleSheet("QPushButton#pushButton_1{background-color:white;font-size:20px;border-radius:8px;}"
                                        "QPushButton#pushButton_1:hover{background-color:#274E69;font-size:25px;border-radius:4px;color:white;}")
        self.pushButton_1.setObjectName("pushButton_1")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(381, 40, 110, 41))
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{background-color:white;font-size:20px;border-radius:8px;}"
                                        "QPushButton#pushButton_2:hover{background-color:#274E69;font-size:25px;border-radius:4px;color:white;}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(521, 40, 151, 41))
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3{background-color:#274E69;font-size:20px;border-radius:8px;}"
                                        "QPushButton#pushButton_3:hover{background-color:#274E69;font-size:25px;border-radius:4px;color:white;}")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 40, 161, 41))
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4{background-color:white;font-size:20px;border-radius:8px;}"
                                        "QPushButton#pushButton_4:hover{background-color:#274E69;font-size:25px;border-radius:4px;color:white;}")
        self.pushButton_4.setObjectName("pushButton_4")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 120, 311, 71))
        self.label_2.setStyleSheet("font-size:50px;color:white;font-weight:bold;")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 230, 91, 31))
        self.label_3.setStyleSheet("color:white;font-size:30px;")
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 300, 81, 31))
        self.label_4.setStyleSheet("color:white;font-size:30px;")
        self.label_4.setObjectName("label_4")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 390, 121, 41))
        self.label_6.setStyleSheet("color:white;font-size:30px;")
        self.label_6.setObjectName("label_6")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(420, 220, 401, 51))
        self.lineEdit_3.setStyleSheet("font-size:22px;border-radius:4px;padding:4px;color: black;")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 290, 401, 51))
        self.lineEdit_2.setStyleSheet("font-size:22px;border-radius:4px;padding:4px;color: black;")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(420, 355, 411, 111))
        self.textEdit.setStyleSheet("font-size:22px;border-radius:4px;padding:4px;color: black;")
        self.textEdit.setObjectName("textEdit")

        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(540, 520, 151, 41))
        self.submitButton.setStyleSheet("QPushButton#submitButton{background-color:white;font-size:20px;border-radius:8px;}"
                                        "QPushButton#submitButton:hover{background-color:#274E69;font-size:25px;border-radius:4px;color:white;}")
        self.submitButton.setObjectName("submitButton")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_start(self):
        from GUI_start import Ui_MainWindow as start_window
        self.MainWindow1 = QtWidgets.QMainWindow()
        self.ui = start_window()
        self.ui.setupUi(self.MainWindow1)
        self.MainWindow1.show()
        self.centralwidget.parent().close()

    def open_home(self):
        from GUI import Ui_MainWindow as home_window
        self.MainWindow2 = QtWidgets.QMainWindow()
        self.ui = home_window()
        self.ui.setupUi(self.MainWindow2)
        self.MainWindow2.show()
        self.centralwidget.parent().close()

    def open_about(self):
        from GUI_about import Ui_MainWindow as about_window
        self.MainWindow3 = QtWidgets.QMainWindow()
        self.ui = about_window()
        self.ui.setupUi(self.MainWindow3)
        self.MainWindow3.show()
        self.centralwidget.parent().close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_1.setText(_translate("MainWindow", "Home"))
        self.pushButton_2.setText(_translate("MainWindow", "About"))
        self.pushButton_3.setText(_translate("MainWindow", "Contact us"))
        self.pushButton_4.setText(_translate("MainWindow", "Get Started"))
        self.label_2.setText(_translate("MainWindow", "Contact us"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Email"))
        self.label_6.setText(_translate("MainWindow", "Message"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Enter Text"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter Your Email"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Enter Your Name"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.submitButton.clicked.connect(self.submit_data)


        self.pushButton_1.clicked.connect(self.open_home)
        self.pushButton_2.clicked.connect(self.open_about)
        self.pushButton_4.clicked.connect(self.open_start)
        
    def submit_data(self):
     name = self.lineEdit_3.text()
     email = self.lineEdit_2.text()
     message = self.textEdit.toPlainText()

     if name and email and message:
        try:
            conn = sqlite3.connect("contact_data.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)", (name, email, message))
            conn.commit()
            conn.close()
            
            QMessageBox.information(None, "Success", "Your message has been submitted!")
            print("data is send successfully")

            # Clear fields
            self.lineEdit_3.clear()
            self.lineEdit_2.clear()
            self.textEdit.clear()
        except Exception as e:
            QMessageBox.warning(None, "Error", f"Something went wrong:\n{e}")
     else:
        QMessageBox.warning(None, "Missing Info", "Please fill all fields.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
