import grizzly
import grizzly.aggregates

from grizzly.relationaldbexecutor import RelationalExecutor
from grizzly.sqlgenerator import SQLGenerator

import speedtest.timing as timing

import sqlite3
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
    g_df1 = grizzly.read_table("speedtest")
    g_df1["test_id"]
    for m in g_df1:
        print(m)
    
    i: int = 2
    f: str = "hello"
    return a + i

con = sqlite3.connect("grizzly.db")
con = cx_Oracle.connect(user='demopython', password='orcl_py123', dsn='127.0.0.1/orclpdb')
#con = psycopg2.connect(dbname="postgres", user="post_py", password="post_py_DB123")

grizzly.use(RelationalExecutor(con, SQLGenerator('postgresql')))
df = grizzly.read_table("speedtest")
df["udf"] = df["test_id"].map(myfunc2)
print(df.generateQuery())
df.show(pretty=True)


