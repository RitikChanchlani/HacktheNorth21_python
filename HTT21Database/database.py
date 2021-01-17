  import mysql.connector

config = {
    'user': 'root',
    'password': 'AuAusLL9fgw3Kkkq',
    'host': '35.202.3.19',
    'database' : 'trial'
}
db = mysql.connector.connect(**config)
cursor = db.cursor()