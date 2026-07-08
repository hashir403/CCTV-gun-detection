
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import time
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
        self.label.setPixmap(QtGui.QPixmap("start.png"))
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
"background-color:#274E69;\n"
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
        self.label_2.setGeometry(QtCore.QRect(450, 350, 191, 101))
        self.label_2.setStyleSheet("color:white;\n"
"font-size:30px;\n"
"border-radius:8px;\n"
"")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def open_home(self):
        from GUI import Ui_MainWindow as home_window
        self.MainWindow1 = QtWidgets.QMainWindow() 
        self.ui = home_window()
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
        
    def open_about(self):
        from GUI_about import Ui_MainWindow as about_window
        self.MainWindow3 = QtWidgets.QMainWindow()
        self.ui = about_window()
        self.ui.setupUi(self.MainWindow3)
        self.MainWindow3.show()
        self.centralwidget.parent().close()
    
    def camera_open_action(self):
        self.label_2.setText(QtCore.QCoreApplication.translate("MainWindow", "Camera Open"))    
    def new_button_clicked(self):
        print('Please wait Now Camera is opening')
        os.system('python Gun_prediction_code.py')
        time.sleep(5)
        os.system('python send__all_details_images_video.py')
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_1.setText(_translate("MainWindow", "Home"))
        self.pushButton_1.clicked.connect(self.open_home)
        self.pushButton_2.clicked.connect(self.open_about)
        self.pushButton_3.clicked.connect(self.open_contact)
        self.pushButton_2.setText(_translate("MainWindow", "About"))
        self.pushButton_3.setText(_translate("MainWindow", "Contact us"))
        self.pushButton_4.setText(_translate("MainWindow", "Get Started"))
        # self.label_2.setText(_translate("MainWindow", "Camera Open1"))
        self.pushButton_camera = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_camera.setText("Camera Open1")
        self.pushButton_camera.clicked.connect(self.camera_open_action)
        # Create a new QPushButton
        self.newPushButton = QtWidgets.QPushButton(MainWindow)
        self.newPushButton.setGeometry(QtCore.QRect(470, 400, 150, 40))  # Adjust the position and size
        self.newPushButton.setObjectName("newPushButton")
        self.newPushButton.setText(_translate("MainWindow", "Camera Open"))

        # Connect the new button to a function
        self.newPushButton.clicked.connect(self.new_button_clicked)
         
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
