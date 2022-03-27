import mysql.connector
import databaseconfig as cfg

db = mysql.connector.connect(
    host=cfg.database["host"],
    user=cfg.database["user"],
    password=cfg.database["password"],
    database=cfg.database["db"]
)

cursor = db.cursor()

query = ("SELECT mail FROM user WHERE iduser={}")

userid = 1

cursor.execute(query.format(userid))

for (mail) in cursor:
    print("{}".format(mail))

cursor.close()
db.close()