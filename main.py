import sys
# import datetime
# import typing
# import PySide2
import PySide2.QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QListWidgetItem, QMessageBox
from PySide2 import QtCore, QtGui
from PySide2.QtCharts import QtCharts as qtch
from dialogs.adddialog import addDialog
from dialogs.correctperioddialog import correctPeriodDialog
from models.itemsmodel import ItemsModel
from dialogs.newperioddialog import newPeriodDialog
from ui_new_period import Ui_DialogP
from ui_add_update import Ui_Dialog
from ui_mainwindowt import Ui_MainWindow
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from dialogs.updatedialog import UpdateDialog




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('currency.png'))

        self.model = ItemsModel()
        self.ui.tableView.setModel(self.model)

        self.engine = create_engine("sqlite+pysqlite:///cashflow.sqlite", echo=True)
        self.load_periods()
        self.load_cash()
        self.ui.tableView.hideColumn(0)
        self.ui.btnAdd.clicked.connect(self.on_btnAdd_click)
        self.ui.btnDelete.clicked.connect(self.on_btnDelete_click)
        self.ui.btnEdit.clicked.connect(self.on_btnEdit_click)
        self.ui.cmbPeriods.currentIndexChanged.connect(self.load_cash)
        self.ui.btnNewPeriod.clicked.connect(self.on_btnNewPeriod)
        self.ui.btnEditPeriod.clicked.connect(self.on_btnEditPeriod_click)

    def on_btnEditPeriod_click(self):
        init_data = self.ui.cmbPeriods.currentData()
        if init_data == None:
            return

        with Session(self.engine) as s:
            query = """
            SELECT * FROM periods WHERE p_id = :p_id
            """
            r = s.execute(text(query), {'p_id': init_data.p_id}).fetchone()


        dialog = correctPeriodDialog(r)
        dialog.setWindowTitle("EDIT")
        p = dialog.exec_()
        if p == 0:
            return

        data = dialog.get_dates_period()
        with Session(self.engine) as s:
            query = """
            UPDATE periods SET 
            p_from = :p_from, 
            p_to = :p_to
            WHERE p_id = :p_id
            """
            s.execute(text(query), {
                "p_from": data['p_from'],
                "p_to": data['p_to'],
                "p_id": r[0]
            })
            s.commit()
        self.load_periods()
        self.load_cash()


    def on_btnNewPeriod(self):
        dialog = newPeriodDialog(self.p_max)
        p = dialog.exec_()
        if p == 0:
            return
        
        data = dialog.get_dates_period()
        with Session(self.engine) as s:
            query = """
            INSERT INTO periods(p_from, p_to) 
            VALUES (:p_from, :p_to) 
            """
            s.execute(text(query), {
                "p_from": data['p_from'],
                "p_to": data['p_to']
            })
            s.commit()
        self.load_periods()
        self.load_cash()
        

    def on_btnEdit_click(self):

        item = self.ui.tableView.currentIndex()
        
        init_data = item.data(QtCore.Qt.ItemDataRole.UserRole)
        if init_data == None:
            return

        with Session(self.engine) as s:
            query = """
            SELECT * FROM cashboxes WHERE c_id = :c_id
            """
            r = s.execute(text(query), {'c_id': init_data.c_id}).fetchone()


        dialog = UpdateDialog(r)
        dialog.set_label()
        dialog.setWindowTitle("EDIT")
        p = dialog.exec_()
        if p == 0:
            return

        data = dialog.get_data()
        with Session(self.engine) as s:
            query = """
            UPDATE cashboxes SET 
            c_date = :c_date, 
            c_1000 = :c_1000, 
            c_500 = :c_500, 
            c_200 = :c_200, 
            c_100 = :c_100, 
            c_50 = :c_50 
            WHERE c_id = :c_id
            """
            s.execute(text(query), {
                "c_date": data['c_date'],
                "c_1000": data['c_1000'],
                "c_500": data['c_500'],
                "c_200": data['c_200'],
                "c_100": data['c_100'],
                "c_50": data['c_50'],
                "c_id": r[0]
            })
            s.commit()
        self.load_cash()


    def on_btnDelete_click(self):
        item = self.ui.tableView.currentIndex()
        data = item.data(QtCore.Qt.ItemDataRole.UserRole)
        if data == None:
            return
        r = QMessageBox.question(self, "Підтвердження", "Видалити запис?")
        if r == QMessageBox.StandardButton.No:
            return
        with Session(self.engine) as s:
            query = """
            DELETE FROM cashboxes WHERE c_id = :c_id
            """
            s.execute(text(query), {'c_id': data.c_id})
            s.commit()

        self.load_cash()


    def on_btnAdd_click(self):
        dialog = addDialog()
        dialog.set_label()
        dialog.setWindowTitle("ADD")
        r = dialog.exec_()
        if r == 0:
            return
        data = dialog.get_data()
        with Session(self.engine) as s:
            query = """
            INSERT INTO cashboxes(c_date, c_1000, c_500, c_200, c_100, c_50) 
            VALUES (:c_date, :c_1000, :c_500, :c_200, :c_100, :c_50) 
            """
            s.execute(text(query), {
                "c_date": data['c_date'],
                "c_1000": data['c_1000'],
                "c_500": data['c_500'],
                "c_200": data['c_200'],
                "c_100": data['c_100'],
                "c_50": data['c_50']
            })
            s.commit()
        self.load_cash()




    def load_cash(self):
        period_data = self.ui.cmbPeriods.currentData()
        if period_data:
            date_from = self.ui.cmbPeriods.currentData().p_from
            date_to = self.ui.cmbPeriods.currentData().p_to
        else:
            date_from = self.p_min
            date_to = self.p_max
        self.rowsDate = []
        self.rowsSuma = []
        self.rows = []

        with Session(self.engine) as s:
            query1 = """
            SELECT c_id, c_date AS DATE, 
            (c_1000*1000+c_500*500+c_200*200+c_100*100+c_50*50) AS SUMA 
            FROM cashboxes 
            WHERE DATE BETWEEN :df AND :dt
            ORDER BY DATE DESC"""
            query2 = """
            SELECT SUM(c_1000*1000+c_500*500+c_200*200+c_100*100+c_50*50) 
            FROM cashboxes
            WHERE c_date BETWEEN :df AND :dt
            """
            listsum = s.execute(text(query2), {"df": date_from, "dt": date_to}).fetchall()[0][0]
            rows = s.execute(text(query1), {"df": date_from, "dt": date_to})
            for r in rows:
                self.rowsDate.append(r.DATE)
                self.rowsSuma.append(r.SUMA)
                self.rows.append(r)
                
            if not listsum:
                listsum = 0
            self.ui.lblSuma.setNum(listsum)

        self.model.setItems(self.rows)
        self.draw_bar_chart()

    def load_periods(self):
        self.ui.cmbPeriods.clear()            
        self.periods ={}
        with Session(self.engine) as s:
            query = """
            SELECT * FROM periods ORDER BY p_to DESC
            """
            rows = s.execute(text(query))
            for r in rows:
                self.periods[r.p_id] = r
        
        self.p_min = min([i.p_from for i in self.periods.values()])
        self.p_max = max([i.p_to for i in self.periods.values()])


        for r in self.periods.values():
            item = f"Від {r.p_from} до {r.p_to}"
            self.ui.cmbPeriods.addItem(item, r)

        self.ui.cmbPeriods.addItem("Всі періоди")

        self.model.setPeriod(self.periods)
        

    def  draw_bar_chart(self):
        series = qtch.QHorizontalBarSeries()
        bar_set = qtch.QBarSet("Суми по датах")
        for row in self.rowsSuma[::-1]:
            bar_set.append(row)
        series.append(bar_set)
        series.setLabelsVisible()
        chart = qtch.QChart()
        chart.addSeries(series)
        axis = qtch.QBarCategoryAxis()
        axis.append(self.rowsDate[::-1])
        chart.setAxisY(axis)
        series.attachAxis(axis)
        self.ui.chartView1.setChart(chart)


    



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
