# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_periodebOTgv.ui'
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
        DialogP.resize(217, 242)
        DialogP.setLocale(QLocale(QLocale.Ukrainian, QLocale.Ukraine))
        self.gridLayout_2 = QGridLayout(DialogP)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(DialogP)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.line_2 = QFrame(DialogP)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(DialogP)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.dateEditFrom = QDateEdit(DialogP)
        self.dateEditFrom.setObjectName(u"dateEditFrom")
        self.dateEditFrom.setFont(font)
        self.dateEditFrom.setCalendarPopup(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dateEditFrom)


        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_3 = QLabel(DialogP)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.dateEditTo = QDateEdit(DialogP)
        self.dateEditTo.setObjectName(u"dateEditTo")
        self.dateEditTo.setFont(font)
        self.dateEditTo.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateEditTo.setCalendarPopup(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.dateEditTo)


        self.gridLayout.addLayout(self.formLayout_2, 3, 0, 1, 1)

        self.line = QFrame(DialogP)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 4, 0, 1, 1)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.btnOk = QPushButton(DialogP)
        self.btnOk.setObjectName(u"btnOk")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.btnOk.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.btnOk)

        self.btnCancel = QPushButton(DialogP)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.btnCancel)


        self.gridLayout.addLayout(self.formLayout_3, 5, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


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
        self.btnOk.setText(QCoreApplication.translate("DialogP", u"\u0414\u041e\u0414\u0410\u0422\u0418", None))
        self.btnCancel.setText(QCoreApplication.translate("DialogP", u"\u0412\u0406\u0414\u041c\u0406\u041d\u0410", None))
    # retranslateUi

