# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_updateZQJGSI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(281, 364)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 247, 339))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.dateEdit = QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setFont(font)
        self.dateEdit.setMaximumDateTime(QDateTime(QDate(9999, 12, 31), QTime(23, 59, 59)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setDate(QDate(2023, 4, 1))

        self.horizontalLayout_4.addWidget(self.dateEdit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.widget = QWidget(self.layoutWidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lc1000 = QLabel(self.widget)
        self.lc1000.setObjectName(u"lc1000")
        self.lc1000.setFont(font)
        self.lc1000.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lc1000)

        self.lc500 = QLabel(self.widget)
        self.lc500.setObjectName(u"lc500")
        self.lc500.setFont(font)
        self.lc500.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lc500)

        self.lc200 = QLabel(self.widget)
        self.lc200.setObjectName(u"lc200")
        self.lc200.setFont(font)
        self.lc200.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lc200)

        self.lc100 = QLabel(self.widget)
        self.lc100.setObjectName(u"lc100")
        self.lc100.setFont(font)
        self.lc100.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lc100)

        self.lc50 = QLabel(self.widget)
        self.lc50.setObjectName(u"lc50")
        self.lc50.setFont(font)
        self.lc50.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lc50)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sc1000 = QSpinBox(self.widget)
        self.sc1000.setObjectName(u"sc1000")
        self.sc1000.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sc1000.setProperty("showGroupSeparator", True)
        self.sc1000.setMaximum(1000)
        self.sc1000.setSingleStep(0)

        self.verticalLayout_2.addWidget(self.sc1000)

        self.sc500 = QSpinBox(self.widget)
        self.sc500.setObjectName(u"sc500")
        self.sc500.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sc500.setProperty("showGroupSeparator", True)
        self.sc500.setMaximum(1000)
        self.sc500.setSingleStep(0)

        self.verticalLayout_2.addWidget(self.sc500)

        self.sc200 = QSpinBox(self.widget)
        self.sc200.setObjectName(u"sc200")
        self.sc200.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sc200.setProperty("showGroupSeparator", True)
        self.sc200.setMaximum(1000)
        self.sc200.setSingleStep(0)

        self.verticalLayout_2.addWidget(self.sc200)

        self.sc100 = QSpinBox(self.widget)
        self.sc100.setObjectName(u"sc100")
        self.sc100.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sc100.setProperty("showGroupSeparator", True)
        self.sc100.setMaximum(1000)
        self.sc100.setSingleStep(0)

        self.verticalLayout_2.addWidget(self.sc100)

        self.sc50 = QSpinBox(self.widget)
        self.sc50.setObjectName(u"sc50")
        self.sc50.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sc50.setProperty("showGroupSeparator", True)
        self.sc50.setMaximum(1000)
        self.sc50.setSingleStep(0)

        self.verticalLayout_2.addWidget(self.sc50)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.e1000 = QLabel(self.widget)
        self.e1000.setObjectName(u"e1000")
        self.e1000.setFont(font)

        self.verticalLayout_3.addWidget(self.e1000)

        self.e500 = QLabel(self.widget)
        self.e500.setObjectName(u"e500")
        self.e500.setFont(font)

        self.verticalLayout_3.addWidget(self.e500)

        self.e200 = QLabel(self.widget)
        self.e200.setObjectName(u"e200")
        self.e200.setFont(font)

        self.verticalLayout_3.addWidget(self.e200)

        self.e100 = QLabel(self.widget)
        self.e100.setObjectName(u"e100")
        self.e100.setFont(font)

        self.verticalLayout_3.addWidget(self.e100)

        self.e50 = QLabel(self.widget)
        self.e50.setObjectName(u"e50")
        self.e50.setFont(font)

        self.verticalLayout_3.addWidget(self.e50)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lsc1000 = QLabel(self.widget)
        self.lsc1000.setObjectName(u"lsc1000")
        self.lsc1000.setFont(font)

        self.verticalLayout_4.addWidget(self.lsc1000)

        self.lsc500 = QLabel(self.widget)
        self.lsc500.setObjectName(u"lsc500")
        self.lsc500.setFont(font)

        self.verticalLayout_4.addWidget(self.lsc500)

        self.lsc200 = QLabel(self.widget)
        self.lsc200.setObjectName(u"lsc200")
        self.lsc200.setFont(font)

        self.verticalLayout_4.addWidget(self.lsc200)

        self.lsc100 = QLabel(self.widget)
        self.lsc100.setObjectName(u"lsc100")
        self.lsc100.setFont(font)

        self.verticalLayout_4.addWidget(self.lsc100)

        self.lsc50 = QLabel(self.widget)
        self.lsc50.setObjectName(u"lsc50")
        self.lsc50.setFont(font)

        self.verticalLayout_4.addWidget(self.lsc50)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addWidget(self.widget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.OkButton = QPushButton(self.layoutWidget)
        self.OkButton.setObjectName(u"OkButton")
        self.OkButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.OkButton)

        self.CancelButton = QPushButton(self.layoutWidget)
        self.CancelButton.setObjectName(u"CancelButton")
        self.CancelButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.CancelButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy-MM-dd", None))
        self.lc1000.setText(QCoreApplication.translate("Dialog", u"1000 x", None))
        self.lc500.setText(QCoreApplication.translate("Dialog", u"500 x", None))
        self.lc200.setText(QCoreApplication.translate("Dialog", u"200 x", None))
        self.lc100.setText(QCoreApplication.translate("Dialog", u"100 x", None))
        self.lc50.setText(QCoreApplication.translate("Dialog", u"50 x", None))
        self.e1000.setText(QCoreApplication.translate("Dialog", u"=", None))
        self.e500.setText(QCoreApplication.translate("Dialog", u"=", None))
        self.e200.setText(QCoreApplication.translate("Dialog", u"=", None))
        self.e100.setText(QCoreApplication.translate("Dialog", u"=", None))
        self.e50.setText(QCoreApplication.translate("Dialog", u"=", None))
        self.lsc1000.setText(QCoreApplication.translate("Dialog", u"1000 x", None))
        self.lsc500.setText(QCoreApplication.translate("Dialog", u"500 x", None))
        self.lsc200.setText(QCoreApplication.translate("Dialog", u"200 x", None))
        self.lsc100.setText(QCoreApplication.translate("Dialog", u"100 x", None))
        self.lsc50.setText(QCoreApplication.translate("Dialog", u"50 x", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0421\u0443\u043c\u0430", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"100000", None))
        self.OkButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.CancelButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

