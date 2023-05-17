import datetime
from dialogs.add_dialog import addDialog


class UpdateDialog(addDialog):
    def __init__(self, init_data, *args, **kvargs):
        super().__init__(*args, **kvargs)

        self.ui.dateEdit.setDate(datetime.datetime.strptime(init_data[1], "%Y-%m-%d"))
        self.ui.sc1000.setValue(init_data[2])
        self.ui.sc500.setValue(init_data[3])
        self.ui.sc200.setValue(init_data[4])
        self.ui.sc100.setValue(init_data[5])
        self.ui.sc50.setValue(init_data[6])
