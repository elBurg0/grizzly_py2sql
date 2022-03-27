oracle = dict(
    user="",
    password="",
    dsn="localhost/orclpdb"
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

test_cases = [
    ["PL/Python - Online Postgres DB", "postgresql", postgres_server, "py"],
    ["PL/SQL - Online Postgres DB", "postgresql",postgres_server, "sql"],
    ["PL/Python - Local Postgres DB", "postgresql",postgres, "py"],
    ["PL/SQL - Local Postgres DB", "postgresql",postgres, "sql"],
    ["PL/SQL - Local Oracle DB", "oracle", oracle, "sql"]
]