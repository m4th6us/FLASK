lista = {
	"documents": [
		{
			"_id": "63c5859ad5f8ef201b3f778b",
			"id": 1,
			"status": "biriri",
			"task": " do creu"
		},
		{
			"_id": "63c5859ed5f8ef201b3f7824",
			"id": 1,
			"status": "biriri",
			"task": " do creu"
		},
		{
			"_id": "63c585a325ce649e55794ce0",
			"id": 1,
			"status": "biriri",
			"task": " do creu"
		},
		{
			"_id": "63c585b059ad1777226585bd",
			"id": 5,
			"status": "biriri",
			"task": " do creu"
		}
	]
}
for i in lista['documents']:
	print(i['id'])

print(lista['documents'][0]['id'])