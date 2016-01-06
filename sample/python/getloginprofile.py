import requests

credentials = 'your_assetic_username', 'your_assetic_password'
session = requests.Session()
session.auth = credentials

asseticcloud = 'your_assetic_enviornment_url'

endpoint =  asseticcloud + '/api/User/Details'

response = session.get(endpoint)

if response.status_code != 200:
    print('Failed to retrieve user deatil with error {}'.format(response.status_code))
    exit()
	
data = response.json()
print(data)
