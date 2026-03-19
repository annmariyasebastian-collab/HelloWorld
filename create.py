import connection
cursor = connection.conn.cursor()
cursor.execute("DROP TABLE IF EXISTS place;")
print("Old table dropped successfully")
sql_create = """
CREATE TABLE place (
    id INT,
    name VARCHAR(20),
    age INT
)
"""
cursor.execute(sql_create)
print("Table created successfully")