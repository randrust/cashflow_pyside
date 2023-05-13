# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_periodgGFYpn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogP(object):
    def setupUi(self, DialogP):
        if not DialogP.objectName():
            DialogP.setObjectName(u"DialogP")
        DialogP.resize(181, 216)
        DialogP.setLocale(QLocale(QLocale.Ukrainian, QLocale.Ukraine))
        self.label = QLabel(DialogP)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(13, 13, 142, 19))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.line = QFrame(DialogP)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(7, 140, 161, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(DialogP)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 40, 151, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.layoutWidget = QWidget(DialogP)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 60, 133, 33))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.dateEditFrom = QDateEdit(self.layoutWidget)
        self.dateEditFrom.setObjectName(u"dateEditFrom")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.dateEditFrom.setFont(font1)
        self.dateEditFrom.setCalendarPopup(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dateEditFrom)

        self.layoutWidget1 = QWidget(DialogP)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 110, 133, 31))
        self.formLayout_2 = QFormLayout(self.layoutWidget1)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.dateEditTo = QDateEdit(self.layoutWidget1)
        self.dateEditTo.setObjectName(u"dateEditTo")
        self.dateEditTo.setFont(font1)
        self.dateEditTo.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateEditTo.setCalendarPopup(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.dateEditTo)

        self.layoutWidget2 = QWidget(DialogP)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 170, 158, 26))
        self.formLayout_3 = QFormLayout(self.layoutWidget2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnOk = QPushButton(self.layoutWidget2)
        self.btnOk.setObjectName(u"btnOk")
        self.btnOk.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.btnOk)

        self.btnCancel = QPushButton(self.layoutWidget2)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.btnCancel)


        self.retranslateUi(DialogP)

        QMetaObject.connectSlotsByName(DialogP)
    # setupUi

    def retranslateUi(self, DialogP):
        DialogP.setWindowTitle(QCoreApplication.translate("DialogP", u"NEW", None))
        self.label.setText(QCoreApplication.translate("DialogP", u"\u041d\u043e\u0432\u0438\u0439 \u043f\u0435\u0440\u0435\u043e\u0431\u043b\u0456\u043a", None))
        self.label_2.setText(QCoreApplication.translate("DialogP", u"\u0412\u0456\u0434", None))
        self.dateEditFrom.setDisplayFormat(QCoreApplication.translate("DialogP", u"yyyy-MM-dd", None))
        self.label_3.setText(QCoreApplication.translate("DialogP", u"\u0414\u043e ", None))
        self.dateEditTo.setDisplayFormat(QCoreApplication.translate("DialogP", u"yyyy-MM-dd", None))
        self.btnOk.setText(QCoreApplication.translate("DialogP", u"\u0414\u043e\u0434\u0430\u0442\u0438", None))
        self.btnCancel.setText(QCoreApplication.translate("DialogP", u"\u0412\u0456\u0434\u043c\u0456\u043d\u0430", None))
    # retranslateUi

