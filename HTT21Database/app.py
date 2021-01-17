from flask import Flask, jsonify, request
import main
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "<h1>Test</h1>"

@app.route('/createUser', methods=['GET'])
def generate_user():
    return jsonify({'user_id': main.add_user('u')})


@app.route('/add/<key_string>', methods=['GET', 'POST'])
def add_key_amount(key_string):
    user_id = Flask.request.headers['user_id']
    main.add_str(key_string)
    

@app.route('/get/max', methods=['GET'])
def get_max():
    user_id = Flask.request.headers['user_id']
    return jsonify({'max': main.get_max(user_id)})

@app.route('/get/min', methods=['GET'])
def get_min():
    user_id = Flask.request.headers['user_id']
    return jsonify({'min': main.get_min(user_id)})


