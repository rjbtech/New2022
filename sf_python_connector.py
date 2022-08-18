
# pip install snowflake-connector-python
# pip install sqlalchemy

import snowflake.connector
import snowflake.sqlalchemy
import pandas as pd


def snow_connect():
    # Snow Connection string
    snowconnect = snowflake.connector.connect(
        user="username for snowflake",
        password="Password for snowflake",
        account=‘account locater’,
        region = 'us-east-1',
        Role='ACCOUNTADMIN',
        Warehouse='COMPUTE_WH' 
        )
    return snowconnect