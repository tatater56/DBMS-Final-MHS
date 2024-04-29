from mysql.connector import connect
from mysql.connector.connection import MySQLConnection

from typing import Optional

_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "mhs"
}

def get_connection() -> Optional[MySQLConnection]:
    try:
        return connect(**_config)
    except (mysql.connector.Error, IOError) as err:
        print("Could not connect to db: ", err)
    
    return None

def create_db():
    print("create_db() called!")
    execute_script("sql\mhs-create-db.sql")

def populate_db():
    print("populate_db() called!")
    execute_script("sql\mhs-populate-db.sql")

def execute_script(file_path):
    cnx = get_connection()

    if(cnx and cnx.is_connected()):
        cnx.autocommit = True
        
        with cnx.cursor() as cursor:
            with open(file_path) as file:
                text = file.read().split(";")
                for query in text:
                    if(query and (not query.isspace())):
                        cursor.execute(query + ";")
