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
    except Exception as err:
    #except (mysql.connector.Error, IOError) as err:
        print("Could not connect to db: ", err)
    
    return None

def select_all(table_name):
    if is_empty_string(table_name):
        return []

    sql = f"SELECT * FROM {table_name};"
    cnx = get_connection()
    result = []

    try:
        if(cnx and cnx.is_connected()):
            with cnx.cursor(dictionary = True) as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
    except Exception as e:
        print(e)
        return []
    finally:
        cnx.close()

    return result

def select(table_name, id_column, id_value):
    if is_empty_string(table_name) or is_empty_string(id_column) or is_empty_string(id_value):
        return {}
    
    sql = f"SELECT * FROM {table_name} WHERE {id_column}={id_value};"
    cnx = get_connection()
    result = {}
    
    try:
        if(cnx and cnx.is_connected()):
            with cnx.cursor(dictionary = True) as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
    except Exception as e:
        print(e)
        return {}
    finally:
        cnx.close()

    return result

def insert(table_name, data):
    if is_empty_string(table_name) or not (data and isinstance(data, dict)):
        return -1
    
    cnx = get_connection()
    result = -1

    print(data)
    
    try:
        if(cnx and cnx.is_connected()):
            with cnx.cursor() as cursor:
                # https://blog.finxter.com/5-best-ways-to-insert-python-dictionaries-into-mysql/
                placeholders = ', '.join(['%s'] * len(data))
                columns = ', '.join(data.keys())
                sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

                cursor.execute(sql, list(data.values()))
                result = cursor.lastrowid
            cnx.commit()
    except Exception as e:
        print(e)
    finally:
        cnx.close()
    
    return result

def update(table_name, id_column, data):
    if is_empty_string(table_name) or is_empty_string(id_column) or not (data and isinstance(data, dict)):
        print("db.update: invalid params")
        return False
    
    id_value = data.pop(id_column, None)
    if(is_empty_string(id_value)):
        print("db.update: id_column not found in data")
        return False
    
    cnx = get_connection()
    
    try:
        if(cnx and cnx.is_connected()):
            with cnx.cursor() as cursor:
                # https://www.codeease.net/programming/python/python-dictionary-to-sql-update
                vals = ', '.join([f"{key} = %s" for key in data.keys()])
                sql = f"UPDATE {table_name} SET {vals} WHERE {id_column} = {id_value}"
                print(sql)
                cursor.execute(sql, list(data.values()))
            cnx.commit()
    except Exception as e:
        print(e)
        return False
    finally:
        cnx.close()
    
    return id_value

def delete(table_name, id_column, id_value):
    if is_empty_string(table_name) or is_empty_string(id_column) or is_empty_string(id_value):
        return False
    
    cnx = get_connection()
    
    try:
        if(cnx and cnx.is_connected()):
            with cnx.cursor() as cursor:
                sql = f"DELETE from {table_name} where {id_column}={id_value};"
                cursor.execute(sql)
            cnx.commit()
    except Exception as e:
        print(e)
        return False
    finally:
        cnx.close()
    
    return True

def create_db():
    print("create_db() called!")
    execute_script("sql/mhs-create-db.sql")

def populate_db():
    print("populate_db() called!")
    execute_script("sql/mhs-populate-db.sql")

def execute_script(file_path):
    cnx = get_connection()

    try:
        if(cnx and cnx.is_connected()):
            cnx.autocommit = True
            
            with cnx.cursor() as cursor:
                with open(file_path) as file:
                    text = file.read().split(";")
                    for query in text:
                        if(query and (not query.isspace())):
                            cursor.execute(query + ";")
    except Exception as e:
        print(e)
    finally:
        cnx.close()
