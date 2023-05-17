from sqlalchemy import text
from sqlalchemy.orm import Session


def fetch_all_period(s: Session):
    query = """
            SELECT * FROM periods ORDER BY p_to DESC
            """
    rows = s.execute(text(query))
    return rows