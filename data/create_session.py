from sqlalchemy import create_engine
from sqlalchemy.orm import Session

def create_session() -> Session:
    engine = create_engine("sqlite+pysqlite:///cashflow.sqlite", echo=True)

    s = Session(engine)
    return s

