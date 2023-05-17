import datetime
from PySide2.QtWidgets import QDialog

from ui_add_update import Ui_Dialog 



class addDialog(QDialog):
    def __init__(self, *args, **kvargs):
        super().__init__(*args, **kvargs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
                
        self.ui.OkButton.clicked.connect(self.accept)
        self.ui.CancelButton.clicked.connect(self.reject)
        self.ui.dateEdit.setDate(datetime.date.today())
        self.ui.OkButton.clicked.connect(self.get_data)
        self.ui.sc1000.valueChanged.connect(self.set_label)
        self.ui.sc500.valueChanged.connect(self.set_label)
        self.ui.sc200.valueChanged.connect(self.set_label)
        self.ui.sc100.valueChanged.connect(self.set_label)
        self.ui.sc50.valueChanged.connect(self.set_label)

    def set_label(self):
        self.ui.lsc1000.setNum(1000*self.ui.sc1000.value())
        self.ui.lsc500.setNum(500*self.ui.sc500.value())
        self.ui.lsc200.setNum(200*self.ui.sc200.value())
        self.ui.lsc100.setNum(100*self.ui.sc100.value())
        self.ui.lsc50.setNum(50*self.ui.sc50.value())
        self.ui.label.setNum(1000*self.ui.sc1000.value()+500*self.ui.sc500.value()+200*self.ui.sc200.value()+100*self.ui.sc100.value()+50*self.ui.sc50.value())




    def get_data(self):
        return {
            "c_date": self.ui.dateEdit.date().toPython(),
            "c_1000": self.ui.sc1000.value(),
            "c_500": self.ui.sc500.value(),
            "c_200": self.ui.sc200.value(),
            "c_100": self.ui.sc100.value(),
            "c_50": self.ui.sc50.value()
        }