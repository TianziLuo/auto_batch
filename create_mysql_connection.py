import mysql.connector
from mysql.connector import Error

def create_mysql_connection():
    try:
        print("Creating MySQL connection...")
        connection = mysql.connector.connect(
            host="127.0.0.1",       # Hostname (localhost or 127.0.0.1)
            port=3308,             # Port (3308 as per your setup)
            user="root",           # Username (root)
            password="123456",           # Password (leave empty if no password is set)
        )
        if connection.is_connected():
            print("MySQL connection 'userve' created successfully!")
            return connection
    except Error as e:
        print(f"Error while connecting: {e}")
        return None
    


if __name__ == "__main__":
    create_mysql_connection()