import sys

import PySide2
from PySide2.QtWidgets import QApplication, QMainWindow
from ui_mainwindowt import Ui_MainWindow
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.engine = create_engine("sqlite+pysqlite:///cashflow.sqlite", echo=True)
        self.load_cash()

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
