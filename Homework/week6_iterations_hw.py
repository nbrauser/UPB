# ### QUESTION ONE ######

end_num = int(input("Type a number greater than 1: "))  # gets the ending number form user
prime = []  # list where we will put prime numbers
for i in range(1, end_num):  # runs a loop for each number till we get to the end number
    for num in range(1, i + 1):  # each number will run a loop to see if it is divisible by any numbers beside itself
        if num == 1:  # since all numbers are divisible by one we skip if num is one
            continue
        elif num == i:  # if the number we are dividing by is equal to the number we are dividing we have a prime number
            prime.append(i)  # add prime number to list
        elif i % num == 0:  # if the number is divisible by any number
            break  # we break the loop we are in and the outside loop will move to the next number
print(prime)  # print the prime numbers


# ### QUESTION TWO ########

num_target = int(input("Type an end number: "))  # gets number from user
even = []  # list to hold our even numbers
for n in range(0, 1 + num_target, 2):  # will run a loop from 0 and count by 2 to stay on even numbers
    # end bound is one plus our target to end after we run the target number
    even.append(n)  # adds number to even list
print(even)  # print list


# #### QUESTION THREE ####

num_three = [10, 20, 30, 40, 50, 60]  # list of numbers
for j in range(1, len(num_three), 2):  # will run loop starting at 1 and count by 2 to keep j an odd number
    # since the length of the list is one plus the last index the upper bound will run every index up to the length
    print(num_three[j])  # prints the numbers


# ##### QUESTION FOUR #######

unsort_list = [10, 24, 8, 187, 34, 100]  # list of numbers
max_num = unsort_list[0]  # sets the 0 index to the max
for s in range(1, len(unsort_list)):  # will run the 1 index through the length since we already set o index to max
    # the length as upper bound will run all indexes since length is one more than last index
    if max_num >= unsort_list[s]:  # if the current max is bigger than index we are in move on to next
        continue  # move on to next index in loop
    elif max_num < unsort_list[s]:  # if the current index is bigger than current max
        max_num = 0  # change the max to zero
        max_num += unsort_list[s]  # change max to current index
print(max_num)  # Print max
