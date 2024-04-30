from mysql.connector import connect
from mysql.connector.connection import MySQLConnection

from typing import Optional

from util import is_empty_string

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

def select_all(table_name):
    if is_empty_string(table_name):
        return []

    sql = "select * from %s;" % table_name
    cnx = get_connection()
    result = []

    if(cnx and cnx.is_connected()):
        with cnx.cursor(dictionary = True) as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
    cnx.close()

    return result

def select(table_name, id_column, id_value):
    if is_empty_string(table_name) or is_empty_string(id_column) or is_empty_string(id_value):
        return {}
    
    sql = "select * from %s where %s=%s;" % (table_name, id_column, id_value)
    cnx = get_connection()
    result = {}

    if(cnx and cnx.is_connected()):
        with cnx.cursor(dictionary = True) as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()
    cnx.close()

    return result


def create_db():
    print("create_db() called!")
    execute_script("sql/mhs-create-db.sql")

def populate_db():
    print("populate_db() called!")
    execute_script("sql/mhs-populate-db.sql")

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
    
    cnx.close()
