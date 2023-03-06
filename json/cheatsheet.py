import json

# Convert a Python object to a JSON string
python_object = {'name': 'John', 'age': 30, 'city': 'New York'}
json_string = json.dumps(python_object)
print(json_string)

# Convert a JSON string to a Python object
json_string = '{"name": "John", "age": 30, "city": "New York"}'
python_object = json.loads(json_string)
print(python_object)

# Write a Python object to a JSON file
python_object = {'name': 'John', 'age': 30, 'city': 'New York'}
with open('data.json', 'w') as file:
    json.dump(python_object, file)

# Read a JSON file into a Python object
with open('data.json', 'r') as file:
    python_object = json.load(file)
print(python_object)

# Customize the JSON encoding and decoding process
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_json(self):
        return {'name': self.name, 'age': self.age}

    @staticmethod
    def from_json(json_object):
        return Person(json_object['name'], json_object['age'])

person = Person('John', 30)
json_string = json.dumps(person, default=person.to_json)
print(json_string)

person = json.loads(json_string, object_hook=Person.from_json)
print(person.name, person.age)
