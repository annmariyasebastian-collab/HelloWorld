import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="world"
)

print("Connected successfully")