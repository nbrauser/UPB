# JSON - java script object notation

emp_data = '''
{
    "employees":    [
        {
            "name": "John",
            "age": 29
            "emails": ["john@gmail.com", "john@outlook.com"]
        },
        {
            "name": "Jane",
            "age":48
            "emails":null
        }
    ]
}
'''
import json
# to load json string into a puthon object
json_data = json.loads(emp_data)
print(json_data)
print(type(json_data))
print(json_data['employees'])

for emp in json_data['employees']:
    # del emp['name']
    pass

print(json_data)

# delete the email for each employee and then load it into a json string
new_string = json.dumps(json_data, indent=2)
print(new_string)
print(type(new_string))

# API --> application programing interface
"""
address --> user entered address 16701, recomended address 16701-1234
web application --> USPS public API --> valid and return appropriate address
"""

# load JSON data from a file into python object
with open('states.json', 'r') as file_obj:
    data = json.load(file_obj)

#print(data)
#print(type)

for state in data['states']:
    print(state['name'], state['abbreviation'])

    # remove the area code for each state
    del state['area_codes']

print(data['states'])
      
# to write json data to a file
with open('new_states.json', 'w') as file_obj:
    json.dump(data, file_obj, indent=2)






"""
Fidelity Incestments --> facebook page, twitter handle, linkedin
Facebook page-JSON format
posts, comments,replies ect...
"""

import random

random.random()