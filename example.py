import grizzly
import grizzly.aggregates
from grizzly.dataframes.frame import DataFrame

from grizzly.relationaldbexecutor import RelationalExecutor
from grizzly.sqlgenerator import SQLGenerator

import config
import data_prep
import timing

import psycopg2
import cx_Oracle

def myfunc4(a: int) -> int:
    i: int = 22
    n: float = 22.3
    m: int = a + i
    for i in range(1, a):
        if i + a > 20:
            return 20 * a
        else:
            return 0
            
    return m

def myfunc2(a: int) -> str:
    n: float = 22.3
    g_df1 = grizzly.read_table("events")
    g_df1["actor1name"]
    g_df2 = grizzly.read_table("cool")
    g_df2.generateQuery()
    i: int = 2
    f: str = "hello"
    print(f)
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



import sqlite3
con = sqlite3.connect("grizzly.db")

grizzly.use(RelationalExecutor(con, SQLGenerator('postgresql')))
df_eval = grizzly.read_table("events")
df = grizzly.read_table("events")
df["udf"] = df["test_id"].map(myfunc2, 'sql')
print(df.generateQuery())

to_eval= ['grizzly.use(RelationalExecutor(con, SQLGenerator("sqlite")))', 'df = grizzly.read_table("events")', 'df.generateQuery()']

def evaluate(to_eval):
    _var = ""
    for line in to_eval:
        if "=" in line:
            exec(line)
            _var = line.split("=")[0].replace(" ", "")
        else:
            _df = eval(line)
    return _df, _var

_df, _var = evaluate(to_eval)

if type(_df) == DataFrame:
    _qry = _df.generateQuery()
else:
    _qry = _df

print(f"CURSOR {_var} IS {_qry}")

