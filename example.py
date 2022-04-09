import grizzly
import grizzly.aggregates

from grizzly.relationaldbexecutor import RelationalExecutor
from grizzly.sqlgenerator import SQLGenerator

import functions

import sqlite3
import psycopg2
import cx_Oracle

# SQLite db
#con = sqlite3.connect("grizzly.db")

# Oracle pluggable db
#con = cx_Oracle.connect(user='demopython', password='orcl_py123', dsn='127.0.0.1/orclpdb')

# Oracle db
con = cx_Oracle.connect(user='demopython', password='orcl2_py123', dsn='orcl2')

#Postgresql db
#con = psycopg2.connect(dbname="postgres", user="post_py", password="post_py_DB123")


grizzly.use(RelationalExecutor(con, SQLGenerator('oracle')))
df = grizzly.read_table("speedtest")
df = df[["test_id", "test_text", "test_float", "test_number"]]
df["udf"] = df["test_id"].map(functions.myfunc3)
print(df.generateQuery())
df.show(pretty=True)