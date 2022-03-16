# Python to SQL Compiler
## Using
### Credentials
Add the credentials of your oracle or postgresql db to the config.py file.
### Examples
In the example.py file you can find a projection of an udf on the oracle and postgresql dbs. 
The data that is needed for that insertion is provided by the data_prep module. 
The module creates the Table "speedtest" and inserts a given amount of records into the db.

For compiling the udfs please specify the parameter lang at the .map() function in which language the udf should be translated:
- "sql" for compiling the python udf to PL/SQL or PGPL/SQL
- "py" for creating a functgion with python code on DB (only working on postgresql db with plpython3u enabled)