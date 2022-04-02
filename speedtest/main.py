import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import grizzly
from grizzly.relationaldbexecutor import RelationalExecutor
from grizzly.sqlgenerator import SQLGenerator

import timing
import config
import data_prep

import cx_Oracle
import psycopg2

def myfunc2(a: int) -> str:
    n: float = 22.3
    i: int = 2
    f: str = "hello"
    return a + i


@timing.timing
def show_udfs(df, lang):
    # Prepare df
    df = df[["test_text", "test_float", "test_number"]]
    df["udf"] = df["test_id"].map(myfunc2, lang)  # apply myfunc

    # Print generated query
    # print("----------------------------------------")
    #print(df.generateQuery())
    #print("----------------------------------------")

    # Show table
    df.show(pretty=True, limit=1)
    #print("----------------------------------------")


def compare_sql(iteration_index, iterations):
    times = []

    for s in config.test_cases:
        print("----------------------------------------")
        print(s[0])
        if s[2] == config.postgres_uni or s[2] == config.postgres_pi:
            con = psycopg2.connect(dbname=s[2]['dbname'], user=s[2]['user'], password=s[2]['password'], host=s[2]['host'], keepalives=1)
        elif s[2] == config.postgres:
            con = psycopg2.connect(dbname=s[2]['dbname'], user=s[2]['user'], password=s[2]['password'], keepalives=1)
        elif s[2] == config.oracle:
            con = cx_Oracle.connect(user=s[2]['user'], password=s[2]['password'], dsn=s[2]['dsn'])
        
        with con as conn:
            # Insert test data into db
            data_prep.Data_prep(conn, iteration_index, iterations)
            # Tell grizzly connection and db-type
            grizzly.use(RelationalExecutor(conn, SQLGenerator(s[1])))
            # create df as table reference
            df = grizzly.read_table("speedtest")
            # execute query and get time for that
            time = show_udfs(df, s[3])
            times.append([iterations[iteration_index], s[0], time[1]])

    return times

if __name__ == "__main__":
    compare_sql(0, [10000])