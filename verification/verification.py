import hashlib

# from verification import databaseconfig as dbcfg
#
# cursor = dbcfg.db.cursor()
#
#
# def startVerify(mail):
#     cursor.execute("SELECT iduser FROM user WHERE mail = '{}'".format(mail))
#
#     if cursor is None:
#         cursor.execute("INSERT INTO user (mail) VALUES ({})".format(mail))
#
#         cursor.execute("SELECT iduser FROM user WHERE mail = '{}'".format(mail))
#         for userid in cursor:
#             iduser = userid
#
#         cursor.execute("INSERT INTO verificaton(iduser, verificationhash) VALUES ({}, 'xxx') ".format(iduser))
import random


def startVerify(mail):
    f = open('C:/Users/Christopher Nass/Desktop/Python Verification/'+mail+'.txt', 'w')
    hashed = hashlib.sha256(bytes(mail+str(random.randrange(0,999,1)), 'UTF-8')).hexdigest()
    print(hashed)
    f.write(hashed)
