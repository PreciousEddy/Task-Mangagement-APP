from flask import Flask, request, jsonify, render_template
from appwrite.client import Client
from appwrite.services.account import Account
from appwrite.services.databases import Databases

app = Flask(__name__)

client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1')  # Your Appwrite endpoint
client.set_project('66fb6af40018d78fbbe7')  # Your project ID

account = Account(client)
databases = Databases(client)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    try:
        account.create('unique()', data['email'], data['password'])
        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    try:
        account.create_session(data['email'], data['password'])
        return jsonify({'message': 'Logged in successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    try:
        databases.create_document('66fb6b71003a6832c945', 'tasks', 'unique()', {
            'title': data['title'],
            'description': data['description'],
            'status': False,
            'userId': data['userId']
        })
        return jsonify({'message': 'Task created successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        response = databases.list_documents('66fb6b71003a6832c945', 'tasks')
        return jsonify(response['documents']), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
