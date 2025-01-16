import os

ssh_config = {
   'ssh_address_or_host': os.getenv("SSH_HOST"),
   'ssh_username': os.getenv("SSH_USERNAME"),
   'ssh_pkey': "private_key.pem",
   'remote_bind_address': ("localhost", 3306)
}

db_config = {
    'user': os.getenv("DB_USER"),
    'password': '',
    'database': 'seven_and_half'
}