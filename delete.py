import connection
cursor = connection.conn.cursor()
sql = "delete from place where name='Anna' "
cursor.execute(sql)
connection.conn.commit()
print(" delete successfully")
cursor.close()