import requests

# Make a GET request
response = requests.get('https://api.example.com/users')
print(response.status_code)
print(response.text)

# Add query parameters to a GET request
params = {'page': 2, 'per_page': 100}
response = requests.get('https://api.example.com/users', params=params)
print(response.url)

# Send a POST request with JSON data
data = {'name': 'John', 'age': 30}
response = requests.post('https://api.example.com/users', json=data)
print(response.status_code)

# Send a POST request with form data
data = {'name': 'John', 'age': 30}
response = requests.post('https://api.example.com/users', data=data)
print(response.status_code)

# Send a PUT request with JSON data
data = {'name': 'John', 'age': 30}
response = requests.put('https://api.example.com/users/1', json=data)
print(response.status_code)

# Send a DELETE request
response = requests.delete('https://api.example.com/users/1')
print(response.status_code)

# Send a request with headers
headers = {'Authorization': 'Bearer mytoken'}
response = requests.get('https://api.example.com/users', headers=headers)
print(response.status_code)

# Send a request with cookies
cookies = {'session_id': '1234567890'}
response = requests.get('https://api.example.com/users', cookies=cookies)
print(response.status_code)

# Handle errors and exceptions
try:
    response = requests.get('https://api.example.com/nonexistent')
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(e)
