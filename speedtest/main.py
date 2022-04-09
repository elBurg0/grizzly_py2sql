import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import functions
import plots
import grizzly
from grizzly.relationaldbexecutor import RelationalExecutor
from grizzly.sqlgenerator import SQLGenerator

import timing
import config
import data_prep

import cx_Oracle
import psycopg2

@timing.timing
def show_udfs(df, lang, func):
    # Prepare df
    df = df[["test_text", "test_float", "test_number"]]
    df["udf"] = df["test_id"].map(func, lang)  # apply myfunc

    # Print generated query
    # print("----------------------------------------")
    #print(df.generateQuery())
    #print("----------------------------------------")

    # Show table
    df.show(pretty=True, limit=1)
    #print("----------------------------------------")


def compare_sql(iteration_index, iterations, func):
    times = []

    for s in config.test_cases:
        print("----------------------------------------")
        print(s[0])
        if s[2] == config.postgres_uni or s[2] == config.postgres_pi:
            con = psycopg2.connect(dbname=s[2]['dbname'], user=s[2]['user'], password=s[2]['password'], host=s[2]['host'], keepalives=1)
        elif s[2] == config.postgres:
            con = psycopg2.connect(dbname=s[2]['dbname'], user=s[2]['user'], password=s[2]['password'], keepalives=1)
        elif s[2] == config.oracle or config.oracle_pdb:
            con = cx_Oracle.connect(user=s[2]['user'], password=s[2]['password'], dsn=s[2]['dsn'])
        
        with con as conn:
            # Insert test data into db
            data_prep.Data_prep(conn, iteration_index, iterations)
            # Tell grizzly connection and db-type
            grizzly.use(RelationalExecutor(conn, SQLGenerator(s[1])))
            # create df as table reference
            df = grizzly.read_table("speedtest")
            # execute query and get time for that
            time = show_udfs(df, s[3], func)
            times.append([iterations[iteration_index], s[0], time[1]])

    return times

if __name__ == "__main__":
    func = functions.myfunc2
    times = []
    test_iterations2 = [10, 100, 500, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 250000, 500000, 750000, 1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 4500000, 5000000]
    test_iterations = []

    for f in range(1, 200):
        if f % 20 == 0:
            test_iterations.append(f)

    print(test_iterations)

    try:
        for i,_ in enumerate(test_iterations):
            times += compare_sql(i, test_iterations, func)
            print("\n")
    except KeyboardInterrupt as e:
        print(e)
    
    plots.plot(func.__name__, times)

    compare_sql(0, [10000])