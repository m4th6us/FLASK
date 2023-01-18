import json
from flask import request
from back_mongo import Mongo

class Models:

    def __init__(self):
        self.mongo = Mongo()

    def list_all_tasks(self):
        '''
        this function list all tasks in the mongodb
        '''
        data = self.mongo.get_mongo()['documents']
        itens = {}
        lista = []

        for i in data:
            print(i)
            itens = {
                'id': i['id'],
                'task': i['task'],
                'status': i['status']
            }
            lista.append(itens)

        if lista != []:
            response = lista
        else:
            response = []

        return response

    def list_task_id(self,id):
        '''
        this function list the tasks by id
        '''
        
        data = self.mongo.get_mongo()
        response = {'message':f'task id {id} not exists in api'}
        itens = {}
        lista = []

        for i in data['documents']:
            if i['id'] == id:
                itens = {
                    'id': i['id'],
                    'task': i['task'],
                    'status': i['status']
                }
                lista.append(itens)
                response = lista

        return response

    def add_tasks(self):
        '''
        this function add tasks in mongodb cloud and add id auto incremente
        '''
        try:
            data = json.loads(request.data)
            data['id'] = [i['id'] for i in self.mongo.get_mongo()['documents']][-1] + 1

        except:
            data['id'] = 1

        self.mongo.insert_mongo([data])

        response = {'message':f'id record {data["id"]} successfully added'}
        return response

    def update_task(self, id):

        # try:
        data = self.mongo.get_mongo()['documents']
        dados = json.loads(request.data)
        response = {'message': f'task id {id} not exist'}

        for itens in data:
            if itens['id'] == id:
                dados['_id'] = itens['_id']

                self.mongo.update_mongo(dados)
                response = {'message': f'task id {id} update successfully'}
                

        # except IndexError:
        #     response = {'message': 'There are still no records in the api, add one via the /add_tasks endpoint'}
            
        return response
        
    def delete_task_id(self,id):
        '''
        this functions delete tasks in mongodb cloud by id
        '''
        response = {'message': 'There are still no records in the api, add one via the /add_tasks endpoint'}

        try:
            data = self.mongo.get_mongo()['documents']
            for itens in data:
                if itens['id'] == id:
                    response = {'message': f'task id {id} deleted successfully'}
                    self.mongo.delete_mongo(itens['_id'])
        except:
            response = {'message': f'task id {id} not exist'}

        return response
