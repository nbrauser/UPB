'''####### LISTS ########
# Allow us to hold duplicate values
# Order is maintained
# Can hold heterogeneous data


list1 = [10, 'test', True, 20.24, 10]
print(list1)

# len() --> returns the number of elements in a list
print(len(list1))


# index and slice
print(list1[2])  # accessing element at 3rd position
print(list1[1:4])
print(list1[-2])

# List can hold other list too
list2 = [10, 'hi', False, 22.12, ['hello', True, 20]]

# Creating an empty list
countries = []

# Elements can be added to a list using either append, insert, or extend
countries.append('USA')
countries.append('Canada')
countries.append('Mexico')
print(countries)  # append always add elements at the end

countries.insert(1,"France")
print(countries)

countries2 = ['Germany', 'Russia', 'Italy']
countries.extend(countries2)
print(countries)

countries.append(countries2)
print(countries)

# Remove an element - can use either remove or pop method
countries.remove('France')
print(countries)

countries.pop()
print(countries)

removed_country = countries.pop()
print(removed_country)
print(countries)

print(countries.pop(2))  # pop by default removes the last element but we can also specif a particular index


# Sorting list
countries.sort()  # in-place functions. modifying the internal contents of the list
print(countries)

num_list = [3434, 2193, 12, 43, 7]
num_list.sort(reverse=True)
print(num_list)

# Membership Test
print("USA" in countries)

# Creating a string from list elements
countries_str ='-'.join(countries)
print(countries_str)
print(type(countries_str))


# creating a list by breaking string into different elements
countries3 = countries_str.split('-')
print(countries3)

########## Tuples ###########
# similar to list but once they are created you cannot add new elements to it or remove elements from it.

tuple1 = (36, 45, 32, 45, 3548)
print(tuple1)  # order maintained, duplicates allowed
print(tuple1[2])


# tuple1[2] = 89 # cannot modify, add or remove
# Can access or slice a tuple





############## SETS #############
# Sets do not allow duplicate values
# order is not guaranteed


courses = {'networking', 'english', 'math', 'history'}
print(courses)

print("math" in courses)

# ## Widely used for 'set' operation

courses1 = {'networking', 'physics', 'programming'}
print(courses.union(courses1))
print(courses.intersection(courses1))
print(courses.difference(courses1))
print(courses1.difference(courses))

courses.add('psychology')
courses.remove('math')



########## DICTIONARIES ###############
# store key-value pairs
employees = {
    'id': 2133,
    'name': 'Jane Doe',
    'salary': 4500,
    'skills': ['Java', 'SQL', 'c#'],
    'address':{
        'city': "Pittsburgh",
        'state': 'PA',
        'zip-code': 15044,
    }
}

# Accessing dictionary values
print(employees['name'])
print(employees['address']['city'])

employees['name'] = 'ryan'

employees.update({'name': 'jane watson', 'salary': 5000})

# Deleting key
del employees['salary']

print(employees)

# Accessing Keys
print(employees.get('address'))
print(employees.get('phone'))
print(employees.get('phone)', 'Not found'))


# ## Creating Empty Collections ###
List1 = []
tuple1 = ()

# tuple with a single element
tuple2 = (10,)
print(type(tuple2))


# set1 = {} this creates dictionary
set1 = set()
print(type(set1))
dict1 = {}


# #### ACCESSING COLLECTION ITEMS ####
list1 =  [34,43,65,7, [45,56,20, [1234, 233, 6578]], 4]
print(list1[3][3][1])

set1 = {34, 235,32,1}
'''
# set1[1] won't work because sets dont have order

dict1 = {
    'name': 'john',
    'age': 25,
    'address': {
        'city': 'Boston',
        'state': 'MA',
        'zip': 12434
},
    'skills': ['java', 'SQL', 'PHP']
}

print(dict1['address']['state'])

employee_details = [
    {
        'name': 'john',
        'age': 25,
        'address': {
            'city': 'Boston',
            'state': 'MA',
            'zip': 12434
    },
    'skills': ['java', 'SQL', 'PHP']
    },
    {
    'name': 'john',
    'age': 25,
    'address': {
        'city': 'Boston',
        'state': 'MA',
        'zip': 12434
},
    'skills': ['java', 'SQL', 'PHP']
},
]


### LIst and tuple to a set####
list2 = [343, 3, 5, 8, 10, 3]
set2 = set(list2)
print(set2)
