from sqlalchemy import text
from sqlalchemy.orm import Session


def get_id_edit_period(s: Session, init_data):
    query = """
            SELECT * FROM periods WHERE p_id = :p_id
            """
    r = s.execute(text(query), {'p_id': init_data.p_id}).fetchone()

    return r