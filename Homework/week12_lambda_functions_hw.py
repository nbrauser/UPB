from functools import reduce
nums = [3, 2, 6, 8, 4, 6, 2, 9]
multiply = lambda x, y: x * y
print(multiply(2, 4))

print((lambda x,y: x-y)(5,4))

big_five = filter(lambda x: x > 5, nums)
print(list(big_five))

alter_list = map(lambda x: x / 5 if x > 5 else x + 5, nums)
print(list(alter_list))

double = map(lambda x: x*2, nums)
print(list(double))

sum_odd_nums = reduce(lambda x, y: x + y, list(map(lambda x: x*x,filter(lambda x: x % 2 != 0, nums))))
print(sum_odd_nums)
