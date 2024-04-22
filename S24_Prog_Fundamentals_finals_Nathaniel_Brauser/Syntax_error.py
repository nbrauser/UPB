from functools import reduce
# 24
number = 250
while number <= 1000:
    if number >= 750:
        print(number)
        number = number+100
    else:
        print(number*2)
    number = number + 50

# 25
val = 25
for i in range(0,val):
    if i%2 ==0:
        print(i+1)
    else:
        print(i-1)

# 26
weather = 'raining'
if weather == 'sunny':
    print('wear sunblock')
elif weather == 'snow':
    print('going skiing')
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
