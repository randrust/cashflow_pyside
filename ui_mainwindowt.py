# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowtGFHkCW.ui'
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
        MainWindow.resize(1010, 662)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 6, 0, 1, 3)

        self.chartView1 = QChartView(self.centralwidget)
        self.chartView1.setObjectName(u"chartView1")

        self.gridLayout.addWidget(self.chartView1, 0, 3, 8, 1)

        self.btnDelete = QPushButton(self.centralwidget)
        self.btnDelete.setObjectName(u"btnDelete")

        self.gridLayout.addWidget(self.btnDelete, 5, 2, 1, 1)

        self.btnNewPeriod = QPushButton(self.centralwidget)
        self.btnNewPeriod.setObjectName(u"btnNewPeriod")

        self.gridLayout.addWidget(self.btnNewPeriod, 1, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.lblSuma = QLabel(self.centralwidget)
        self.lblSuma.setObjectName(u"lblSuma")
        self.lblSuma.setFont(font)
        self.lblSuma.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblSuma, 7, 1, 1, 2)

        self.cmbPeriods = QComboBox(self.centralwidget)
        self.cmbPeriods.setObjectName(u"cmbPeriods")

        self.gridLayout.addWidget(self.cmbPeriods, 1, 0, 1, 2)

        self.lbl = QLabel(self.centralwidget)
        self.lbl.setObjectName(u"lbl")
        self.lbl.setFont(font)
        self.lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl, 7, 0, 1, 1)

        self.btnAdd = QPushButton(self.centralwidget)
        self.btnAdd.setObjectName(u"btnAdd")

        self.gridLayout.addWidget(self.btnAdd, 5, 0, 1, 1)

        self.btnEdit = QPushButton(self.centralwidget)
        self.btnEdit.setObjectName(u"btnEdit")

        self.gridLayout.addWidget(self.btnEdit, 5, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 3)

        self.btnAllSum = QPushButton(self.centralwidget)
        self.btnAllSum.setObjectName(u"btnAllSum")

        self.gridLayout.addWidget(self.btnAllSum, 2, 0, 1, 3)


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
        self.btnNewPeriod.setText(QCoreApplication.translate("MainWindow", u"NEW", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043e\u0431\u043b\u0456\u043a", None))
        self.lblSuma.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u044c\u043e\u0433\u043e", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.btnEdit.setText(QCoreApplication.translate("MainWindow", u"EDIT", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u0438 \u043f\u043e \u0434\u0430\u0442\u0430\u0445", None))
        self.btnAllSum.setText(QCoreApplication.translate("MainWindow", u"ALL", None))
    # retranslateUi

