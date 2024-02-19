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
user_choice = 'yes'  # starts as yes so the while statement is furfilled and game will play

while user_choice.lower() == 'yes':  # as long as the user chooses yes at the end of the game will play again
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

    if user_move == comp_move:  # If both the user and computer play the same move they tie
        result = 'Tie.'  # changes result string to tie
    elif user_move == 'r':  # if the user plays r then it will move to see what the computer does
        if comp_move == 'p':  # when the user plays r than the way the user loses is when the computer plays p
            result = 'You Lose!'  # changes result to lose
        else:  # the only other option when user plays r and it is not a tie is when the comp plays s so user wins
            result = 'You Win!'  # Changes result to you win
    elif user_move == 'p':  # see what happens if the user plays p
        if comp_move == 's':  # if the computer plays s than the user loses
            result = 'You Lose!'  # change result to you lose
        else:  # the last result is if the user plays p and it is not a tie is the computer plays r and user wins
            result = 'You Win!'  # change result to you win
    elif user_move == 's':  # see what happens if the user plays s
        if comp_move == 'r':  # if the computer plays r and user plays s the user loses
            result = 'You Lose!'  # change result to you lose
        else:  # the last result is if the user plays s and it is not a tie is the computer plays p and user wins
            result = 'You Win!'  # change result to you win
    else:  # if the user characters does not apply to any of the if statements it prompts them to use correct characters
        result = 'Please type correct character using lowercase'  # prompts them to type new character
    print(f'Computer did {comp_move}')  # print what the computer did
    print(result)  # prints result
    user_choice = input("type yes to keep playing if not type no. ")  # prompt them to see if they want to play again
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
year = float(input('Please type a year: '))  # prompts them to type a year
result = ''  # set result to be a string
if year % 4 == 0:  # if the year is divisible by 4 continue to nested if
    if year % 100 == 0:  # if the year is divisible by 100 continue to next nested if
        if year % 400 == 0:  # if the year is divisible by 400 than it satisfies all the rules for leap year
            result = 'Leap Year.'  # change result to leap year
        else:  # if it is divisible by 100 and not 400 than it is not a leap year
            result = 'Not leap year.'  # change result to not a leap year
    else:  # if the year is divisible by 4 and not 100 than it is a leap year
        result = 'Leap year.'  # change a leap year
else:  # if it is not divisible by 4 than it is not a leap year
    result = 'Not leap year.'  # change result to not a leap year
print(result)  # print result

# Question 4
print("welcome to Treasure Island. Your mission is to find the treasure.")  # print the welcome message
result = ''  # set result as a string
first_split = input("Go Left or Right? type r or l: ")  # ask for first input
if first_split == 'l' or first_split == 'L':  # if they put l they went the right direction so continue to nested if
    second_split = input("Swim or wait? type s or w: ")  # ask for second input
    if second_split == 'w' or second_split == 'W':  # if they put w they went the right direction go to nested if
        third_input = input("Yellow, Red, or Blue door? type y, b, or r: ")  # ask for third input
        if third_input == 'y' or third_input == 'Y':  # if they choose y then they went the right direction and win
            result = "You Win!"  # change result to win
        elif third_input == 'r' or third_input == 'R':  # if they choose r then the lose
            result = "Burned by fire. Game over."  # change result to lose message
        elif third_input == 'b' or third_input == 'B':  # if they put b they lose
            result = " Eaten by beasts. Game Over."  # change result to lose message
        else:  # if the third input is none of the above
            result = "Game Over."  # change result to game over
    else:  # if the second input is not the correct one say they lose
        result = 'Attacked by trout. Game Over'  # change result to game over message
else:  # if the first input is not correct one say they lose
    result = 'Fall into a hole and game over'  # change result to game over
print(result)  # print result
