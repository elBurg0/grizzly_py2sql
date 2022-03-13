import grizzly
import grizzly.aggregates
import sqlite3

from grizzly.relationaldbexecutor import RelationalExecutor
from grizzly.sqlgenerator import SQLGenerator

def myfunc2(a: int) -> str:
      i: int = 12
      f: float = 3
      m: int = 3 + a
      g: str = m + "_functioned"

      return g


import cx_Oracle

connection = None
try:
      connection = cx_Oracle.connect(
        user = "demopython",
        password = "orcl_py123",
        dsn = "localhost/orclpdb",
        encoding="UTF-8")
      
      grizzly.use(RelationalExecutor(connection, SQLGenerator("postgresql")))
      df = grizzly.read_table("todoitem")  # load table
      #df = df[df.globaleventid == 467268277] # filter it

      df = df[["id", "description"]]
      df["gefunctioned"] = df["id"].map(myfunc2, "sql") # apply myfunc

      print("----------------------------------------")
      print(df.generateQuery())
      print("----------------------------------------")

      df.show(pretty=True)

except cx_Oracle.Error as error:
    print("Error -", error)
finally:
    # release the connection
    if connection:
        connection.close()

