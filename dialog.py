# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(210, 157)
        self.checkBox_0 = QCheckBox(Dialog)
        self.checkBox_0.setObjectName(u"checkBox_0")
        self.checkBox_0.setGeometry(QRect(20, 20, 79, 19))
        self.checkBox_1 = QCheckBox(Dialog)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setGeometry(QRect(20, 50, 79, 19))
        self.checkBox_2 = QCheckBox(Dialog)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(20, 80, 91, 19))
        self.checkBox_3 = QCheckBox(Dialog)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(120, 20, 79, 19))
        self.checkBox_4 = QCheckBox(Dialog)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(20, 110, 79, 19))
        self.checkBox_5 = QCheckBox(Dialog)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(120, 50, 91, 19))
        self.checkBox_6 = QCheckBox(Dialog)
        self.checkBox_6.setObjectName(u"checkBox")
        self.checkBox_6.setGeometry(QRect(120, 80, 91, 19))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u6446\u70c2\u8bbe\u7f6e", None))
        self.checkBox_0.setText(QCoreApplication.translate("Dialog", u"\u6a21\u62df\u5ba4", None))
        self.checkBox_1.setText(QCoreApplication.translate("Dialog", u"\u7ade\u6280\u573a", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"\u81ea\u52a8\u54a8\u8be2", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"\u6536\u7c73", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"\u8054\u76df\u6218", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"\u62e6\u622a\u6218", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"\u5355\u4eba\u7a81\u88ad", None))
    # retranslateUi
