# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auto_script.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSlider, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(391, 505)
        font = QFont()
        font.setFamilies([u"Adobe Arabic"])
        font.setPointSize(9)
        Form.setFont(font)
        icon = QIcon()
        icon.addFile(u"./icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.pushButton1 = QPushButton(Form)
        self.pushButton1.setObjectName(u"pushButton1")
        self.pushButton1.setGeometry(QRect(40, 60, 101, 51))
        font1 = QFont()
        font1.setFamilies([u"Adobe Arabic"])
        self.pushButton1.setFont(font1)
        self.pushButton2 = QPushButton(Form)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setGeometry(QRect(40, 150, 101, 51))
        self.pushButton2.setFont(font1)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 10, 141, 31))
        font2 = QFont()
        font2.setFamilies([u"Adobe Arabic"])
        font2.setPointSize(15)
        font2.setBold(False)
        self.label.setFont(font2)
        self.pushButton3 = QPushButton(Form)
        self.pushButton3.setObjectName(u"pushButton3")
        self.pushButton3.setGeometry(QRect(40, 240, 101, 51))
        self.pushButton3.setFont(font1)
        self.stopButton = QPushButton(Form)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(270, 440, 101, 51))
        self.stopButton.setFont(font1)
        self.pushButton4 = QPushButton(Form)
        self.pushButton4.setObjectName(u"pushButton4")
        self.pushButton4.setGeometry(QRect(40, 330, 101, 51))
        self.pushButton4.setFont(font1)
        self.pushButton4.setCursor(QCursor(Qt.ArrowCursor))
        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(40, 470, 101, 16))
        self.horizontalSlider.setMinimum(4)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setValue(8)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 440, 101, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton1.setText(QCoreApplication.translate("Form", u"\u6536\u7c73", None))
        self.pushButton2.setText(QCoreApplication.translate("Form", u"\u53cb\u60c5\u70b9", None))
        self.label.setText("")
        self.pushButton3.setText(QCoreApplication.translate("Form", u"\u6a21\u62df\u5ba4", None))
        self.stopButton.setText(QCoreApplication.translate("Form", u"\u7ec8\u6b62\u4efb\u52a1", None))
        self.pushButton4.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u54a8\u8be2", None))
        self.label_2.setText("")
    # retranslateUi

