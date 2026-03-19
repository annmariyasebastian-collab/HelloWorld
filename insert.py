import connection
cursor = connection.conn.cursor()
sql_create = """
CREATE TABLE IF NOT EXISTS place (
    id INT,
    name VARCHAR(20),
    age INT
)
"""
cursor.execute(sql_create)
print("Table checked/created successfully")
sql_insert = "INSERT INTO place (id, name, age) VALUES (%s, %s, %s)"
values_list = [
    (1, 'Ann', 20),
    (2, 'Maria', 20),]
cursor.executemany(sql_insert, values_list)
connection.conn.commit()
print("Multiple records inserted successfully")