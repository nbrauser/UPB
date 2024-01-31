# Question 1: take an imput string from user and creat a new sring with the first, middle, last characters of the imput string

first_string = input("Type a string \n")
string_length = len(first_string)
middle = (string_length/2)
first_char = first_string[0]
second_char = first_string[int(middle)]
third_char = first_string[string_length - 1]
print(first_char + second_char + third_char)