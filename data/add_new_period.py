from sqlalchemy import text
from sqlalchemy.orm import Session


def add_new_period(s: Session, data):
    query = """
            INSERT INTO periods(p_from, p_to) 
            VALUES (:p_from, :p_to) 
            """
    s.execute(text(query), {
                "p_from": data['p_from'],
                "p_to": data['p_to']
            })
    s.commit()
