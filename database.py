import mysql.connector

config = {
    'user': 'root',
    'password': 'Password',
    'host': 'localhost',
    'database' : 'final'
}
db = mysql.connector.connect(**config)
cursor = db.cursor()