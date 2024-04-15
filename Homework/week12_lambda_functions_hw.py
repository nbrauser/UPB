from functools import reduce  # import the reduce function
nums = [3, 2, 6, 8, 4, 6, 2, 9]
multiply = lambda x, y: x * y  # takes in two variables as y and x and uses lambda to multiply them
print(multiply(2, 4))  # prints the multiples of the two variables

print((lambda x,y: x-y)(5,4))  # prints the lambda function of two variables that are subtracted from each other. then passes the variables right after

big_five = filter(lambda x: x > 5, nums)  # uses lambda function and filter to make a new list of numbers only bigger than 5
print(list(big_five)) # prints the new list

alter_list = map(lambda x: x / 5 if x > 5 else x + 5, nums) # uses lambda and map to divide numbers bigger than 5 and adds 5 to other numbers
print(list(alter_list))  # print the new list

double = map(lambda x: x*2, nums)  # uses map to double every number in list 
print(list(double))  # print list

sum_odd_nums = reduce(lambda x, y: x + y, list(map(lambda x: x*x,filter(lambda x: x % 2 != 0, nums)))) 
# starts with a filter to take only numbers divisable by 2 then passes the filtered list to the map to then square the filtered list and then sends the map of the filter to the lambda function to add the numbers up 
print(sum_odd_nums) #prints the sum
