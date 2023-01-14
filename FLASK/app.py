from flask import Flask
from models import Models

functions = Models()

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Bem vindo a página inicial da API</h1>\n
    <h2>Caminhos da api:</h2>\n
    <p>/list_all_tasks - lista todas as tarefas presentes na api.</p>\n
    <p>/list_task_id/id - lista as tarefas presentes na api pelo id.</p>\n
    <p>/add_tasks - adiciona tarefas na api.</p>\n
    <p>/delete_task_id/id - lista todas as tarefas presentes na api.</p>\n'''

@app.route('/list_all_tasks', methods=['GET'])
def list_all_tasks():
    return functions.list_all_tasks()


@app.route('/list_task_id/<int:id>', methods=['GET'])
def list_task_id(id):
    try:
        return functions.list_task_id(id)
    except:
        return {'mensagem':f'a task de id {id} não existe!'}

@app.route('/add_tasks', methods=['POST'])
def add_tasks():
    return functions.add_tasks()

@app.route('/delete_task_id', methods=['DELETE'])
def delete_task_id():
    return functions.delete_task_id()

    
if __name__ == '__main__':
    app.run(debug=True)