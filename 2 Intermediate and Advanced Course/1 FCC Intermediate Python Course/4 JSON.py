import json

# a good way to distuinguish a json text from a normal python text is json files must have speech marks ("") but
# python doesn't unless you write it with "" and have an indent(s) inside json files

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# sort_keys=True will sort our keys alphabetically
personJSON = json.dumps(person, indent=3)
print(personJSON)

with open('json/person.json', 'w') as file:
    json.dump(person, file, indent=3)

# how to convert from a JSON string into python
person = json.loads(personJSON)
print(person)

# how to convert from a JSON file into python

with open('json/person.json', 'r') as file:
    person = json.load(file)
    print(person)


# how to put a custom object into a JSON file. It has to be converted into text that can go into a json file as well
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Oscar', 64)


# encode an instance of the object
def encode_user(object):
    if isinstance(object, User):
        return {'name': object.name, 'age': object.age, object.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')


# dump and print a json version of this class
userJSON = json.dumps(user, default=encode_user, indent=3)
print(userJSON)

# better way to do that
from json import JSONEncoder


class UserEncorder(JSONEncoder):

    def default(self, object):
        if isinstance(object, User):
            return {'name': object.name, 'age': object.age, object.__class__.__name__: True}
        return JSONEncoder.default(self, object)


userJSON = UserEncorder(indent=3).encode(user)
print(userJSON)


# convert it into python
def decode_user(dct):
    # if the name of the class (User) we are looking for is inside the dictionary
    # then return the class user with the values of name and age in a dictionary form
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct


user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)
