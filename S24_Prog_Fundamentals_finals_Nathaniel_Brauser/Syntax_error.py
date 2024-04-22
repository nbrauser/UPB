from functools import reduce
# 24
number = 250  # define the variable then give it a value
while number <= 1000:
    if number >= 750: # add a colan after the if statement and organize it as greater than equal to no =>
        print(number)
        number = number+100
    else:  # add colan
        print(number*2)
    number = number + 50  # add indent so is still inside while loop

# 25
val = 25  # define variable before giving it value
for i in range(0,val): # do not need "the" and add colan after for statement
    if i%2 ==0:
        print(i+1)
    else:
        print(i-1) # indent back one and add parenthesis

# 26
weather = 'raining'
if weather == 'sunny':  # add extra equals to not assign a value but compare them
    print('wear sunblock')  # add indent
elif weather == 'snow':  # add extra equals to not assign a value but compare them
    print('going skiing')  # add indent
else:
    print(weather)

# 27
num_list = [14, 17, -13, -75, 150, 15, 19, 10, -3, 16, 9, -145, 12, 50]
sum_odd_nums = reduce(lambda x, y: x + y, list(map(lambda x: x-5,filter(lambda x: x % 2 != 0, num_list))))
print(sum_odd_nums)
# 28
with open('sample_text', 'r') as file_obj:
    print(file_obj.name)
    file_contents = file_obj.read()
    print(file_contents)

# 30
from urllib.request import urlopen
with urlopen("https:////dummyjson.com//products") as products:
    api_products = products.read()
for product in data['api_products']:
    print(api_products['title'])
