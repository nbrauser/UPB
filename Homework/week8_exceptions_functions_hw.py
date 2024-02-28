# QUESTION 2

def palindrome():
    user_str1 = input("Give a string: ")  # Gets User input
    for n in range(0, len(user_str1)):  # will start a for loop till gets to length of string to slice all char
        if user_str1[n] == user_str1[-(n+1)]:  # if the first char is equal to the last and then second to second last
            if n == len(user_str1) - 1:  # if we have reached the end of the for loop
                print(f"{user_str1} is a palindrome.")  # it is a palindrome
            else:
                continue  # if we did not reach the end it will continue with the test
        else:  # if at any point the letter we are on does not equal its counterpart it is not a palindrome
            print(f"{user_str1} is not a palindrome.")  # print it is not a palindrome
            break  # end the test


def anagram():
    user_str1 = input("Give a string: ")
    user_str2 = input("Give a string: ")  # get the user string one and two
    sort_str1 = sorted(user_str1)
    sort_str2 = sorted(user_str2)  # Sort both stings to have them in alphabetical order
    if sort_str1 == sort_str2:  # if the sorted string are equal it has all the same letters
        print(f"{user_str1} and {user_str2} are anagrams.")  # print it is a palindrome
    else:
        print(f"{user_str1} and {user_str2} are not anagrams.")  # if it is not equal print it is not a palindrome


def user_input():
    user = {
        'name': input("What is your name? "),
        'birth': int(input("What is your birth year")),
        'budget': int(input("What is your budget?")),
        'price': int(input("What is the price? "))
    }  # Get user's input and store in a dictionary
    try:  # Try these operations
        age = 2024 - user['birth']  # calculate age by subtracting birth year from current year
        num_product = int(user['budget'] / user['price'])  # dividing budget by price to get amount use int to round
    except ZeroDivisionError as e:  # if they make price 0 it will print error
        print(e)
    except Exception as e:  # any other error will print error
        print(e)
    else:
        print(f"Hello {user['name']}! You are {age} and can buy {num_product} products.")  # print output


def triangle():
    length1 = int(input("What is the length of line one: "))
    length2 = int(input("What is the length of line two: "))
    length3 = int(input("What is the length of line three: "))  # Get all length of sides
    biggest_side = length1  # set side one as biggest side
    if length2 > biggest_side and length2 > length3:  # if side 2 is bigger than both other sides then we use it to test
        if length3 + length1 >= length2:  # test if the sum of the two smaller sides is greater than the biggest side
            print("Can create triangle.")  # if it is than it passes the test and is a triangle
        else:
            print("Can't create triangle.")  # if not it is not a triangle
    elif length3 > biggest_side and length3 > length2:  # If side 3 is bigger than both other side we use it to test
        if length2 + length1 >= length3:  # test if the sum of the smaller sides is greater than biggest side
            print("Can create triangle.")  # if it is than it passes the test
        else:
            print("Can't create triangle.")  # if not it is not a triangle
    else:  # since we tested the two other sides to see if they are bigger ,and it's not true side one is the biggest
        if length2 + length3 >= biggest_side:  # test if the sum of the small sides id greater than the big side
            print("Can create triangle.")  # if it is than it passes te test and is a triangle
        else:
            print("Can't create triangle.")  # if not than it is not a triangle
            # We only have to test if the sum of the smaller sides are greater than the biggest
            # because the biggest side plus any number will be greater than the rest of the sides. Ex 10 + 0.00001 > 9


palindrome()
anagram()
user_input()
triangle()
