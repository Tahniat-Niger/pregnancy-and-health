import psycopg2
import pandas as pd
from psycopg2 import Error


def connection():
    try:
        print("Connecting to the database ....")
        con = psycopg2.connect(
            user="postgres",
            password="",
            host="localhost",
            port="5432",
            database="postgre")
        con.autocommit = True
        if (con)
        print("The database connection is successful")
        return con
    except (Exception, Error) as error:
        print("Error while connecting to postgreSQL", error)
    finally:
        if (con):
            con.close


def Query1(conn):
    select_query1 = """select * from b;"""
    with conn.cursor() as cur:
        cur.execute(select_query1)
        records = cur.fetchall()
        for row in records:
            print(row)
        cur.close()


def query2(conn):
    select_query2 = """select * from a;"""
    with conn.cursor() as cur:
        cur.execute(select_query2)
        records = cur.fetchall()
        for row in records:
            print(row)
        cur.close()


def main():
    conn = connection()
    Query1(conn)
    query2(conn)


if __name__ == "__main__":
    main()
