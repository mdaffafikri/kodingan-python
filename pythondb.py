import mysql.connector

pariabeldatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "test_python"
)

cursor= pariabeldatabase.cursor()
#cursor.execute("DESC table1")
#cursor.execute("SHOW TABLES")
#print(cursor.fetchall())

values_nama = input("Nama = ")
values_alamat = input("Alamat = ")
query = "INSERT INTO table1 (nama, alamat) VALUES (%s, %s)"
values = (values_nama, values_alamat)

cursor.execute(query, values)

pariabeldatabase.commit()

print(cursor.rowcount, "record inserted!!")

