'''
print("Hello World")
# For variable names, do not use reserved keywords
print(help('keywords'))  # shows all keywords

# Assign multiple variables with the same value simultaneously

a = b = c = 10  # works but not recommended
print(a, b, c)

# Expression vs Statement
x = 47  # Statement
y = 47 + 10  # expression



# Type Conversion
# convert to int
print(int(10.24))
print(int(float("10.24")))

# Convert to String
print(str(20))
print(type(str(20)))


## Strings ##
# Can be created either by using single, double, or tripple quotes
first_name = 'jane'
print(first_name)

last_name = "doe"
print(last_name)

address = '10 main st'
print(address)

job1 = "physician's Assistant"


## STRING FUNCTIONS ##

emp_name = "Jane Doe"
# len() --> returns number of characters in a given string
print(len(emp_name))

# upper and lower --> these convert string into corresponding cases
print(emp_name.upper())

# string concatenation
first_name = "Jane"
last_name = "Doe"
print(first_name + ' ' + last_name)

age = 24
print(first_name + ' ' + last_name + ':' + str(age))

# String Multiplication
print('hello'*3)
# can only add two strings;can only multiply sting by int



# Accessing string characters
emp_name ="Jane Doe"
print(emp_name[3])
# print(emp_name[8])  # index out of rnage because last character is at index 7

print(emp_name.index('n'))



### String Slicing ###

emp_name = "Jane Doe"
print(emp_name[2:6])
print(emp_name[:4])
print(emp_name[3:])
print(emp_name[-4:-1])
print(emp_name[1:6:2])  # the third value is the step value

print(emp_name.count('e'))  # counts that character

print(emp_name.find('Doe'))

print(emp_name.replace('Jane', 'John'))

print('oh' in emp_name)

# string Formatting
student_name = "Alice"
score = 87
print(student_name + ":" + str(score))
print("Name: {} score: {}".format(student_name, score))
# f-string
print(f'Name: {student_name} Score: {score}')

print(f'10 times 3 is {10*3}')
'''