import os
from sshtunnel import SSHTunnelForwarder
import mysql.connector
import printing as p

from dotenv import load_dotenv
load_dotenv(dotenv_path="Programacion\db_access.env")

ssh_config = {
   'ssh_address_or_host': os.getenv("SSH_HOST"),
   'ssh_username': os.getenv("SSH_USERNAME"),
   'ssh_pkey': os.getenv("SSH_PRIVATE_KEY"),
   'remote_bind_address': ("localhost", 3306)
}

db_config = {
    'user': os.getenv("DB_USER"),
    'password': '',
    'database': 'seven_and_half'
}

def execute_query_in_db(query):
    # Conectarse a la BBDD
    with SSHTunnelForwarder(**ssh_config) as tunnel:
        connection = mysql.connector.connect(host="127.0.0.1", port=tunnel.local_bind_port, **db_config)
        cursor = connection.cursor()

    # Ejecutar la query
        cursor.execute(query)
        results = cursor.fetchall()
    
    # Desconectarse de la BBDD
        cursor.close()
        connection.close()
        return results

def insert_dict_into_db_table(dict, table):
    key_list = list(dict.keys())
    value_list = list(dict.values())
    query = f"INSERT INTO {table} ({", ".join(key_list)}) VALUES ({", ".join(value_list)})"
    execute_query_in_db(query)

def delete_player_from_db(player_id):
    query = f"DELETE FROM "
