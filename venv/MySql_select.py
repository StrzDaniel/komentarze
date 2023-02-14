import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql1 = "SELECT * FROM komenatrze"
sql2="SELECT * FROM Orders WHERE OrderDate='2008-11-11'"

mycursor.execute(sql1)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)