from sqlalchemy import text
from sqlalchemy.orm import Session


def add_day_cash_sum(s: Session, data):
    query = """
            INSERT INTO cashboxes(c_date, c_1000, c_500, c_200, c_100, c_50) 
            VALUES (:c_date, :c_1000, :c_500, :c_200, :c_100, :c_50) 
            """
    s.execute(text(query), {
                "c_date": data['c_date'],
                "c_1000": data['c_1000'],
                "c_500": data['c_500'],
                "c_200": data['c_200'],
                "c_100": data['c_100'],
                "c_50": data['c_50']
            })
    s.commit()