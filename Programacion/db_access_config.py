import os
from sshtunnel import SSHTunnelForwarder
import paramiko
import mysql.connector

from dotenv import load_dotenv
load_dotenv(dotenv_path="Programacion\db_access.env")

ssh_config = {
   'ssh_address_or_host': os.getenv("SSH_HOST"),
   'ssh_username': os.getenv("SSH_USERNAME"),
   'ssh_pkey': os.getenv("SSH_PRIVATE_KEY"),
   'remote_bind_address': ("localhost", 3306)
}

print(ssh_config["ssh_pkey"])

db_config = {
    'user': os.getenv("DB_USER"),
    'password': '',
    'database': 'seven_and_half'
}

def connect_to_db():
    global connection, cursor
    with SSHTunnelForwarder(**ssh_config) as tunnel:
        connection = mysql.connector.connect(host="127.0.0.1", port=tunnel.local_bind_port, **db_config)
        cursor = connection.cursor()

        print("Connected to:", cursor.fetchone()) # Comprobación debug

connect_to_db()

def disconnect_from_db():
    cursor.close()
    connection.close()

def query_to_database(query):
    connect_to_db()
    pass
    disconnect_from_db()

def insert_dict_into_db_table(dict, table):
    connect_to_db()
    pass
    disconnect_from_db()

def delete_player_from_db(player_id):
    connect_to_db()
    pass
    disconnect_from_db()