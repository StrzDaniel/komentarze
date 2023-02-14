import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql1 = "CREATE TABLE zamowienia (zamowienie_produkt_id INT(255),product_id INT(255), data_zamowienia DATE)"
sql2 = "CREATE TABLE komenatrze (komentarz_id INT(255),product INT(255), tresc VCHAR(255))"

mycursor.execute(sq1)