# Question 1: take an imput string from user and creat a new sring with the first, middle, last characters of the imput string

first_string = input("Type a string \n")
string_length = len(first_string)
middle = (string_length/2)
first_char = first_string[0]
second_char = first_string[int(middle)]
third_char = first_string[string_length - 1]
print(first_char + second_char + third_char)

# Problem 2
firstname = str(input("What is your first name\n"))
lastname = str(input("What is your last name \n"))
# gets both first and last name making sure they are strings
age = int(input("What is your age \n"))
SSN = int(input("What is your SSN \n"))
height = int(input("What is your height in CM \n"))
weight = int(input("What is your weight in lbs \n"))
# gets all int values making sure to keep them as ints

new_height = height * 0.393701
new_weight = weight * 0.453592
# converting the height and weight to new measurements

print("Hello " + firstname + "! Thank your for applying. Please find your details below. \n")
print("     Age: " + str(age) + "\n")
print("     SNN: " + str(SSN) + "\n")
print("     Height: " + str(new_height) + "\n")
print("     Weight: " + str(new_weight) + "\n")


# problem 3
Phrase = "You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose. -Dr. Seuss"
print(Phrase[59:107])
print(Phrase.find('feet'))
print(Phrase.replace("Dr.Seuss", "Dr.Seuss, Oh,the Places You'll Go!"))