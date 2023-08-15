import sys
from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QProcess, QCoreApplication
from PyQt5 import QtGui
from UL import mainLog
import os 
import sys
from pyautogui import click
import speech_recognition as sr
import pyttsx3
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
000
def speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

class loginFile(QWidget):

    
    def __init__(self):
        super(loginFile, self).__init__()
        self.LoginUI = mainLog.Ui_Login()
        self.LoginUI.setupUi(self)
        
        self.LoginUI.invalidMovie = QtGui.QMovie("C:\\Users\\SURAJ\\OneDrive\\Desktop\\Main GUI\\gif\\password.gif")
        self.LoginUI.label_2.setMovie(self.LoginUI.invalidMovie)

        self.LoginUI.label_2.hide()
        self.LoginUI.pushButton_4.clicked.connect(self.validateLogin)
        self.LoginUI.password_edit.setEchoMode(QLineEdit.Password)
        self.LoginUI.pushButton_3.clicked.connect(self.close)
        self.LoginUI.pushButton.clicked.connect(self.retryBtn)
        
        
    def validateLogin(self):
        username = self.LoginUI.username_edit.text()
        password = self.LoginUI.password_edit.text()
        if username == 'Surajsc007' and password == 'sur123':
            # os.system('python DeltaMain.py')
            process = QProcess(self)
            process.start("python", ["DeltaMain.py"])
            click(x=1217, y=165)
            process.finished.connect(QCoreApplication.quit)


            
        else:
            self.startMovie()
            
            
    def retryBtn(self):
        self.LoginUI.username_edit.clear()
        self.LoginUI.password_edit.clear()
        self.stopMovie()
    
    def startMovie(self):
        self.LoginUI.label_2.show()
        self.LoginUI.invalidMovie.start()
        
    def stopMovie(self):
        self.LoginUI.invalidMovie.stop()
        self.LoginUI.label_2.hide()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ui = loginFile()
    ui.show()
    sys.exit(app.exec_())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# import sys
# from PyQt5.QtWidgets import QWidget, QLineEdit
# from PyQt5.QtWidgets import QApplication
# from PyQt5 import QtGui
# from mainLog import Ui_Login
# import os 
# import pyautogui


# class loginFile(QWidget):
#     def __init__(self):
#         super(loginFile, self).__init__()
#         self.LoginUI = Ui_Login()
#         self.LoginUI.setupUi(self)
        
#         self.LoginUI.invalidMovie = QtGui.QMovie("C:\\Users\\SURAJ\\OneDrive\\Desktop\\Main GUI\\gif\\password.gif")
#         self.LoginUI.label_2.setMovie(self.LoginUI.invalidMovie)

#         self.LoginUI.label_2.hide()
#         self.LoginUI.pushButton_4.clicked.connect(self.validateLogin)
#         self.LoginUI.password_edit.setEchoMode(QLineEdit.Password)
#         self.LoginUI.pushButton_3.clicked.connect(self.close)
#         self.LoginUI.pushButton.clicked.connect(self.retryBtn)
        
#     def validateLogin(self):
#         username = self.LoginUI.username_edit.text()
#         password = self.LoginUI.password_edit.text()
#         if username == 'Surajsc007' and password == 'sur123':
#             os.system('python main.py')
            
#         else:
#             self.startMovie()
            
#     def retryBtn(self):
#         self.LoginUI.username_edit.clear()
#         self.LoginUI.password_edit.clear()
#         self.stopMovie()
    
#     def startMovie(self):
#         self.LoginUI.label_2.show()
#         self.LoginUI.invalidMovie.start()
        
#     def stopMovie(self):
#         self.LoginUI.invalidMovie.stop()
#         self.LoginUI.label_2.hide()
        
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ui = loginFile()
#     ui.show()
#     sys.exit(app.exec_())

