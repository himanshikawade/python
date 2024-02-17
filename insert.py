import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor=mydb.cursor()
mycursor.execute("insert into test1.test_table values(1456,'himanshi',19,45.0,'Kawade')")
mycursor.execute("insert into test1.test_table values(1456,'himanshi',19,45.0,'Kawade')")
mycursor.execute("insert into test1.test_table values(1456,'himanshi',19,45.0,'Kawade')")
mycursor.execute("insert into test1.test_table values(1456,'himanshi',19,45.0,'Kawade')")
mycursor.execute("insert into test1.test_table values(1456,'himanshi',19,45.0,'Kawade')")
mycursor.execute("insert into test1.test_table values(1456,'himanshi',19,45.0,'Kawade')")
mycursor.execute("insert into test1.test_table values(1456,'himanshi',19,45.0,'Kawade')")
mydb.commit()
mydb.close()