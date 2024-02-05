# ###### NESTED IF ELSE #########
'''
height = int(input('Please enter your height in cms: '))
photos_cost = 0
ticket_price = 0

if height > 120:
    print('can ride')
    age = int(input('Please enter your age: '))
    if 45 > age > 18:
        print('Ticket is $12')
        ticket_price = 12
    elif 12 <= age < 18:
        print('Ticket is $7')
        ticket_price = 7
    elif 45 >= age <=55:
        print('Ticket is $0')
        ticket_price = 0
    elif age < 12:
        print('Ticket is $5')
        ticket_price = 5
    want_photos = input("Do you want a photo taken? Enter Y/y or N/n ")
    if want_photos == "Y" or want_photos == "y":
        photos_cost = 3
    bill = photos_cost + ticket_price
    print(f'Your final bill is ${bill}')

else:
    print('Can\'t ride')
'''

grade = int(input("What is your grade in percent %"))

if grade < 60:
    print("F")
elif grade < 70:
    if grade < 63:
        print("D-")
    elif grade < 67:
        print("D")
    else:
        print("D+")
elif grade < 80:
    if grade < 73:
        print("C-")
    elif grade < 77:
        print("C")
    else:
        print("C+")
elif grade < 90:
    if grade < 83:
        print("B-")
    elif grade < 87:
        print("B")
    else:
        print("B+")
elif grade < 100:
    if grade < 93:
        print("A-")
    elif grade < 97:
        print("A")
    else:
        print("A+")
else:
    print("Please use a correct percentage")


