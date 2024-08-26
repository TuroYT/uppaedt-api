import mysql.connector
import os

db = mysql.connector.connect(
  host=os.environ.get("DB_HOST"),
  user=os.environ.get("DB_USER"),
  password=os.environ.get("DB_PASS")
)

print(os.environ.get("DB_HOST"))

#