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

