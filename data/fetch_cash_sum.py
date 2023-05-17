from sqlalchemy import text
from sqlalchemy.orm import Session



def fetch_cash_sum(s: Session, date_from, date_to):
    query1 = """
            SELECT c_id, c_date AS DATE, 
            (c_1000*1000+c_500*500+c_200*200+c_100*100+c_50*50) AS SUMA 
            FROM cashboxes 
            WHERE DATE BETWEEN :df AND :dt
            ORDER BY DATE DESC"""
    query2 = """
            SELECT SUM(c_1000*1000+c_500*500+c_200*200+c_100*100+c_50*50) 
            FROM cashboxes
            WHERE c_date BETWEEN :df AND :dt
            """
    listsum = s.execute(text(query2), {"df": date_from, "dt": date_to}).fetchall()[0][0]
    rows = s.execute(text(query1), {"df": date_from, "dt": date_to})

    return (listsum, rows)