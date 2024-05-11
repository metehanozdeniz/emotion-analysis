# -*- coding: utf-8 -*-

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1010, 600)
        MainWindow.setMinimumSize(QSize(1010, 600))
        MainWindow.setMaximumSize(QSize(1010, 600))
        MainWindow.setStyleSheet(u"background-color: rgb(31, 31, 31);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

       # Circular Progress Bar Angry 
        self.circularProgressBar_Main = QFrame(self.centralwidget)
        self.circularProgressBar_Main.setObjectName(u"circularProgressBar_Main")
        self.circularProgressBar_Main.setGeometry(QRect(10, 80, 240, 240))
        self.circularProgressBar_Main.setStyleSheet(u"background-color: none;")
        self.circularProgressBar_Main.setFrameShape(QFrame.NoFrame)
        self.circularProgressBar_Main.setFrameShadow(QFrame.Raised)
        self.circularProgressAngry = QFrame(self.circularProgressBar_Main)
        self.circularProgressAngry.setObjectName(u"circularProgressAngry")
        self.circularProgressAngry.setGeometry(QRect(10, 10, 220, 220))
        self.circularProgressAngry.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.0 rgba(255, 0, 127, 255), stop:0.0 rgba(255, 255, 255, 0));\n"
"}")
        self.circularProgressAngry.setFrameShape(QFrame.StyledPanel)
        self.circularProgressAngry.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.circularProgressBar_Main)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(10, 10, 220, 220))
        self.circularBg.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: rgba(18, 18, 18, 100);\n"
"}")
        self.circularBg.setFrameShape(QFrame.StyledPanel)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.circularContainer = QFrame(self.circularProgressBar_Main)
        self.circularContainer.setObjectName(u"circularContainer")
        self.circularContainer.setGeometry(QRect(25, 25, 190, 190))
        self.circularContainer.setBaseSize(QSize(0, 0))
        self.circularContainer.setStyleSheet(u"QFrame{\n"
"	border-radius: 95px;	\n"
"	background-color: rgb(45, 45, 45);\n"
"}")
        self.circularContainer.setFrameShape(QFrame.StyledPanel)
        self.circularContainer.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.circularContainer)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 171, 125))
        self.infoLayout = QGridLayout(self.layoutWidget)
        self.infoLayout.setObjectName(u"infoLayout")
        self.infoLayout.setContentsMargins(0, 0, 0, 0)
        self.labelAplicationName = QLabel(self.layoutWidget)
        self.labelAplicationName.setObjectName(u"labelAplicationName")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        self.labelAplicationName.setFont(font)
        self.labelAplicationName.setStyleSheet(u"color: #FFFFFF; background-color: none;")
        self.labelAplicationName.setAlignment(Qt.AlignCenter)

        self.infoLayout.addWidget(self.labelAplicationName, 0, 0, 1, 1)

        self.labelPercentageAngry = QLabel(self.layoutWidget)
        self.labelPercentageAngry.setObjectName(u"labelPercentageAngry")
        font1 = QFont()
        font1.setFamily(u"Roboto Thin")
        font1.setPointSize(30)
        self.labelPercentageAngry.setFont(font1)
        self.labelPercentageAngry.setStyleSheet(u"color: rgb(255, 0, 127); padding: 0px; background-color: none;")
        self.labelPercentageAngry.setAlignment(Qt.AlignCenter)
        self.labelPercentageAngry.setIndent(-1)

        self.infoLayout.addWidget(self.labelPercentageAngry, 1, 0, 1, 1)

        self.circularBg.raise_()
        self.circularProgressAngry.raise_()
        self.circularContainer.raise_()

        # Circular Progress Bar Fear
        self.circularProgressBar_Main_2 = QFrame(self.centralwidget)
        self.circularProgressBar_Main_2.setObjectName(u"circularProgressBar_Main_2")
        self.circularProgressBar_Main_2.setGeometry(QRect(260, 80, 240, 240))
        self.circularProgressBar_Main_2.setStyleSheet(u"background-color: none;")
        self.circularProgressBar_Main_2.setFrameShape(QFrame.NoFrame)
        self.circularProgressBar_Main_2.setFrameShadow(QFrame.Raised)
        self.circularProgressFear = QFrame(self.circularProgressBar_Main_2)
        self.circularProgressFear.setObjectName(u"circularProgressFear")
        self.circularProgressFear.setGeometry(QRect(10, 10, 220, 220))
        self.circularProgressFear.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.0 rgba(255, 243, 53, 255), stop:0.0 rgba(255, 255, 255, 0));\n"
