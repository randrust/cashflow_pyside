import datetime
from PySide2.QtWidgets import QDialog

from ui_new_period import Ui_DialogP



class correctPeriodDialog(QDialog):
    def __init__(self,  init_data, *args, **kvargs):
        super().__init__(*args, **kvargs)
        self.ui = Ui_DialogP()
        self.ui.setupUi(self)
        self.ui.label.setText("Виправити поточний")
                
        self.ui.btnOk.clicked.connect(self.accept)
        self.ui.btnCancel.clicked.connect(self.reject)

        self.ui.dateEditFrom.setDate(datetime.datetime.strptime(init_data[1], "%Y-%m-%d"))
        self.ui.dateEditTo.setDate(datetime.datetime.strptime(init_data[2], "%Y-%m-%d"))

    def get_dates_period(self):
        return {
            "p_from": self.ui.dateEditFrom.date().toPython(),
            "p_to": self.ui.dateEditTo.date().toPython()
        }
