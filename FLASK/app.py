from flask import Flask, request
from models import Models
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import json
from datetime import timedelta
from jwt.exceptions import ExpiredSignatureError
from threading import Lock

functions = Models()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '1234'
jwt = JWTManager(app)

add_lock = Lock()

@app.route('/login', methods=['POST'])
def login():
    authentication = json.loads(request.data)

    if authentication['user'] != 'matheus' or authentication['pass'] != 1234:
        response = {'error':'user not exists'}
    else:
        access_token = create_access_token(identity=authentication['user'], expires_delta=timedelta(seconds=60))
        response = access_token
    return {'access_token':response}

@app.route('/')
def index():
    try:
        return '''
        <h1>Bem vindo a página inicial da API</h1>\n
        <h2>Caminhos da api:</h2>\n
        <p>/list_all_tasks - lista todas as tarefas presentes na api.</p>\n
        <p>/list_task_id/id - lista as tarefas presentes na api pelo id.</p>\n
        <p>/add_tasks - adiciona tarefas na api.</p>\n
        <p>/update_task_id/id - altera o valor das tarefas existentes.</p>\n
        <p>/delete_task_id/id - lista todas as tarefas presentes na api.</p>\n'''
    except ExpiredSignatureError:
        return {'message': 'token expirated'}


@app.route('/list_all_tasks', methods=['GET'])
@jwt_required()
def list_all_tasks():
    try:
        return functions.list_all_tasks()
    except ExpiredSignatureError:
        return {'message': 'token expirated'}

@app.route('/list_task_id/<int:id>', methods=['GET'])
@jwt_required()
def list_task_id(id):
    try:
        return functions.list_task_id(id)
    except ExpiredSignatureError:
        return {'message': 'token expirated'}

@app.route('/add_tasks', methods=['POST'])
@jwt_required()
def add_tasks():
    try:
        add_lock.acquire()
        response = functions.add_tasks()
        return response

    except ExpiredSignatureError:
        return {'message': 'token expirated'}
    
    finally:
        add_lock.release()

@app.route('/update_task_id/<int:id>', methods=['PUT'])
@jwt_required()
def update_task_id(id):
    try:
        return functions.update_task(id)
    except ExpiredSignatureError:
        return {'message': 'token expirated'}

@app.route('/delete_task_id/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_task_id(id):
    try:
        return functions.delete_task_id(id)
    except ExpiredSignatureError:
        return {'message': 'token expirated'}
    
if __name__ == '__main__':
    app.run(host='192.168.229.19', debug=True)