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
    # print(file_obj.name)
    # file_contents = file_obj.read()
    # print(file_contents)

    # to access one line at a time
    # for line in file_obj:
    #     print(line)

    """
    file_content = file_obj.reeadline()
    print(file_content)

    file_content = file_obj.reeadline()
    print(file_content)

    file_content = file_obj.reeadline()
    print(file_content)
    """
    
    size_to_read = 10

    '''
    file_contents = file_obj.read(sized_to_read)
    print(file_contents)

    file_contents = file_obj.read(sized_to_read)
    print(file_contents)

    file_contents = file_obj.read(sized_to_read)
    print(file_contents)

    file_contents = file_obj.read(sized_to_read)
    print(file_contents)
    '''
    # when there are no more characters to return, will return an empty strng

    
    file_contents = file_obj.read(size_to_read)

    while len(file_contents) > 0:
        print(file_contents, end='*')
        file_contents = file_obj.read(size_to_read)


# print(file_obj.closed)