from PySide2 import QtCore


class ItemsModel(QtCore.QAbstractTableModel):
    def __init__(self, *args, **kvargs):
        super().__init__(*args, **kvargs)

        self.items = []
        self.periods = {}
        

    def setItems(self, items):
        self.beginResetModel()
        self.items = items
        self.endResetModel()

    def setPeriod(self, periods):
        self.beginResetModel()
        self.periods = periods
        self.endResetModel()

    def rowCount(self, *args, **kvargs) -> int:
        return len(self.items)
    
    def columnCount(self, *args, **kvargs) -> int:
        return 3
    
    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole):
        if not index.isValid:
            return
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            sumtodate = self.items[index.row()]
            col = index.column()
            if col == 0:
                return f'{sumtodate.c_id}'
            elif col == 1:
                return f'{sumtodate.DATE}'
            elif col == 2:
                return f'{sumtodate.SUMA}'
        elif role == QtCore.Qt.ItemDataRole.UserRole:
            return self.items[index.row()]
        
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return {
                    0: "id",
                    1: "ДАТА",
                    2: "СУМА"
                }.get(section)
        return super().headerData(section, orientation, role)