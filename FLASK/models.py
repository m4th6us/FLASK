import json
from flask import request
from connect_to_mongo import Mongo

class Models:

    def __init__(self):
        self.mongo = Mongo()
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

        if self.mongo.get_mongo() != []:
            response = self.mongo.get_mongo()
        else:
            response = {'mensagem': 'não existem tasks adicione uma atráves do caminho /add_tasks método post'}
        return response


    def list_task_id(self,id):

        for itens in self.mongo.get_mongo()['documents']:
            if str(itens['id']) == str(id):
                response = itens

        return response

    def add_tasks(self):

        dados = json.loads(request.data)
        try:
            dados['id'] = [itens['id'] for itens in self.mongo.get_mongo()['documents']][-1] + 1
        except IndexError:
            dados['id'] = 1

        self.mongo.insert_mongo([dados])
        return {'task':self.mongo.get_mongo()['documents'][-1], 'mensagem':'inserida no MongoCloud'}

    def delete_task_id(self):
        response =self.mongo.delete_mongo(self.mongo.get_mongo())

        return response
