from sqlalchemy import text
from sqlalchemy.orm import Session


def edit_day_cash_sum(s: Session, data, r):
    query = """
            UPDATE cashboxes SET 
            c_date = :c_date, 
            c_1000 = :c_1000, 
            c_500 = :c_500, 
            c_200 = :c_200, 
            c_100 = :c_100, 
            c_50 = :c_50 
            WHERE c_id = :c_id
            """
    s.execute(text(query), {
                "c_date": data['c_date'],
                "c_1000": data['c_1000'],
                "c_500": data['c_500'],
                "c_200": data['c_200'],
                "c_100": data['c_100'],
                "c_50": data['c_50'],
                "c_id": r[0]
            })
    s.commit()