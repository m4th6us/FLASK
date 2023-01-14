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
        url = "https://data.mongodb-api.com/app/data-ouyxz/endpoint/data/v1/action/find"

        payload = json.dumps({
            "collection": "tabela",
            "database": "flask",
            "dataSource": "Flask-bd"
        })

        response = requests.request("POST", url, headers=self.header, data=payload).json()
        return response



    def insert_mongo(self,tasks = []):

        url = "https://data.mongodb-api.com/app/data-ouyxz/endpoint/data/v1/action/insertMany"

        payload = json.dumps({
            "collection": "tabela",
            "database": "flask",
            "dataSource": "Flask-bd",
            "documents": tasks
        })

        response = requests.request("POST", url, headers=self.header, data=payload).json()
        return response

    
    def delete_mongo(self, tasks = []):
        url = "https://data.mongodb-api.com/app/data-ouyxz/endpoint/data/v1/action/deleteMany"
        
        payload = json.dumps({
            "collection": "tabela",
            "database": "flask",
            "dataSource": "Flask-bd",
            "documents": tasks
        })

        response = requests.request("POST", url, headers=self.header, data=payload).json()
        return response
