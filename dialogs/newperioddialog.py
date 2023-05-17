import datetime
from PySide2.QtWidgets import QDialog

from ui_new_period import Ui_DialogP



class newPeriodDialog(QDialog):
    def __init__(self, p_max, *args, **kvargs):
        super().__init__(*args, **kvargs)
        self.ui = Ui_DialogP()
        self.ui.setupUi(self)
                
        self.ui.btnOk.clicked.connect(self.accept)
        self.ui.btnCancel.clicked.connect(self.reject)
        # self.ui.dateEdit.setDate(datetime.date.today())
        self.ui.dateEditFrom.setDate(datetime.datetime.strptime(p_max, "%Y-%m-%d")+datetime.timedelta(days=1))
        self.ui.dateEditTo.setDate(datetime.datetime.strptime(p_max, "%Y-%m-%d")+datetime.timedelta(days=21))

    def get_dates_period(self):
        return {
            "p_from": self.ui.dateEditFrom.date().toPython(),
            "p_to": self.ui.dateEditTo.date().toPython()
        }
    