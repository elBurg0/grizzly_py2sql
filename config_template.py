oracle = dict(
    user="",
    password="",
    dsn=""
)

postgres = dict(
    dbname="",
    user="",
    password=""
)

postgres_server = dict(
    dbname="",
    user="",
    password="",
    host=""
)

# Format is: display name of testcase, db type, connection dictonary, language to compile to (py only available at postgres db)
test_cases = [
    ["PL/Python - Online Postgres DB", "postgresql", postgres_server, "py"],
    ["PL/SQL - Online Postgres DB", "postgresql",postgres_server, "sql"],
    ["PL/Python - Local Postgres DB", "postgresql",postgres, "py"],
    ["PL/SQL - Local Postgres DB", "postgresql",postgres, "sql"],
    ["PL/SQL - Local Oracle DB", "oracle", oracle, "sql"]
]