import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='pass',
)

# Prepare cursor object
cursorObject = dataBase.cursor()

# Create database
cursorObject.execute("CREATE DATABASE dcrm_db")

print("Created database")
