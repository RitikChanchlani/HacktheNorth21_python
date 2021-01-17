from flask import Flask
import main

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Test</h1>"

@app.route('/create/user', methods=['GET'])
def generate_user(){
    return jsonify({'id': main.add_user('u')})
}