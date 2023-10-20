import requests

data = {'questions_num': 4}

response = requests.post('http://127.0.0.1:8000/post_endpoint', json=data)
if response.status_code == 200:
    result = response.json()['res']
else:
    print('Error:', response.status_code)
