import sqlite3

class DB:
    def __init__(self):
        self.conn = sqlite3.connect('cashflow.sqlite')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS cashboxes (
                c_id integer primary key, 
                c_date date, 
                c_1000 integer default 0, 
                c_500 integer default 0, 
                c_200 integer default 0, 
                c_100 integer default 0, 
                c_50 integer default 0
                )
            ''')
        self.conn.commit()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS periods (
                p_id integer primary key, 
                p_from date, 
                p_to date
                )
            ''')
        self.conn.commit()

DB()