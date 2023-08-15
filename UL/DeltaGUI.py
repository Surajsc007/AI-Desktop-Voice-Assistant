

from PyQt5 import QtCore, QtGui, QtWidgets


class UI_Delta(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 600)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.speaking = QtWidgets.QLabel(Form)
        self.speaking.setGeometry(QtCore.QRect(250, 90, 501, 450))
        self.speaking.setStyleSheet("border-radius:250px;\n"
"background: transparent;\n"
"border-image: url(../../../Downloads/GUI files-20230410T095706Z-001/GUI files/speak.gif);")
        self.speaking.setText("")
        self.speaking.setScaledContents(True)
        self.speaking.setObjectName("speaking")
        self.listening = QtWidgets.QLabel(Form)
        self.listening.setGeometry(QtCore.QRect(300, 90, 401, 451))
        self.listening.setStyleSheet("border-radius:250px;\n"
"background: transparent;\n"
"border-image: url(../../../Downloads/GUI files-20230410T095706Z-001/GUI files/listen.gif);")
        self.listening.setText("")
        self.listening.setScaledContents(False)
        self.listening.setObjectName("listening")
        self.loading = QtWidgets.QLabel(Form)
        self.loading.setGeometry(QtCore.QRect(300, 90, 421, 391))
        self.loading.setStyleSheet("border-radius:250px;\n"
"background: transparent;\n"
"border-image: url(../../../Downloads/GUI files-20230410T095706Z-001/GUI files/tech loading-cropped.gif);")
        self.loading.setScaledContents(True)
        self.loading.setObjectName("loading")
        self.loading_2 = QtWidgets.QLabel(Form)
        self.loading_2.setGeometry(QtCore.QRect(300, 90, 421, 391))
        self.loading_2.setStyleSheet("border-radius:250px;\n"
"background: transparent;\n")
        self.loading_2.setScaledContents(True)
        self.loading_2.setObjectName("loading_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 10, 671, 81))
        self.label.setStyleSheet("border-image: url(../../../Downloads/GUI files-20230410T095706Z-001/GUI files/KartisTechnology(white).png);\n"
"background: transparent;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(830, 500, 151, 61))
        self.pushButton.setStyleSheet("border-image: url(../../../Downloads/GUI files-20230410T095706Z-001/GUI files/exit(with border).png);\n"
"background: transparent;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "DELTA"))
        self.loading.setText(_translate("Form", "TextLabel"))
        self.loading_2.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = UI_Delta()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
