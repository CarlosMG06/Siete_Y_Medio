import os
from sshtunnel import SSHTunnelForwarder
import mysql.connector
import datetime

from dotenv import load_dotenv
load_dotenv(dotenv_path="db_access.env")

ssh_config = {
   'ssh_address_or_host': os.getenv("SSH_HOST"),
   'ssh_username': os.getenv("SSH_USERNAME"),
   'ssh_pkey': os.getenv("SSH_PRIVATE_KEY"),
   'remote_bind_address': (os.getenv("SSH_HOST"), 3306)
}

db_config = {
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'database': os.getenv("DB_NAME")
}

def execute_transaction_in_db(transaction, one=False, DML=False):
    """
    Ejecutamos una transacción en la base de datos, haciendo commit solo al acabar con éxito
    :param transaction: (str, list[str]) -> una query o lista de queries
    :param one: (bool = False) -> si la transacción devuelve un solo dato, p.ej. "SELECT now();"
    :param DML: (bool = False) -> si la transacción modifica tablas en vez de seleccionar datos  
    :return: None | list[tuple] | list[list[tuple]] | Any
    """    
    # Conectarse a la BBDD
    with SSHTunnelForwarder(**ssh_config) as tunnel:
        connection = mysql.connector.connect(user=db_config["user"],passwd=db_config["password"],db=db_config["database"],host=ssh_config["ssh_address_or_host"],port=ssh_config["remote_bind_address"][1])
        cursor = connection.cursor()

        try:
            # Ejecutar las queries de la transacción
            if type(transaction) == str: 
                cursor.execute(transaction)
                results = cursor.fetchone()[0] if one else cursor.fetchall()
            else:
                results = []
                for query in transaction:
                    cursor.execute(query)
                    results.append(cursor.fetchall())

            # Confirmar modificaciones de tabla
            if DML: connection.commit()
        except Exception as e:
            # Revertir cambios en caso de error
            connection.rollback()
            print(f"There was an error with the following transaction: {transaction}\n")
            raise e
        finally:
            # Desconectarse de la BBDD
            cursor.close()
            connection.close()
            if not DML: return results

def insert_query(data, table):
    """
    Devuelve la INSERT INTO query correspondiente
    :param data: (dict, list[dict]) -> una fila o lista de filas de datos
    :param table: (str) -> tabla en la que se deben insertar los datos 
    :return: str
    """    
    if type(data) == dict:
        query = f"""INSERT INTO {table} ({', '.join(data.keys())}) 
        VALUES ({', '.join(f"'{v}'" if type(v) in (str, datetime.datetime) else str(v) for v in data.values())});"""
    else:
        query = f"INSERT INTO {table} ({', '.join(data[0].keys())}) VALUES "
        for i, row in enumerate(data):
            data[i] = f"({', '.join(f"'{v}'" if type(v) in (str, datetime.datetime) else str(v) for v in row.values())})"
        query += f"{', '.join(data)};"
    return query