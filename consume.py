import requests

response = requests.get('http://127.0.0.1:8000/drink.json')
print('{0}'.format(response.json()))
x = response.json()
print(x[0]['title'])