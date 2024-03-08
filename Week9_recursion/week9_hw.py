import statistics
def findfactorial(num):
    if (num <0):  # if the number is not positive cant take factorial
        print("Please use positive number")
        return
    elif(num<= 1):  # if the number is less than or equal to one it is just one
        return 1
    else:  
        return num * findfactorial(num-1)  # will return the number times factorial one mus number by recalling the function with recution 
factorial_value = findfactorial(5)  # call function and set what it returns to a variable
print(factorial_value)  # print variable


def quicksort(num_list):
    if len(num_list) <= 1:  # if the the list is only one number it is already sorted
        return num_list
    else:
        median_value = statistics.median([
            num_list[0], 
            num_list[int(len(num_list)/2)],
            num_list[-1]
        ])  # take the median value by giving the first number the middle number and the last number 
        left_list = [] 
        middle_list = []
        right_list = []
        for i in num_list:  # run loop for every number in the list 
            if i < median_value:  # if i is less than the the median add it to the left
                left_list.append(i)
            elif i > median_value:  # if it is greater it will add to the right list
                right_list.append(i)
            else:
                middle_list.append(i)  # if it is equal it will add to the middle
        return(quicksort(left_list) + middle_list + quicksort(right_list))  # return the sorted list
sorted_list = quicksort([31, 18, 72, 79, 3, 18, 92, 11, 44, 56, 41, 28])
print(sorted_list)  # call the function and print what it returns


fiblist = []  # creat a blank list to hold the fib sequence
def fibanachi(num):
    if num < 1:  # if the num is less than one we reached the end and can print the last two fib numbers
        print(fiblist[-1])
        print(fiblist[-2])
    else:
        if len(fiblist) < 2:  # if the length of fib list os not yet greater than two we can not add the two previous numbers so it is just appending with one
            fiblist.append(1)
            fibanachi(num-1)  # recution function 
        else:
            fiblist.append((fiblist[-1] + fiblist[-2]))  # if the length is greater than 2 it will add the two previous numbers and apend it to the list 
            fibanachi(num-1)  # recution function 
fibanachi(5)  # call the function 

