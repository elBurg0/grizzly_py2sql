import grizzly
import grizzly.aggregates
from grizzly.relationaldbexecutor import RelationalExecutor
from grizzly.sqlgenerator import SQLGenerator

import functions
import config

import psycopg2
import cx_Oracle

# Connection to test
conf = config.oracle
# Function to compile and execute
func = functions.myfunc4

# Oracle db
if conf == config.oracle:
    con = cx_Oracle.connect(user=conf['user'], password=conf['password'], dsn=conf['dsn'])
# Postgres local db
elif conf == config.postgres:
    con = psycopg2.connect(dbname=conf['dbname'], user=conf['user'], password=conf['password'])
# Postgres server db
elif conf == config.postgres_server:
    con = psycopg2.connect(dbname=conf['dbname'], user=conf['user'], password=conf['password'], host=conf['host'])


grizzly.use(RelationalExecutor(con, SQLGenerator('oracle')))
df = grizzly.read_table("speedtest")
df = df[["test_id", "test_text", "test_float", "test_number"]]
df["udf"] = df["test_id"].map(func)
print(df.generateQuery())
df.show(pretty=True)