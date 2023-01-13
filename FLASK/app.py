from flask import Flask, request
import json


list_tasks = []
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

    if list_tasks != []:
        response = list_tasks
    else:
        response = {'mensagem': 'não existem tasks adicione uma atráves do caminho /add_tasks método post'}
    return response


@app.route('/list_task_id/<int:id>', methods=['GET'])
def list_task_id(id):
    try:
        response = list_tasks[id]
    except IndexError:
        response = {'mensagem': f'id de tarefa {id} não existe'}

    return response

@app.route('/add_tasks', methods=['POST'])
def add_tasks():
    dados = json.loads(request.data)
    if list_tasks:
        dados['id'] = list_tasks[-1]['id'] + 1
    else:
        dados['id'] = 0
    list_tasks.append(dados)

    return {'status':'sucesso','task adicionada':list_tasks[-1]}

@app.route('/delete_task_id/<int:id>', methods=['DELETE'])
def delete_task_id(id):
    if list_tasks != []:
        for item in list_tasks:
            if str(item['id']) == str(id):
                list_tasks.remove(item)
                response = list_tasks
    else:
        response = {'status':'erro','mensagem':'não existem tarefas na api, adicione uma pelo endpoint /add_tasks'}

    return response

    
if __name__ == '__main__':
    app.run(host='192.168.230.24')