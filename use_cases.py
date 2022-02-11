# load connection
from turtle import begin_fill


con = ...

# load table
table = Table(con, "table")
table = grizzly.read_table("events")


def udf():
    if table.column > 10:
        table.column = 12

UPDATE table
SET table.column = 12
WHERE table.column > 12



def udf():
    if table.column > 10:
        print(table.column)

SELECT table.column
FROM table
WHERE table.column > 10

BEGIN 
    for r in (SELECT * FROM table WHERE table.column > 10)
    loop
        dbms_output.put_line(r.column);
    end loop;
END;


# Bei return auch SQL-Return, aber was? -> Liste, cursor, df

def udf():
