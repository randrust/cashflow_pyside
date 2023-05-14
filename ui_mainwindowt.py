# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowtzSiGZy.ui'
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

        self.btnNewPeriod = QPushButton(self.centralwidget)
        self.btnNewPeriod.setObjectName(u"btnNewPeriod")

        self.gridLayout.addWidget(self.btnNewPeriod, 1, 2, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 3)

        self.btnEdit = QPushButton(self.centralwidget)
        self.btnEdit.setObjectName(u"btnEdit")

        self.gridLayout.addWidget(self.btnEdit, 5, 1, 1, 1)

        self.btnDelete = QPushButton(self.centralwidget)
        self.btnDelete.setObjectName(u"btnDelete")

        self.gridLayout.addWidget(self.btnDelete, 5, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.lbl = QLabel(self.centralwidget)
        self.lbl.setObjectName(u"lbl")
        self.lbl.setFont(font)
        self.lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl, 7, 0, 1, 2)

        self.cmbPeriods = QComboBox(self.centralwidget)
        self.cmbPeriods.setObjectName(u"cmbPeriods")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setWeight(50)
        self.cmbPeriods.setFont(font1)

        self.gridLayout.addWidget(self.cmbPeriods, 2, 0, 1, 3)

        self.btnAdd = QPushButton(self.centralwidget)
        self.btnAdd.setObjectName(u"btnAdd")

        self.gridLayout.addWidget(self.btnAdd, 5, 0, 1, 1)

        self.lblSuma = QLabel(self.centralwidget)
        self.lblSuma.setObjectName(u"lblSuma")
        self.lblSuma.setFont(font)
        self.lblSuma.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lblSuma, 7, 2, 1, 1)

        self.chartView1 = QChartView(self.centralwidget)
        self.chartView1.setObjectName(u"chartView1")

        self.gridLayout.addWidget(self.chartView1, 0, 3, 8, 1)

        self.btnEditPeriod = QPushButton(self.centralwidget)
        self.btnEditPeriod.setObjectName(u"btnEditPeriod")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(28)
        sizePolicy.setHeightForWidth(self.btnEditPeriod.sizePolicy().hasHeightForWidth())
        self.btnEditPeriod.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btnEditPeriod, 1, 0, 1, 2)


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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CASH FLOW", None))
        self.btnNewPeriod.setText(QCoreApplication.translate("MainWindow", u"\u041d\u041e\u0412\u0418\u0419", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0423\u041c\u0418 \u041f\u041e \u0414\u0410\u0422\u0410", None))
        self.btnEdit.setText(QCoreApplication.translate("MainWindow", u"\u0417\u041c\u0406\u041d\u0418\u0422\u0418", None))
        self.btnDelete.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0418\u0414\u0410\u041b\u0418\u0422\u0418", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0415\u0420\u0415\u041e\u0411\u041b\u0406\u041a", None))
        self.lbl.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u044c\u043e\u0433\u043e \u0437\u0430 \u043f\u0435\u0440\u0456\u043e\u0434", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"\u0414\u041e\u0414\u0410\u0422\u0418", None))
        self.lblSuma.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnEditPeriod.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0418\u041f\u0420\u0410\u0412\u0418\u0422\u0418", None))
    # retranslateUi

