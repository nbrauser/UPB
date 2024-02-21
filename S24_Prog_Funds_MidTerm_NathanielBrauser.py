import random
# Question 1
keep_play = "yes"
while keep_play.lower() == "yes":
    user_toss = input("Pick either heads or tails: ")
    rand_num = round(random.random(), 2)
    rand_toss = " "
    if rand_num < 0.5:
        rand_toss = "heads"
    else:
        rand_toss = "tails"
    if user_toss.lower() == rand_toss:
        print(f"You picked {user_toss}, Computer picked {rand_toss}- It is a tie!")
    elif user_toss.lower() == "heads":
        print(f"You picked {user_toss}, Computer picked {rand_toss}- You Win!")
    else:
        print(f"You picked {user_toss}, Computer picked {rand_toss}- You Lose!")
    keep_play = input("Type yes to keep playing: ")

# Question 2

num_list = []
count_list = int(input("How many number do you want in the list: "))
for i in range(0, count_list):
    num_list.append(int(input("Type number for list: ")))
for i in range(0, count_list):
    if num_list[i] > 500:
        break
    elif num_list[i] > 150:
        continue
    elif num_list[i] % 5 == 0:
        print(num_list[i], end=" ")
print(" ")


# Question 3
rows = int(input("How many rows? "))
for i in range(0, rows):
    for n in range(1, i * 2 + 2, 2):
        print(n, end=" ")
    print(" ")

# Question 4

target_num = int(input("Type a target number: "))
for i in range(1, target_num + 1):
    factor_list = []
    for n in range(1, i + 1):
        if i % n == 0:
            factor_list.append(n)
    print(f"Factors of {i}: {factor_list}")
