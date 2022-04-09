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
from data_prep import Data_prep

import cx_Oracle
import psycopg2

class Speedtester:
    def __init__(self, iterations, func):
        self.func = func
        self.iterations= iterations

    @timing.timing
    def show_udfs(self, df, lang):
        # Prepare df
        df = df[["test_text", "test_float", "test_number"]]
        df["udf"] = df["test_id"].map(self.func, lang)  # apply myfunc

        # Show table
        df.show(pretty=True, limit=1)

    def compare_test_cases(self, iteration_index, test_cases):
        times = []

        for s in test_cases:
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
                dataprepper = Data_prep(conn)
                dataprepper.speedtest_prep(iteration_index, self.iterations, 'speedtest')
                # Tell grizzly connection and db-type
                grizzly.use(RelationalExecutor(conn, SQLGenerator(s[1])))
                # create df as table reference
                df = grizzly.read_table("speedtest")
                # execute query and get time for that
                time = self.show_udfs(df, s[3])
                times.append([self.iterations[iteration_index], s[0], time[1]])

        return times

if __name__ == "__main__":
    # Parameters for testing (funtion to compile, testcases with connections, iterations to test)
    func = functions.myfunc2
    test_cases = config.test_cases
    times = []
    test_iterations = []

    for f in range(1, 200):
        if f % 20 == 0:
            test_iterations.append(f)

    speedtester = Speedtester(test_iterations, func)

    try:
        for i,_ in enumerate(test_iterations):
            times += speedtester.compare_test_cases(i, test_cases)
            print("\n")
    except KeyboardInterrupt as e:
        pass
    
    plots.plot(func.__name__, times)