import psycopg2
import cx_Oracle
import timing

def create_table(c):
    # Delete table and create table
    try:
        c.execute('DROP TABLE speedtest')
        #print("Dropped Table")
    except Exception as e:
        print("No Table deleted:", e)
    finally:
        c.execute("""CREATE TABLE speedtest (
            test_id INT,
            test_text VARCHAR(255), 
            test_number INT,
            test_float FLOAT
            )
        """)
        #print("Created Table")

@timing.timing
def insert_data(con, iterations):
    c = con.cursor()
    create_table(c)
    rows = []
    rows2 = []

    # Insert data into table
    for i in range(1,iterations +1):
        text = f"'{str(i)}. Entry'"
        rows.append(f"({i}, {text}, {i}, {float(i)})")
        rows2.append((i, text, i, float(i)))
    
    if "postgres" in con.dsn:
        # Trying to insert into postgresql db
        values = ", ".join(map(str, rows))
        c.execute(f"""
                    INSERT INTO speedtest(
                        test_id,
                        test_text,
                        test_number,
                        test_float
                    )
                    VALUES {values}
            """)

    elif "oracle" in con.dsn:
        # Inserting into oracle db
        c.executemany(
            f"""
                    INSERT INTO speedtest(
                        test_id,
                        test_text,
                        test_number,
                        test_float
                    )
                    VALUES (:test_id, :test_text, :test_number, :test_float)
            """, rows2
        )

    con.commit() 
    print(f"-- Inserted {iterations} rows to DB: {con.dsn}")

def main(iters):
    # Prep postgresql db
    conn = psycopg2.connect(
        dbname="postgres", 
        user="postgres",
        password="post_DB123")
    insert_data(conn, iters)

    # Prep oracle db
    con = cx_Oracle.connect(
        user = "demopython",
        password = "orcl_py123",
        dsn = "localhost/orclpdb",
        encoding="UTF-8")
    insert_data(con, iters)

if __name__ == "__main__":
    main(100)
