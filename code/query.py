import psycopg2
import pandas as pd
from psycopg2 import Error


def connection():
    try:
        print("Connecting to the database ....")
        con = psycopg2.connect(
            user="postgres",
            password="postgre",
            host="localhost",
            port="5432",
            database="Pregnancy_and_Health")
        con.autocommit = True
        return con
    except (Exception, Error) as error:
        print("Error while connecting to postgreSQL", error)
    finally:
        if (con):
            con.close


def runQuery1(conn):
    select_query = """SELECT year, COUNT(death) AS total_death,underlying_cause, race_ethnicity FROM (SELECT d.year,
    d.underlying_cause,d.death, e.race_ethnicity FROM "Pregnancy_and_Health".death_record d JOIN 
    "Pregnancy_and_Health".race_ethnicity e ON d.ethnicity_id=e.id) AS death_record WHERE underlying_cause='Cancer'
    GROUP BY(year,underlying_cause,race_ethnicity);"""
    with conn.cursor() as cur:
        cur.execute(select_query)
        print("The First Query is Given Below")
        records = cur.fetchall()
        print("number of returned rows:", cur.rowcount)
        for row in records:
            print(
                f"Year = {row[0]}, Total Death = {row[1]}, Death Reason = {row[2]}, ethnicity = {row[3]} ")
        cur.close()


def runQuery2(conn):
    select_query = """SELECT m.heart_rate FROM "Pregnancy_and_Health".mental_health m
    JOIN "Pregnancy_and_Health".risk_level r ON m.risk_level_id=r.id AND r.risk_level='high risk'
    AND m.age<20 GROUP BY(m.heart_rate);"""
    with conn.cursor() as cur:
        cur.execute(select_query)
        print("")
        print("The Second Query is Given Below")
        records = cur.fetchall()
        print("number of returned rows:", cur.rowcount)
        for row in records:
            print(
                f"Heart Rate = {row[0]}")
        cur.close()


def main():
    conn = connection()
    if conn:
        print("Connection to the Postgre is successful")
        print("")
    else:
        print("Connection failed !")
    runQuery1(conn)
    runQuery2(conn)


if __name__ == "__main__":
    main()
