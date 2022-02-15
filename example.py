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


## Use of UDF
def myfunc(a: int, b: str) -> str:
      return a+"_grizzly"

grizzly.use(RelationalExecutor(con, SQLGenerator("postgresql")))
df = grizzly.read_table("events")  # load table
#df = df[df.globaleventid == 467268277] # filter it
#df["newid"] = df["globaleventid"].map(myfunc, "py") # apply myfunc

df["newid"] = df["globaleventid"].map(myfunc, "py") # apply myfunc

print("\n")
print(df.generateQuery())
#df.show()

i: int = 5
print(i)