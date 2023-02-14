import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql1 = "INSERT INTO zamowienia (zamowienie_produkt_id, product_id, data_zamowienia) VALUES (1,11,2022-01-01)"
sql2 = "INSERT INTO komenatrze (komentarz_id, product, tresc) VALUES (1,11,' fantastyczna jakos produktu')"
mycursor.execute(sql)



mydb.commit()

print(mycursor.rowcount, "record inserted.")