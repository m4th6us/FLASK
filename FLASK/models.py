import json
from flask import request

class Models:

    def __init__(self):
        self.list_tasks = []

    def index():
        return '''
        <h1>Bem vindo a página inicial da API</h1>\n
        <h2>Caminhos da api:</h2>\n
        <p>/list_all_tasks - lista todas as tarefas presentes na api.</p>\n
        <p>/list_task_id/id - lista as tarefas presentes na api pelo id.</p>\n
        <p>/add_tasks - adiciona tarefas na api.</p>\n
        <p>/delete_task_id/id - lista todas as tarefas presentes na api.</p>\n'''

    def list_all_tasks(self):

        if self.list_tasks != []:
            response = self.list_tasks
        else:
            response = {'mensagem': 'não existem tasks adicione uma atráves do caminho /add_tasks método post'}
        return response


    def list_task_id(self,id):
        
        for itens in self.list_tasks:
            if itens['id'] == id:
                response = itens
                
        return response

    def add_tasks(self):
        
        dados = json.loads(request.data)
        if self.list_tasks:
            dados['id'] = self.list_tasks[-1]['id'] + 1
        else:
            dados['id'] = 0
        self.list_tasks.append(dados)

        return {'status':'sucesso','task adicionada':self.list_tasks[-1]}

    def delete_task_id(self,id):
        if self.list_tasks != []:
            for item in self.list_tasks:
                if str(item['id']) == str(id):
                    self.list_tasks.remove(item)
                    response = self.list_tasks
        else:
            response = {'status':'erro','mensagem':'não existem tarefas na api, adicione uma pelo endpoint /add_tasks'}

        return response

