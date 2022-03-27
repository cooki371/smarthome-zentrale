import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="dbuser",
    password="dbuserPw",
    db="smarthome"
)

print(db)