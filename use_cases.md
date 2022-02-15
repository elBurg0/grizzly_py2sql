# load connection
from ast import Is
from asyncio import WriteTransport
from socket import TIPC_DEST_DROPPABLE
from turtle import begin_fill


con = ...

# load table
table = Table(con, "table")
table = grizzly.read_table("events")





# Update specific rows
def udf():
    if table.column > 10:
        table.column = 12
udf()

UPDATE table
SET table.column = 12
WHERE table.column > 10





# Update specific rows with specific value
def udf(a: int):
    if table.column > 10:
        table.column = a
udf(5)

UPDATE table
SET table.column = 5
WHERE table.column > 10





# delete rows
def udf(a: str):
    if table.column == a:
        table.drop_row()
udf("hello")

DELETE FROM table
WHERE table.column = "hello"






# Change data
def udf(values: str):
    table.column = values
udf("hello")

UPDATE table
SET table.column = "hello"





# Print rows (columns) with rstrictions on row
def udf():
    if table.column > 10:
        print(table.column)
udf()

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

# project udf to column
def udf(a: int, b:int) -> int:
    return a *b
new_col = udf(table.column, 3)
table.new_column = udf(table.column, 3)
table["new column"] = table.column.map(udf(3))

CREATE OR REPLACE FUNCTION udf(a IN number, b IN NUMBER)
    RETURN NUMBER IS 
BEGIN 
RETRUN a * b;
END;

SELECT udf(table.column, 3)
FROM table




def udf():
    for r in table:
        if r.column3 == True:
            m = r.column1 + (r.column2 * 30):
        else:
            m = r.column1 + (r.column2 * 10):
        r.column = m
        print(r.column)

UPDATE table
SET table.column = CASE table.column3
    WHEN table.column3 = True THEN table.column1 + (table.column2 * 30)
    WHEN table.column3 = False THEN table.column1 + (table.column2 * 10)




# Factorial:
def udf(i):
    f = 0
    if i == 0:
        f = 1
    else:
        f = i * udf(i - 1)
    return f
udf(5)

CREATE OR REPLACE FUNCTION udf(i number)
RETURN NUMBER
IS
    f number = 0;
BEGIN
    IF i = 0 THEN
        f := 1;
    ELSE
        f := i * udf(i - 1);
    END IF;
RETURN f;
END;

BEGIN
dbms_output.put_line(udf(30));
END;





## Eher so:
# Deklarationen:
i: int = 5  # oder type checken
i number := 5;
i number(5) := 5;
i number(5) DEFAULT 5;
i number(5) NOT NULL := 5;


# Operatoren
=
<>, ~=, !=, ^=
< 
> 
<
>=

.empty()
IS NULL
IS NOT NULL

LIKE '%' und '_'
NOT LIKE
BETWEEN         Kurzschreibweise für <= und >=
IN

# IF-Anweisungen:
if a == 5:
    ...
elif a == 6:
    ...
else:
    ...

if a = 5 then
    ...
elsif a = 6 then
    ...
else
    ...
end if;


# Schleifen:
for i in range(1,10):
FOR i IN 1 .. 10 loop
END loop

while x < 10:
While X < 11 Loop
End Loop;

while True:
    if x > 10:
        break
Loop
EXIT WHEN x > 10;
End Loop;


# Ausgaben
print()
set serveroutput on
dbms.put_line()

