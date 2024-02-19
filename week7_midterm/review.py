import random
'''
for i in range(11):
    if i % 2 == 0:
        continue
    else:
        print(i)
# print odd numbers


# Write a program to calculate the sum and average of digits present in a string
# ex random289$18@str849ing6


total = 0
count = 0

input_str = input('enter a string with digits and other characters: ')
for char in input_str:
    if char.isdigit():
        total = total + int(char)
        count = count + 1
print(total)
print(round(total/count, 2) )


# write a program to print the number of digits, letters, and special symbols in a givin string
# ex random189$18@str849ing6
# output digits: 9, letters: 12, symbols: 2

digit = 0
letters = 0
symbol = 0

input_str = input('enter a string with digits and other characters: ')
for char in input_str:
    if char.isdigit():
        digit += 1
    elif char.isalpha():
        letters += 1
    else:
        symbol += 1
print(f"digits: {digit}, letters: {letters}, Symbols: {symbol}")

rows = int(input("type number of rows: "))

for i in range(0,rows):
    for n in range(0, i + 1):
        print(n * 2, end= " ")
    print(" ")
'''
target = round(random.random() * 100, 0)
answer = 0
guess = 0
while answer == 0:
    if guess <= 10:
        user_input = int(input("Guess a number 0-100: "))
        if user_input > target:
            print("Too high. Try again.")
            guess += 1
            print(guess)
        elif user_input < target:
            print("Too low. try again.")
            guess += 1
            print(guess)
        else:
            guess += 1
            print(f"You win in {guess} guesses")
            break
    else:
        print("You lose!")
        break
