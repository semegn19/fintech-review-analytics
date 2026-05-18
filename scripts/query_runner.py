import pandas as pd

def run_query(sql, conn):
    return pd.read_sql(sql, conn)