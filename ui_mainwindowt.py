# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowtkXzXas.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qchartview import QChartView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1010, 670)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.listCash = QListWidget(self.centralwidget)
        self.listCash.setObjectName(u"listCash")

        self.gridLayout.addWidget(self.listCash, 1, 0, 1, 3)

        self.btnDelete = QPushButton(self.centralwidget)
        self.btnDelete.setObjectName(u"btnDelete")

        self.gridLayout.addWidget(self.btnDelete, 0, 2, 1, 1)

        self.lbl = QLabel(self.centralwidget)
        self.lbl.setObjectName(u"lbl")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl, 2, 0, 1, 1)

        self.lblSuma = QLabel(self.centralwidget)
        self.lblSuma.setObjectName(u"lblSuma")
        self.lblSuma.setFont(font)
        self.lblSuma.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblSuma, 2, 1, 1, 2)

        self.btnEdit = QPushButton(self.centralwidget)
        self.btnEdit.setObjectName(u"btnEdit")

        self.gridLayout.addWidget(self.btnEdit, 0, 1, 1, 1)

        self.btnAdd = QPushButton(self.centralwidget)
        self.btnAdd.setObjectName(u"btnAdd")

        self.gridLayout.addWidget(self.btnAdd, 0, 0, 1, 1)

        self.chartView1 = QChartView(self.centralwidget)
        self.chartView1.setObjectName(u"chartView1")

        self.gridLayout.addWidget(self.chartView1, 1, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1010, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnDelete.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.lbl.setText(QCoreApplication.translate("MainWindow", u"SUMA", None))
        self.lblSuma.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnEdit.setText(QCoreApplication.translate("MainWindow", u"EDIT", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
    # retranslateUi

