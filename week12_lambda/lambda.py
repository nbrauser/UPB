# function that takes in a number and returns the square of it
def square_num(a):
    return a * a


print(square_num(5))

square_num1 = lambda x: x * x
print(square_num1(5))

hello = lambda x: f"hello {x}"

print(hello('world'))

#  write a lambda function that checks whether a number is even or not
check_even = lambda num: "Even number" if num % 2 == 0 else "Odd"
print(check_even(17))

print((lambda x: f"Hello {x}")('World'))
# Immediately Invoked Function Expressions or IIFEs

print((lambda x: x * x)(5))

add_nums = lambda x, y: x + y
print(add_nums(2, 3))

# Higher order functions --> filter, map, reduce
nums = [3, 4, 6, 8, 4, 6, 2, 9]

# Filter
def is_even(n):
    return n % 2 == 0


#even_nums = filter(is_even, nums)
even_nums = filter(lambda n: n % 2 == 0, nums)
print(list(even_nums))

# MAP
def update_num(n):
    return n * 2


# doubles = map(update_num, nums)
doubles = map(lambda n: n * 2, nums)
print(list(doubles))

cities = ['boston', 'new york', 'miami', 'los angeles', 'phoenix']
length = map(lambda x: len(x), cities)
print(list(length))


# Reduce is used to reduce list to single number
from functools import reduce


def add_all(a, b):
    return a + b


sum_value = reduce(lambda x, y: x+y, nums)
print(sum_value)

sum_city = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, list(map(lambda x: len(x), cities))))
print(sum_city)
