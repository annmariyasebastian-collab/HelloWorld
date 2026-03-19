import connection
cursor = connection.conn.cursor()
sql_update = "UPDATE place SET name='Anna' where id =2"
cursor.execute(sql_update)
connection.conn.commit()
print("Record updated successfully")
cursor.close()