import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="dbuser",
    password="dbuserPW"
)


print(db)