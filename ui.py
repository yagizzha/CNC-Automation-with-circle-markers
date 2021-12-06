# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerKaNRKM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import svgpdot

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Input Window")
        MainWindow.resize(856, 557)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.filename1 = QLabel(self.centralwidget)
        self.filename1.setObjectName(u"filename1")
        self.filename1.setGeometry(QRect(10, 60, 141, 41))
        font = QFont()
        font.setPointSize(20)
        self.filename1.setFont(font)
        self.u_File0 = QTextEdit(self.centralwidget)
        self.u_File0.setObjectName(u"u_File0")
        self.u_File0.setGeometry(QRect(10, 110, 261, 41))
        self.u_File1 = QTextEdit(self.centralwidget)
        self.u_File1.setObjectName(u"u_File1")
        self.u_File1.setGeometry(QRect(320, 110, 261, 41))
        self.filename1_2 = QLabel(self.centralwidget)
        self.filename1_2.setObjectName(u"filename1_2")
        self.filename1_2.setGeometry(QRect(320, 60, 141, 41))
        self.filename1_2.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 551, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.u_Height = QTextEdit(self.centralwidget)
        self.u_Height.setObjectName(u"u_Height")
        self.u_Height.setGeometry(QRect(10, 220, 261, 41))
        self.filename1_3 = QLabel(self.centralwidget)
        self.filename1_3.setObjectName(u"filename1_3")
        self.filename1_3.setGeometry(QRect(10, 170, 251, 41))
        self.filename1_3.setFont(font)
        self.u_Length = QTextEdit(self.centralwidget)
        self.u_Length.setObjectName(u"u_Length")
        self.u_Length.setGeometry(QRect(320, 220, 261, 41))
        self.filename1_4 = QLabel(self.centralwidget)
        self.filename1_4.setObjectName(u"filename1_4")
        self.filename1_4.setGeometry(QRect(320, 170, 251, 41))
        self.filename1_4.setFont(font)
        self.filename1_5 = QLabel(self.centralwidget)
        self.filename1_5.setObjectName(u"filename1_5")
        self.filename1_5.setGeometry(QRect(610, 170, 221, 41))
        self.filename1_5.setFont(font)
        self.u_PerBox = QTextEdit(self.centralwidget)
        self.u_PerBox.setObjectName(u"u_PerBox")
        self.u_PerBox.setGeometry(QRect(610, 220, 221, 41))
        self.u_OffsetY = QTextEdit(self.centralwidget)
        self.u_OffsetY.setObjectName(u"u_OffsetY")
        self.u_OffsetY.setGeometry(QRect(10, 320, 261, 41))
        self.u_OffsetY2 = QLabel(self.centralwidget)
        self.u_OffsetY2.setObjectName(u"u_OffsetY2")
        self.u_OffsetY2.setGeometry(QRect(10, 270, 251, 41))
        self.u_OffsetY2.setFont(font)
        self.u_OffsetX = QTextEdit(self.centralwidget)
        self.u_OffsetX.setObjectName(u"u_OffsetX")
        self.u_OffsetX.setGeometry(QRect(320, 320, 261, 41))
        self.u_OffsetY_2 = QLabel(self.centralwidget)
        self.u_OffsetY_2.setObjectName(u"u_OffsetY_2")
        self.u_OffsetY_2.setGeometry(QRect(320, 270, 251, 41))
        self.u_OffsetY_2.setFont(font)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(610, 400, 221, 81))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 856, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.filename1.setText(QCoreApplication.translate("MainWindow", u"Filename0", None))
        self.filename1_2.setText(QCoreApplication.translate("MainWindow", u"Filename1 ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter names of your files , they must be jpg format \n"
"For File0.jpg , input should be File0 only", None))
        self.filename1_3.setText(QCoreApplication.translate("MainWindow", u"Height in boxes", None))
        self.filename1_4.setText(QCoreApplication.translate("MainWindow", u"Length in boxes", None))
        self.filename1_5.setText(QCoreApplication.translate("MainWindow", u"Box length in mm", None))
        self.u_OffsetY2.setText(QCoreApplication.translate("MainWindow", u"Missing box Y axis", None))
        self.u_OffsetY_2.setText(QCoreApplication.translate("MainWindow", u"Missing box Y axis", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi
def tester(ex,w):
    File0=-15
    File1=-15
    Height=-15
    Length=-15
    OffsetX=-15
    OffsetY=-15
    PerBox=-15
    
    if (ex.u_File0.toPlainText()== ""):
        File0=-15
    else:
        File0=ex.u_File0.toPlainText()


    if (ex.u_File1.toPlainText()== ""):
        File1=-15
    else:
        File1=ex.u_File1.toPlainText()


    if (ex.u_Height.toPlainText()== ""):
        Height=-15
    else:
        Height=ex.u_Height.toPlainText()


    if (ex.u_Length.toPlainText()== ""):
        Length=-15
    else:
        Length=ex.u_Length.toPlainText()


    if (ex.u_OffsetX.toPlainText()== ""):
        OffsetX=-15
    else:
        OffsetX=ex.u_OffsetX.toPlainText()


    if (ex.u_OffsetY.toPlainText()== ""):
        OffsetY=-15
    else:
        OffsetY=ex.u_OffsetY.toPlainText()


    if (ex.u_PerBox.toPlainText()== ""):
        PerBox=-15
    else:
        PerBox=ex.u_PerBox.toPlainText()
    svgpdot.dotfinder(File0,File1,Height,Length,OffsetX,OffsetY,PerBox)
    w.close()
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QMainWindow()
    ex.setupUi(w)
    w.show()
    ex.pushButton.clicked.connect(lambda: tester(ex,w))
    sys.exit(app.exec_())

