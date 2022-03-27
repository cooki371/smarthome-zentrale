import mysql.connector
import config

db = mysql.connector.connect(
    host=config.database["host"],
    user=config.database["user"],
    password=config.database["password"],
    db=config.database["db"]
)

print(db)