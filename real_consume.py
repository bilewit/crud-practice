import requests

response = requests.get('https://www.linkedin.com/in/tran-huong-b317b4157')
print('{0}'.format(response.text))