"}")
        self.circularProgressFear.setFrameShape(QFrame.StyledPanel)
        self.circularProgressFear.setFrameShadow(QFrame.Raised)
        self.circularBg_2 = QFrame(self.circularProgressBar_Main_2)
        self.circularBg_2.setObjectName(u"circularBg_2")
        self.circularBg_2.setGeometry(QRect(10, 10, 220, 220))
        self.circularBg_2.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: rgba(18, 18, 18, 100);\n"
"}")
        self.circularBg_2.setFrameShape(QFrame.StyledPanel)
        self.circularBg_2.setFrameShadow(QFrame.Raised)
        self.circularContainer_2 = QFrame(self.circularProgressBar_Main_2)
        self.circularContainer_2.setObjectName(u"circularContainer_2")
        self.circularContainer_2.setGeometry(QRect(25, 25, 190, 190))
        self.circularContainer_2.setBaseSize(QSize(0, 0))
        self.circularContainer_2.setStyleSheet(u"QFrame{\n"
"	border-radius: 95px;	\n"
"	background-color: rgb(45, 45, 45);\n"
"}")
        self.circularContainer_2.setFrameShape(QFrame.StyledPanel)
        self.circularContainer_2.setFrameShadow(QFrame.Raised)
        self.layoutWidget_2 = QWidget(self.circularContainer_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 40, 171, 127))
        self.infoLayout_2 = QGridLayout(self.layoutWidget_2)
        self.infoLayout_2.setObjectName(u"infoLayout_2")
        self.infoLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelAplicationName_2 = QLabel(self.layoutWidget_2)
        self.labelAplicationName_2.setObjectName(u"labelAplicationName_2")
        self.labelAplicationName_2.setFont(font)
        self.labelAplicationName_2.setStyleSheet(u"color: #FFFFFF; background-color: none;")
        self.labelAplicationName_2.setAlignment(Qt.AlignCenter)

        self.infoLayout_2.addWidget(self.labelAplicationName_2, 0, 0, 1, 1)

        self.labelPercentageFear = QLabel(self.layoutWidget_2)
        self.labelPercentageFear.setObjectName(u"labelPercentageFear")
        self.labelPercentageFear.setFont(font1)
        self.labelPercentageFear.setStyleSheet(u"color: rgb(255, 243, 53); padding: 0px; background-color: none;")
        self.labelPercentageFear.setAlignment(Qt.AlignCenter)
        self.labelPercentageFear.setIndent(-1)

        self.infoLayout_2.addWidget(self.labelPercentageFear, 1, 0, 1, 1)

        self.circularBg_2.raise_()
        self.circularProgressFear.raise_()
        self.circularContainer_2.raise_()

        # Circular Progress Bar Happy
        self.circularProgressBar_Main_3 = QFrame(self.centralwidget)
        self.circularProgressBar_Main_3.setObjectName(u"circularProgressBar_Main_3")
        self.circularProgressBar_Main_3.setGeometry(QRect(510, 80, 240, 240))
        self.circularProgressBar_Main_3.setStyleSheet(u"background-color: none;")
        self.circularProgressBar_Main_3.setFrameShape(QFrame.NoFrame)
        self.circularProgressBar_Main_3.setFrameShadow(QFrame.Raised)
        self.circularProgressHappy = QFrame(self.circularProgressBar_Main_3)
        self.circularProgressHappy.setObjectName(u"circularProgressHappy")
        self.circularProgressHappy.setGeometry(QRect(10, 10, 220, 220))
        self.circularProgressHappy.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.0 rgba(85, 255, 127, 255), stop:0.0 rgba(255, 255, 255, 0));\n"
