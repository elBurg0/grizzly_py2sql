import random

# class for preparing the data in a given database (upload specific amount of datasets)
class Data_prep:
    def __init__(self, con):
        self.con = con
        self.c = con.cursor()
    
    # specific method to prepare data for the speedtest (checks whether there is already testdata that can be used)
    def speedtest_prep(self, index, all_iterations, table_name):
        number_of_tuples = all_iterations[index]

        if index == 0:
            self.create_test_table(table_name)
            self.insert_test_data(table_name, 0, number_of_tuples)
        else:
            self.c.execute(f"SELECT COUNT(*) FROM {table_name}")
            rows = self.c.fetchall()
            # Add none if already in db (mulitple cases on same db)
            if rows[0][0] == number_of_tuples:
                return
            # Only add new entries
            else:
                last_iteration_tupel = all_iterations[index-1]
                self.insert_test_data(table_name, last_iteration_tupel, number_of_tuples)

    # Method to drop a table with a specified name
    def drop_test_table(self, table_name):
        try:
            self.c.execute(f'DROP TABLE {table_name}')
        except Exception as e:
            print("No Table deleted:", e)

    # Method to create a table with predefined columns (test_id, test_text, test_number, test_float)
    def create_test_table(self, table_name):
        self.drop_test_table(table_name)
        self.c.execute(f"""CREATE TABLE {table_name} (
                test_id INT,
                test_text VARCHAR(255), 
                test_number INT,
                test_float FLOAT
            )
        """)

    # Method to insert data in the testtable
    def insert_test_data(self, table_name, start = 0, end = 200):
        rows = []
        rows2 = []

        # Prepare Data for insertion
        for i in range(start, end):
            text = f"'{str(i)}. Entry'"
            rows.append(f"({i}, {text}, {random.randint(0, 50)}, {random.uniform(0, 50)})")
            rows2.append((i, text, random.randint(0, 50), random.uniform(0, 50)))

        try:
        # Insert into postgresql db
            values = ", ".join(map(str, rows))
            self.c.execute(f"""
                        INSERT INTO {table_name}(
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
                        INSERT INTO {table_name}(
                            test_id,
                            test_text,
                            test_number,
                            test_float
                            )
                        VALUES (:test_id, :test_text, :test_number, :test_float)
                """, rows2
            )

        self.con.commit()
        #print(f"-- Inserted {end - start} rows to DB: {self.con.dsn}:{table_name}")