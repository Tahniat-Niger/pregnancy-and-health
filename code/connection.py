import psycopg2
import pandas as pd
from psycopg2 import Error
try:
    con = psycopg2.connect(
        user="postgres",
        password="postgre",
        host="localhost",
        port="5432",
        database="Pregnancy_and_Health")
    print("connection has establish")
    cur = con.cursor()

except (Exception, Error) as error:
    print("Error while connecting to postgreSQL", error)
finally:
    if (con):
        cur.close()
        con.close()
        print("Connection is closed")
