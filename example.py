import grizzly
import grizzly.aggregates

import config

from grizzly.relationaldbexecutor import RelationalExecutor
from grizzly.sqlgenerator import SQLGenerator

import data_prep
import timing

import psycopg2
import cx_Oracle


def myfunc1(a: int) -> int:
    i: int = 12
    m: int = a + i
    for i in range(1, a):
        if i + a > 10:
            return 10 * a
        elif a > 1:
            m: int = a
        else:
            return 0

        f: int = f + a

    return m


def myfunc2(a: int) -> str:
    i: int = 2
    f: str = "hello"
    return a + "_grizzly"


@timing.timing
def show_udfs(df):
    df = df[["test_text", "test_float", "test_number"]]
    df["udf"] = df["test_id"].map(myfunc2, "sql")  # apply myfunc

    print("----------------------------------------")
    print(df.generateQuery())
    print("----------------------------------------")

    df.show(pretty=True, limit=20)
    print("----------------------------------------")


def main():
    print("\n", end="")
    entries = 100

    # POSTGRESQL
    print("Postgresql test:")
    with psycopg2.connect(dbname=config.postgres['dbname'], user=config.postgres['user'], password=config.postgres['password'], keepalives=1) as conn:
        data_prep.insert_data(conn, entries)
        grizzly.use(RelationalExecutor(conn, SQLGenerator("postgresql")))
        df = grizzly.read_table("speedtest")
        show_udfs(df)

    # ORACLE PL/SQL
    print("\nOracle test:")
    with cx_Oracle.connect(user=config.oracle['user'], password=config.oracle['password'], dsn=config.oracle['dsn']) as connection:
        data_prep.insert_data(connection, entries)
        grizzly.use(RelationalExecutor(connection, SQLGenerator("oracle")))
        df = grizzly.read_table("speedtest")  # load table
        show_udfs(df)


if __name__ == "__main__":
    main()
