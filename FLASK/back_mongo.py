import requests
import json


class Mongo:

    def __init__(self):

        self.header = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': '05LPPayQoWsQHaWixmLztL60PWG5fKJZ5chkYAp8lqTvUCtvQrNxz9BAJ8aPNZmh', 
        }

    def get_mongo(self):
        '''
        this function returns the records present in the mongodb cloud
        '''

        url = 'https://data.mongodb-api.com/app/data-ouyxz/endpoint/data/v1/action/find'

        payload = json.dumps({
            "collection": "tabela",
            "database": "flask",
            "dataSource": "Flask-bd"
        })
        response = requests.request("POST", url=url, headers=self.header, data=payload).json()

        return response

    def insert_mongo(self,tasks:list):
        '''
        this functions add records in the mongodb cloud
        '''
        url = 'https://data.mongodb-api.com/app/data-ouyxz/endpoint/data/v1/action/insertMany'

        payload = json.dumps({
            "collection": "tabela",
            "database": "flask",
            "dataSource": "Flask-bd",
            "documents": tasks
        })
        response = requests.request("POST", url=url, headers=self.header, data=payload).json()

        return response

    def update_mongo(self,task: dict):
        '''
        this function delete records present in the mongodb cloud
        '''

        url = 'https://data.mongodb-api.com/app/data-ouyxz/endpoint/data/v1/action/updateOne'

        payload = json.dumps({
            "collection": "tabela",
            "database": "flask",
            "dataSource": "Flask-bd",
            "filter": {"_id": {
                "$oid":f"{task['_id']}" }
                },
            "update": {
                "$set": {
                    'task': task["task"],
                    'status': f'{task["status"]}'
                }
            }
        })
        response = requests.request("POST", url=url , headers=self.header, data=payload).json()

        return response

    def delete_mongo(self,task_id: str):
        '''
        this function delete records present in the mongodb cloud
        '''

        url = 'https://data.mongodb-api.com/app/data-ouyxz/endpoint/data/v1/action/deleteOne'

        payload = json.dumps({
            "collection": "tabela",
            "database": "flask",
            "dataSource": "Flask-bd",
            "filter": {"_id": {
                "$oid":f"{task_id}" }}
        })
        response = requests.request("POST", url=url , headers=self.header, data=payload).json()

        return response

