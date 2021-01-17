from flask import Flask, jsonify, request
import main
import json 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "<h1>Test</h1>"

@app.route('/createUser', methods=['GET'])
def generate_user():
    return jsonify({'user_id': main.add_user('u')})


@app.route('/add', methods=['GET', 'POST'])
def add_key_amount():
    data = json.loads(request.data)
    user_id = data['user_id']
    key_string = data['keystrokes']
    main.add_list(user_id, key_string)
    return jsonify({"":""})

@app.route('/get/all', methods=['GET', 'POST'])
def get_all():
    data = json.loads(request.data)
    user_id = data['user_id']
    return jsonify(main.get_data(user_id))




