from sqlalchemy import text
from sqlalchemy.orm import Session


def edit_period(s: Session, data, r):
    query = """
            UPDATE periods SET 
            p_from = :p_from, 
            p_to = :p_to
            WHERE p_id = :p_id
            """
    s.execute(text(query), {
                "p_from": data['p_from'],
                "p_to": data['p_to'],
                "p_id": r[0]
            })
    s.commit()