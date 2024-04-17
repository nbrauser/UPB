'''
# open command
# with open --> context manager

# 1. using the open comand 
# with files --> read,write,append
file_obj = open('sample_text','r')
# default mode is 'r'

print(file_obj.name)
print(file_obj.mode)

# close the file obj
file_obj.close()
'''

# 'with open' --> context management
with open('sample_text', 'r') as file_obj:
    print(file_obj.name)
    file_contents = file_obj.read()
    print(file_contents)

# print(file_obj.closed)