"}")
        self.circularProgressHappy.setFrameShape(QFrame.StyledPanel)
        self.circularProgressHappy.setFrameShadow(QFrame.Raised)
        self.circularBg_3 = QFrame(self.circularProgressBar_Main_3)
        self.circularBg_3.setObjectName(u"circularBg_3")
        self.circularBg_3.setGeometry(QRect(10, 10, 220, 220))
        self.circularBg_3.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: rgba(18, 18, 18, 100);\n"
"}")
        self.circularBg_3.setFrameShape(QFrame.StyledPanel)
        self.circularBg_3.setFrameShadow(QFrame.Raised)
        self.circularContainer_3 = QFrame(self.circularProgressBar_Main_3)
        self.circularContainer_3.setObjectName(u"circularContainer_3")
        self.circularContainer_3.setGeometry(QRect(25, 25, 190, 190))
        self.circularContainer_3.setBaseSize(QSize(0, 0))
        self.circularContainer_3.setStyleSheet(u"QFrame{\n"
"	border-radius: 95px;	\n"
"	background-color: rgb(45, 45, 45);\n"
"}")
        self.circularContainer_3.setFrameShape(QFrame.StyledPanel)
        self.circularContainer_3.setFrameShadow(QFrame.Raised)
        self.layoutWidget_3 = QWidget(self.circularContainer_3)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 40, 171, 125))
        self.infoLayout_3 = QGridLayout(self.layoutWidget_3)
        self.infoLayout_3.setObjectName(u"infoLayout_3")
        self.infoLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelAplicationName_3 = QLabel(self.layoutWidget_3)
        self.labelAplicationName_3.setObjectName(u"labelAplicationName_3")
        self.labelAplicationName_3.setFont(font)
        self.labelAplicationName_3.setStyleSheet(u"color: #FFFFFF; background-color: none;")
        self.labelAplicationName_3.setAlignment(Qt.AlignCenter)

        self.infoLayout_3.addWidget(self.labelAplicationName_3, 0, 0, 1, 1)

        self.labelPercentageHappy = QLabel(self.layoutWidget_3)
        self.labelPercentageHappy.setObjectName(u"labelPercentageHappy")
        self.labelPercentageHappy.setFont(font1)
        self.labelPercentageHappy.setStyleSheet(u"color: rgb(85, 255, 127); padding: 0px; background-color: none;")
        self.labelPercentageHappy.setAlignment(Qt.AlignCenter)
        self.labelPercentageHappy.setIndent(-1)

        self.infoLayout_3.addWidget(self.labelPercentageHappy, 1, 0, 1, 1)

        self.circularBg_3.raise_()
        self.circularProgressHappy.raise_()
        self.circularContainer_3.raise_()


       # Circular Progress Bar Sad
        self.circularProgressBar_Main_4 = QFrame(self.centralwidget)
        self.circularProgressBar_Main_4.setObjectName(u"circularProgressBar_Main_4")
        self.circularProgressBar_Main_4.setGeometry(QRect(760, 80, 240, 240))
        self.circularProgressBar_Main_4.setStyleSheet(u"background-color: none;")
        self.circularProgressBar_Main_4.setFrameShape(QFrame.NoFrame)
        self.circularProgressBar_Main_4.setFrameShadow(QFrame.Raised)
        self.circularProgressSad = QFrame(self.circularProgressBar_Main_4)
        self.circularProgressSad.setObjectName(u"circularProgressSad")
        self.circularProgressSad.setGeometry(QRect(10, 10, 220, 220))
        self.circularProgressSad.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.0 rgba(85, 170, 255, 255), stop:0.0 rgba(255, 255, 255, 0));\n"
"}")
        self.circularProgressSad.setFrameShape(QFrame.StyledPanel)
        self.circularProgressSad.setFrameShadow(QFrame.Raised)
        self.circularBg_4 = QFrame(self.circularProgressBar_Main_4)
        self.circularBg_4.setObjectName(u"circularBg_4")
        self.circularBg_4.setGeometry(QRect(10, 10, 220, 220))
        self.circularBg_4.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: rgba(18, 18, 18, 100);\n"
