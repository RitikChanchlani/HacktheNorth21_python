from flask import Flask, jsonify, request
import json 
from flask_cors import CORS
from flask_mysqldb import MySQL 

app = Flask(__name__)

app.config['MYSQL_USER'] = 'xinyanglu66'
app.config['MYSQL_PASSWORD'] = 'keybored2021'
app.config['MYSQL_HOST'] = 'xinyanglu66.mysql.pythonanywhere-services.com'
app.config['MYSQL_DB'] = 'xinyanglu66$keybored'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

CORS(app)
mysql = MySQL(app)

digits = ['Zero','one','two','three','four','five','six','seven','eight','nine']

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM logs''')
    results = cur.fetchall()
    return jsonify(results)

@app.route('/createUser', methods=['GET'])
def generate_user():
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute('''INSERT INTO logs VALUES (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)''')
    conn.commit()

    return jsonify({'user_id': cur.lastrowid})


@app.route('/add', methods=['GET', 'POST'])
def add_key_amount():
    conn = mysql.connection
    cur = conn.cursor()
    data = json.loads(request.data)
    user_id = data['user_id']
    key = data['keystroke']
    if(key>47 and key<58):
        key = digits[int(chr(key))]
    elif(key>64 and key<91):
        key = chr(key).lower()
    else:
        return('',204)
    cur.execute(f'UPDATE logs SET {key}={key}+1 WHERE id={user_id}')
    conn.commit()

    return ('',204)

@app.route('/get/all', methods=['GET', 'POST'])
def get_all():
    conn = mysql.connection
    cur = conn.cursor()

    data = json.loads(request.data)
    user_id = data['user_id']
    cur.execute(f'SELECT * FROM logs WHERE id={user_id}')
    results = cur.fetchone()
    max=''
    maxVal=0
    total=0
    min = ''
    minVal= float('inf')
    for key in results:
        value = results[key]
        if key == 'id' or key == 'user':
            continue
        if value>maxVal:
            max = key
            maxVal = value
        elif value<minVal:
            min = key
            minVal = value
        total+=value
    results['min'] = min
    results['max'] = max
    results['total']= total
    return jsonify(results)