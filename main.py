import sys
import datetime
import PySide2
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from ui_add_update import Ui_Dialog
from ui_mainwindowt import Ui_MainWindow
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session


class addDialog(QDialog):
    def __init__(self, *args, **kvargs):
        super().__init__(*args, **kvargs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.OkButton.clicked.connect(self.accept)
        self.ui.CancelButton.clicked.connect(self.reject)
        self.ui.dateEdit.setDate(datetime.date.today())
        self.ui.OkButton.clicked.connect(self.get_data)


    def get_data(self):
        return {
            "c_date": self.ui.dateEdit.date().toPython(),
            "c_1000": self.ui.sc1000.value(),
            "c_500": self.ui.sc500.value(),
            "c_200": self.ui.sc200.value(),
            "c_100": self.ui.sc100.value(),
            "c_50": self.ui.sc50.value()
        }

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.engine = create_engine("sqlite+pysqlite:///cashflow.sqlite", echo=True)
        self.load_cash()
        self.ui.btnAdd.clicked.connect(self.on_btnAdd_click)

    def on_btnAdd_click(self):
        dialog = addDialog()
        r = dialog.exec_()
        if r == 1:
            pass

    def load_cash(self):
        with Session(self.engine) as s:
            query1 = """
            SELECT c_id, c_date AS DATE, 
            (c_1000*1000+c_500*500+c_200*200+c_100*100+c_50*50) AS SUMA 
            FROM cashboxes ORDER BY DATE DESC"""
            query2 = """SELECT SUM(c_1000*1000+c_500*500+c_200*200+c_100*100+c_50*50) FROM cashboxes"""
            listsum = s.execute(text(query2)).fetchall()[0][0]
            rows = s.execute(text(query1))
            for r in rows:
                self.ui.listCash.addItem(f"{r.DATE}====={r.SUMA}====={r.c_id}")

            self.ui.lblSuma.setNum(listsum)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