"}")
        self.circularBg_4.setFrameShape(QFrame.StyledPanel)
        self.circularBg_4.setFrameShadow(QFrame.Raised)
        self.circularContainer_4 = QFrame(self.circularProgressBar_Main_4)
        self.circularContainer_4.setObjectName(u"circularContainer_4")
        self.circularContainer_4.setGeometry(QRect(25, 25, 190, 190))
        self.circularContainer_4.setBaseSize(QSize(0, 0))
        self.circularContainer_4.setStyleSheet(u"QFrame{\n"
"	border-radius: 95px;	\n"
"	background-color: rgb(45, 45, 45);\n"
"}")
        self.circularContainer_4.setFrameShape(QFrame.StyledPanel)
        self.circularContainer_4.setFrameShadow(QFrame.Raised)
        self.layoutWidget_4 = QWidget(self.circularContainer_4)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 40, 171, 125))
        self.infoLayout_4 = QGridLayout(self.layoutWidget_4)
        self.infoLayout_4.setObjectName(u"infoLayout_4")
        self.infoLayout_4.setContentsMargins(0, 0, 0, 0)
        self.labelAplicationName_4 = QLabel(self.layoutWidget_4)
        self.labelAplicationName_4.setObjectName(u"labelAplicationName_4")
        self.labelAplicationName_4.setFont(font)
        self.labelAplicationName_4.setStyleSheet(u"color: #FFFFFF; background-color: none;")
        self.labelAplicationName_4.setAlignment(Qt.AlignCenter)

        self.infoLayout_4.addWidget(self.labelAplicationName_4, 0, 0, 1, 1)

        self.labelPercentageSad = QLabel(self.layoutWidget_4)
        self.labelPercentageSad.setObjectName(u"labelPercentageSad")
        self.labelPercentageSad.setFont(font1)
        self.labelPercentageSad.setStyleSheet(u"color: rgb(85, 170, 255); padding: 0px; background-color: none;")
        self.labelPercentageSad.setAlignment(Qt.AlignCenter)
        self.labelPercentageSad.setIndent(-1)

        self.infoLayout_4.addWidget(self.labelPercentageSad, 1, 0, 1, 1)

        self.circularBg_4.raise_()
        self.circularProgressSad.raise_()
        self.circularContainer_4.raise_()

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(210, 540, 580, 40))
        self.label_13.setMaximumSize(QSize(600, 40))
        font4 = QFont()
        font4.setFamily(u"Roboto Light")
        font4.setPointSize(14)
        self.label_13.setFont(font4)
        self.label_13.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(73, 61, 87);\n"
"border-radius: 20px;")
        self.label_13.setAlignment(Qt.AlignCenter)

        # label
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 340, 70, 18))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Metin:", None))

        # textEdit
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setPlaceholderText("Metin giriniz...")
        self.textEdit.setGeometry(200, 370, 600, 90)
        self.textEdit.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.textEdit.setFont(font4)

       # pushButton
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(420, 480, 160, 40)) 
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(58, 45, 73);\n"
"    border-radius: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(73, 61, 87);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(81, 69, 94);\n"
"}")
        self.pushButton.setFont(font4)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"OK", None))


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)


    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Emotion Analysis", None))
        self.labelAplicationName.setText(QCoreApplication.translate("MainWindow", u"ÖFKE", None))
        self.labelPercentageAngry.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:50pt;\">0</span><span style=\" font-size:40pt; vertical-align:super;\">%</span></p>", None))
        self.labelAplicationName_2.setText(QCoreApplication.translate("MainWindow", u"KORKU", None))
        self.labelPercentageFear.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:50pt;\">0</span><span style=\" font-size:40pt; vertical-align:super;\">%</span></p>", None))
        self.labelAplicationName_3.setText(QCoreApplication.translate("MainWindow", u"MUTLU", None))
        self.labelPercentageHappy.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:50pt;\">0</span><span style=\" font-size:40pt; vertical-align:super;\">%</span></p>", None))
        self.labelAplicationName_4.setText(QCoreApplication.translate("MainWindow", u"ÜZGÜN", None))
        self.labelPercentageSad.setText(QCoreApplication.translate("MainWindow", u"<p align=\"center\"><span style=\" font-size:50pt;\">0</span><span style=\" font-size:40pt; vertical-align:super;\">%</span></p>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_13.setVisible(False)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Metin:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"OK", None))
