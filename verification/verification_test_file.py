import mysql.connector
import databaseconfig as cfg
import startdb as db

cursor = db.db.cursor()

query = ("SELECT mail, iduser FROM user WHERE iduser>={}")

userid = 1

cursor.execute(query.format(userid))

for (mail,userid) in cursor:
    print("Die Mail von User {} ist {}".format(userid, mail))

cursor.close()
