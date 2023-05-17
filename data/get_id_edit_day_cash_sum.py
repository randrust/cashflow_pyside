from sqlalchemy import text
from sqlalchemy.orm import Session


def get_id_edit_day_cash_sum(s: Session, init_data):
    query = """
            SELECT * FROM cashboxes WHERE c_id = :c_id
            """
    r = s.execute(text(query), {'c_id': init_data.c_id}).fetchone()

    return r