from flask import Flask, jsonify
import main

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Test</h1>"

@app.route('/create/user', methods=['GET'])
def generate_user():
    return jsonify({'id': main.add_user('u')})


@app.route('/add/<key_string>')
def add_key_amount(key_string):
    user_id = Flask.request.headers['user_id']

@app.route('/')
