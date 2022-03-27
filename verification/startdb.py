import mysql.connector
import databaseconfig as cfg

db = mysql.connector.connect(
    host=cfg.database["host"],
    user=cfg.database["user"],
    password=cfg.database["password"],
    db=cfg.database["db"]
)

print(db)