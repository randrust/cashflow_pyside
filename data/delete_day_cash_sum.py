from sqlalchemy import text
from sqlalchemy.orm import Session

def delete_day_cash_sum(s: Session, data):
    query = """
            DELETE FROM cashboxes WHERE c_id = :c_id
            """
    s.execute(text(query), {'c_id': data.c_id})
    s.commit()