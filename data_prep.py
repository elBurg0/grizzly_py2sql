import config

import psycopg2
import cx_Oracle
import timing


def create_table(c):
    # Delete table and create table
    try:
        c.execute('DROP TABLE speedtest')
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


@timing.timing
def insert_data(con, iterations):
    c = con.cursor()
    create_table(c)
    rows = []
    rows2 = []

    # Prepare Data for insertion
    for i in range(1, iterations + 1):
        text = f"'{str(i)}. Entry'"
        rows.append(f"({i}, {text}, {i}, {float(i)})")
        rows2.append((i, text, i, float(i)))

    # Insert into postgresql db
    if "postgres" in con.dsn:
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

    # Insert into oracle db
    elif "orcl" in con.dsn:
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
        dbname=config.postgres['dbname'],
        user=config.postgres['user'],
        password=config.postgres['password'])
    insert_data(conn, iters)

    # Prep oracle db
    con = cx_Oracle.connect(
        user=config.oracle['user'],
        password=config.oracle['password'],
        dsn=config.oracle['dsn'])
    insert_data(con, iters)


if __name__ == "__main__":
    main(100)
