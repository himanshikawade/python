import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE  if not exists test1")
mycursor.execute("CREATE TABLE  if not exists test1.test_table (c1 INT,c2 VARCHAR(15),c3 int,c4 FLOAT,c5 VARCHAR(10))")
mydb.close()

