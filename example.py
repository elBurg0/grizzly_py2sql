import grizzly
import grizzly.aggregates
import sqlite3

from grizzly.relationaldbexecutor import RelationalExecutor
from grizzly.sqlgenerator import SQLGenerator

con = sqlite3.connect("grizzly.db")

grizzly.use(RelationalExecutor(con))


# Projection
df = grizzly.read_table("events")

df = df[df["globaleventid"] == 470747760] # filter
df = df[["actor1name","actor2name"]]
df.show(pretty=True)

print("----------------------------------------")

# Joins
df1 = grizzly.read_table("t1")
df2 = grizzly.read_table("t2")

j  = df1.join(df2, on = (df1.actor1name == df2.actor2name) | (df1["actor1countrycode"] <= df2["actor2countrycode"]), how="left outer")
#print(j.generate())
#cnt = j.count()
#print(f"join result contais {cnt} elments")

#print("----------------------------------------")

# Count
df = grizzly.read_table("events")
print(df.count("actor2name"))

print("----------------------------------------")

# Aggregation
from grizzly.aggregates import AggregateType
df = grizzly.read_table("events")
g = df.groupby(["theyear","actor1name"])

a = g.agg(col="actor2name", aggType=AggregateType.COUNT)
a.show(pretty=True)

print("----------------------------------------")
print("\n")


def myfunc2(a: str) -> str:
      return a + "grizzly"


import cx_Oracle

connection = None
try:
      connection = cx_Oracle.connect(
        user = "demopython",
        password = "orcl_py123",
        dsn = "localhost/orclpdb",
        encoding="UTF-8")

      # show the version of the Oracle Database
      print(connection.version)

      c = connection.cursor()

      c.execute("""
            SELECT *
            FROM todoitem
      """)

      rows = c.fetchall()


      # Now query the rows back
      for row in c.execute('select description, done from todoitem'):
            if (row[1]):
                  print(row[0], "is done")
            else:
                  print(row[0], "is NOT done")

      grizzly.use(RelationalExecutor(connection, SQLGenerator("postgresql")))
      df = grizzly.read_table("todoitem")  # load table
      #df = df[df.globaleventid == 467268277] # filter it

      df = df[["id" , "description"]]
      df["gefunctioned"] = df["description"].map(myfunc2, "sql") # apply myfunc

      print("\n")

      df.show(pretty=True)

except cx_Oracle.Error as error:
    print("Error -", error)
finally:
    # release the connection
    if connection:
        connection.close()

