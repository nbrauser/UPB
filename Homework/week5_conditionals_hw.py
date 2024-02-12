import random
# Question 1
number = int(input('Type a number from 0-9: '))  # Prompts the user to input a value 0-9
words = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
# set of strings that are in the corisponding place as the number they represent e.g. zero is at words[0]
if 0 <= number <= 9:  # checks to see if the number they wrote actually follows the criteria
    print(words[number])  # Prints the string that goes with the number by slicing the list with th number they put in
else:  # In case they put in a value that is not in the correct range
    print("Please use numbers in the criteria")  # Tells them to try again with a different number

# Question 2

# rand_num = round(random.random(), 2)  # generates a random value between 0 and 1
# print(round(rand_num,2))

comp_move = ''
user_choice = 'yes'

while user_choice.lower() == 'yes':
    user_move = input('Pick either rock, paper, or scissors by typing r, p, or s: ')
    # prompts the user to pick either rock, paper, or scissors
    rand_num = round(random.random(), 2)  # generates a random value between 0 and 1
    if 0 <= rand_num < 1/3:
        comp_move = "r"  # if the random number is less than 1/3 the computer will play rock
    elif 1/3 <= rand_num < 2/3:
        comp_move = "p"  # if the random number is inbetween 1/3 and 2/3 the computer will play paper
    else:
        comp_move = 's'  # if the random number is greater than 2/3 and less than one it will play scissors

    result = ''

    if user_move == comp_move:
        result = 'Tie.'
    elif user_move == 'r':
        if comp_move == 'p':
            result = 'You Lose!'
        else:
            result = 'You Win!'
    elif user_move == 'p':
        if comp_move == 's':
            result = 'You Lose!'
        else:
            result = 'You Win!'
    elif user_move == 's':
        if comp_move == 'r':
            result = 'You Lose!'
        else:
            result = 'You Win!'
    else:
        result = 'Please type correct character using lowercase'
    print(f'Computer did {comp_move}')
    print(result)
    user_choice = input("type yes to keep playing if not type no. ")
'''
# Rock
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
'''
year = float(input('Please type a year: '))
result = ''
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            result = 'Leap Year.'
        else:
            result = 'Not leap year.'
    else:
        result = 'Leap year.'
else:
    result = 'Not leap year.'
print(result)

# Question 4
print("welcome to Treasure Island. Your mission is to find the treasure.")
result = ''
first_split = input("Go Left or Right? type r or l: ")
if first_split == 'l' or first_split == 'L':
    second_split = input("Swim or wait? type s or w: ")
    if second_split == 'w' or second_split == 'W':
        third_input = input("Yellow, Red, or Blue door? type y, b, or r: ")
        if third_input == 'y' or third_input == 'Y':
            result = "You Win!"
        elif third_input == 'r' or third_input == 'R':
            result = "Burned by fire. Game over."
        elif third_input == 'b' or third_input == 'B':
            result = " Eaten by beasts. Game Over."
        else:
            result = "Game Over."
    else:
        result = 'Attacked by trout. Game Over'
else:
    result = 'Fall into a hole and game over'
print(result)
