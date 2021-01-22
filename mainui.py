# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maingui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(425, 284)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 311, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("LMU_WilliamHHannonLibrary_LeftAligned_RGB-CrimsonBlue.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 50, 311, 41))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 140, 361, 41))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 110, 361, 23))
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 190, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(220, 190, 171, 31))
        self.startButton.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 425, 21))
        self.menubar.setObjectName("menubar")
        self.menuLogin = QtWidgets.QMenu(self.menubar)
        self.menuLogin.setObjectName("menuLogin")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.menuLogin.addAction(self.actionLogin)
        self.menubar.addAction(self.menuLogin.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OCLC Control Number Validation Service"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">OCLC Control Number Validaton Service</span></p></body></html>"))
        self.menuLogin.setTitle(_translate("MainWindow", "Authentication"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
