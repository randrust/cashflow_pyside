from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session


class DB:
    def __init__(self):
        self.creat_database_tables()

    def create_session(self) -> Session:
        engine = create_engine("sqlite+pysqlite:///cashflow.sqlite", echo=True)
        s = Session(engine)
        return s


    def creat_database_tables(self):
        with self.create_session() as s:
            self.query = '''
                CREATE TABLE IF NOT EXISTS cashboxes (
                    c_id integer primary key, 
                    c_date date, 
                    c_1000 integer default 0, 
                    c_500 integer default 0, 
                    c_200 integer default 0, 
                    c_100 integer default 0, 
                    c_50 integer default 0
                    )
                '''
            s.execute(text(self.query))
            s.commit()
            self.query = '''
                CREATE TABLE IF NOT EXISTS periods (
                    p_id integer primary key, 
                    p_from date, 
                    p_to date
                    )
                '''
            s.execute(text(self.query))
            s.commit()



if __name__ == "__main__":
    db = DB()

