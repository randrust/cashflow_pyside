from PySide2 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('cashflowpyqt.sqlite')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec_("""CREATE TABLE IF NOT EXISTS cashboxes (
                    c_id integer primary key, 
                    c_date date, 
                    c_1000 integer default 0, 
                    c_500 integer default 0, 
                    c_200 integer default 0, 
                    c_100 integer default 0, 
                    c_50 integer default 0
                    )""")
        query.exec_("""CREATE TABLE IF NOT EXISTS periods (
                    p_id integer primary key, 
                    p_from date, 
                    p_to date
                    )""")
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec_()

        return query

    def add_new_transaction_query(self, date, category, description, balance, status):
        sql_query = "INSERT INTO expenses (Date, Category, Description, Balance, Status) VALUES (?, ?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [date, category, description, balance, status])

    def update_transaction_query(self, date, category, description, balance, status, id):
        sql_query = "UPDATE expenses SET Date=?, Category=?, Description=?, Balance=?, Status=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [date, category, description, balance, status, id])

    def delete_transaction_query(self, id):
        sql_query = "DELETE FROM expenses WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def get_total(self, column, filter=None, value=None):
        sql_query = f"SELECT SUM({column}) FROM expenses"

        if filter is not None and value is not None:
            sql_query += f" WHERE {filter} = ?"

        query_values = []

        if value is not None:
            query_values.append(value)

        query = self.execute_query_with_params(sql_query, query_values)

        if query.next():
            return str(query.value(0)) + '$'

        return '0'

    def total_balance(self):
        return self.get_total(column="Balance")

    def total_income(self):
        return self.get_total(column="Balance", filter="Status", value="Income")

    def total_outcome(self):
        return self.get_total(column="Balance", filter="Status", value="Outcome")

    def total_groceries(self):
        return self.get_total(column="Balance", filter="Category", value="Grocery")

    def total_auto(self):
        return self.get_total(column="Balance", filter="Category", value="Auto")

    def total_entertainment(self):
        return self.get_total(column="Balance", filter="Category", value="Entertainment")

    def total_other(self):
        return self.get_total(column="Balance", filter="Category", value="Other")
    

if __name__ == "__main__":
        db = Data()