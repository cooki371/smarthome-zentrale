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

userid = 0

cursor.execute(query.format(userid))

for (iduser, mail, verified) in cursor:
    print("{} {} {}".format(iduser, mail, verified))

cursor.close()
db.close()