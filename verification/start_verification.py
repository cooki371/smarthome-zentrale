from verification import databaseconfig as dbcfg

cursor = dbcfg.db.cursor()


def startVerify(mail):
    cursor.execute("SELECT iduser FROM user WHERE mail = '{}'".format(mail))

    if cursor is None:
        cursor.execute("INSERT INTO user (mail) VALUES ('{}')".format(mail))

        cursor.execute("SELECT iduser FROM user WHERE mail = '{}'".format(mail))
        for userid in cursor:
            iduser = userid

        cursor.execute("INSERT INTO verificaton(iduser, verificationhash) VALUES ({}, 'xxx') ".format(iduser))
