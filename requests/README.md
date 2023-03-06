# Python `requests` Module Cheat Sheet

The `requests` module is a popular third-party library for sending HTTP requests in Python. It provides a simple and intuitive interface for sending HTTP requests and handling the corresponding responses. Here's a cheat sheet with all the important functions and methods available in the `requests` module:

## Sending HTTP Requests

- `requests.request(method, url, **kwargs)`: Sends a HTTP request to the specified URL using the specified method (e.g. GET, POST, PUT, DELETE, etc.).
  - Example: `response = requests.request('GET', 'https://api.example.com/users')`

- `requests.get(url, **kwargs)`: Sends a GET request to the specified URL.
  - Example: `response = requests.get('https://api.example.com/users')`

- `requests.post(url, data=None, json=None, **kwargs)`: Sends a POST request to the specified URL with the specified data.
  - Example: `response = requests.post('https://api.example.com/users', data={'name': 'John', 'age': 30})`

- `requests.put(url, data=None, **kwargs)`: Sends a PUT request to the specified URL with the specified data.
  - Example: `response = requests.put('https://api.example.com/users/123', data={'name': 'John Doe', 'age': 35})`

- `requests.patch(url, data=None, **kwargs)`: Sends a PATCH request to the specified URL with the specified data.
  - Example: `response = requests.patch('https://api.example.com/users/123', data={'name': 'John Doe'})`

- `requests.delete(url, **kwargs)`: Sends a DELETE request to the specified URL.
  - Example: `response = requests.delete('https://api.example.com/users/123')`

## HTTP Request Parameters

- `params`: A dictionary or list of tuples containing the parameters to be sent with the request.
  - Example: `response = requests.get('https://api.example.com/users', params={'page': 2, 'per_page': 50})`

- `headers`: A dictionary containing the headers to be sent with the request.
  - Example: `response = requests.get('https://api.example.com/users', headers={'Authorization': 'Bearer mytoken'})`

- `auth`: A tuple containing the authentication credentials (e.g. username and password) to be sent with the request.
  - Example: `response = requests.get('https://api.example.com/users', auth=('username', 'password'))`

- `cookies`: A dictionary containing the cookies to be sent with the request.
  - Example: `response = requests.get('https://api.example.com/users', cookies={'session_id': 'abc123'})`

## HTTP Response Handling

- `response.text`: Returns the response body as a string.
  - Example: `print(response.text)`

- `response.json()`: Parses the response body as JSON and returns the resulting object.
  - Example: `data = response.json()`

- `response.status_code`: Returns the HTTP status code of the response.
  - Example: `print(response.status_code)`

- `response.headers`: Returns a dictionary containing the headers of the response.
  - Example: `print(response.headers)`

- `response.cookies`: Returns a dictionary containing the cookies set by the server in the response.
  - Example: `print(response.cookies)`

## Miscellaneous Functions

- `requests.session()`: Returns a `Session` object that can be used to persist cookies and other parameters across multiple requests.
  - Example
