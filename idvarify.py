from PyQt5 import QtCore, QtGui, QtWidgets


class ID_MainWindow(object):
    def iduisetup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(426, 267)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 201, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("mk-worldshare-lf-th.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 60, 231, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 110, 81, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 110, 161, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 140, 81, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 140, 161, 20))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pButton = QtWidgets.QPushButton(self.centralwidget)
        self.pButton.setGeometry(QtCore.QRect(190, 180, 111, 31))
        self.pButton.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Indentity Varification</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Username:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Password:</span></p></body></html>"))
        self.pButton.setText(_translate("MainWindow", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ID_MainWindow()
    ui.iduisetup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
