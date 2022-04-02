import config

import psycopg2
import cx_Oracle
import timing

# class for preparing the data in a given database (upload specific amount of datasets)
class Data_prep:
    def __init__(self, con, index, all_iterations):
        # TODO only add new rows to sql
        self.iterations = all_iterations[index]
        self.last_iteration = 0

        self.con = con
        self.c = con.cursor()
    
        
        if index == 0:
            self.drop_table()
            self.create_table()
            self.insert_data(0, self.iterations)
        else:
            self.c.execute("SELECT COUNT(*) FROM speedtest")
            rows = self.c.fetchall()
            # Add none if already in db (mulitple cases on same db)
            if rows[0][0] == self.iterations:
                return
            # Only add new entries
            else:
                self.last_iteration = all_iterations[index-1]
                self.insert_data(self.last_iteration, self.iterations)

    def drop_table(self):
        try:
            self.c.execute('DROP TABLE speedtest')
        except Exception as e:
            print("No Table deleted:", e)

    def create_table(self):
        self.c.execute("""CREATE TABLE speedtest (
                test_id INT,
                test_text VARCHAR(255), 
                test_number INT,
                test_float FLOAT
            )
        """)

    def insert_data(self, start, end):
        rows = []
        rows2 = []

        # Prepare Data for insertion
        for i in range(start, end):
            text = f"'{str(i)}. Entry'"
            rows.append(f"({i}, {text}, {i}, {float(i)})")
            rows2.append((i, text, i, float(i)))

        try:
        # Insert into postgresql db
            values = ", ".join(map(str, rows))
            self.c.execute(f"""
                        INSERT INTO speedtest(
                            test_id,
                            test_text,
                            test_number,
                            test_float
                        )
                        VALUES {values}
                """)

        # Insert into oracle db
        except Exception as e:
            self.c.executemany(
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

        self.con.commit()
        print(f"-- Inserted {self.iterations - self.last_iteration} rows to DB: {self.con.dsn}")