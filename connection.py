import mysql.connector

mydb = mysql.connector.connect(
  host="184.179.169.45",
  user="elo_weaker",
  password="weakerPassword"
)

print(mydb)