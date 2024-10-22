import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',  # Cambia por tu host de MySQL
        user='root',  # Cambia por tu usuario de MySQL
        password='',  # Cambia por tu contraseña de MySQL
        database='clase12'  # Cambia por tu base de datos
    )
    return conn
