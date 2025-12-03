import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Reyansh@123",
        database="sms"
    )
    return conn