import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2 import QtCore, QtGui
from PySide2.QtCharts import QtCharts as qtch
from data.add_day_cash_sum import add_day_cash_sum
from data.add_new_period import add_new_period
from data.create_database import DB
from data.create_session import create_session
from data.delete_day_cash_sum import delete_day_cash_sum
from data.edit_day_cash_sum import edit_day_cash_sum
from data.edit_period import edit_period
from data.fetch_all_period import fetch_all_period
from data.fetch_cash_sum import fetch_cash_sum
from data.get_id_edit_day_cash_sum import get_id_edit_day_cash_sum
from data.get_id_edit_period import get_id_edit_period
from dialogs.add_dialog import addDialog
from dialogs.correct_period_dialog import correctPeriodDialog
from models.items_model import ItemsModel
from dialogs.new_period_dialog import newPeriodDialog

from ui_mainwindowt import Ui_MainWindow

from dialogs.update_dialog import UpdateDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("currency.png"))

        self.model = ItemsModel()
        self.ui.tableView.setModel(self.model)

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

        with create_session() as s:
            r = get_id_edit_period(s, init_data)

        dialog = correctPeriodDialog(r)
        dialog.setWindowTitle("EDIT")
        p = dialog.exec_()
        if p == 0:
            return

        data = dialog.get_dates_period()
        with create_session() as s:
            edit_period(s, data, r)
        self.load_periods()
        self.load_cash()

    def on_btnNewPeriod(self):
        dialog = newPeriodDialog(self.p_max)
        p = dialog.exec_()
        if p == 0:
            return

        data = dialog.get_dates_period()
        with create_session() as s:
            add_new_period(s, data)
        self.load_periods()
        self.load_cash()

    def on_btnEdit_click(self):
        item = self.ui.tableView.currentIndex()

        init_data = item.data(QtCore.Qt.ItemDataRole.UserRole)
        if init_data == None:
            return

        with create_session() as s:
            r = get_id_edit_day_cash_sum(s, init_data)

        dialog = UpdateDialog(r)
        dialog.set_label()
        dialog.setWindowTitle("EDIT")
        p = dialog.exec_()
        if p == 0:
            return

        data = dialog.get_data()
        with create_session() as s:
            edit_day_cash_sum(s, data, r)
        self.load_cash()

    def on_btnDelete_click(self):
        item = self.ui.tableView.currentIndex()
        data = item.data(QtCore.Qt.ItemDataRole.UserRole)
        if data == None:
            return
        r = QMessageBox.question(self, "Підтвердження", "Видалити запис?")
        if r == QMessageBox.StandardButton.No:
            return
        with create_session() as s:
            delete_day_cash_sum(s, data)

        self.load_cash()

    def on_btnAdd_click(self):
        dialog = addDialog()
        dialog.set_label()
        dialog.setWindowTitle("ADD")
        r = dialog.exec_()
        if r == 0:
            return
        data = dialog.get_data()
        with create_session() as s:
            add_day_cash_sum(s, data)

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

        with create_session() as s:
            listsum, rows = fetch_cash_sum(s, date_from, date_to)

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
        self.periods = {}
        with create_session() as s:
            rows = fetch_all_period(s)

            for r in rows:
                self.periods[r.p_id] = r

        self.p_min = min([i.p_from for i in self.periods.values()])
        self.p_max = max([i.p_to for i in self.periods.values()])

        for r in self.periods.values():
            item = f"Від {r.p_from} до {r.p_to}"
            self.ui.cmbPeriods.addItem(item, r)

        self.ui.cmbPeriods.addItem("Всі періоди")

        self.model.setPeriod(self.periods)

    def draw_bar_chart(self):
        series = qtch.QHorizontalBarSeries()
        bar_set = qtch.QBarSet("Візуалізація сум по днях")
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
    db = DB()
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
