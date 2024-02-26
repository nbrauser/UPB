"""
Functions - to reuse code
"""
# num --> function parameter


def check_even(num):
    if num % 2 == 0:
        return True

# making a function call


isEven = check_even(4)
print(isEven)
# check_even(9)


print('hello')  # has no return type


def check_string():
    first_word = input("Type a word: ")
    second_word = input("Type a word: ")
    for n in range(0, len(first_word)):
        for i in range(0,len(second_word)):
            if first_word[n] == second_word[i]:
                continue
            elif i == len(second_word):
                print("Not True")
                break


