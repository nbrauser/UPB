'''
x = 1

while x < 5:
    print(x)
    x += 1



# ## Print first 10 natural numbers (start from 1)
x = 1

while x <= 10:
    if x == 5:
        #break   breaks out of the loop as soon as if condition is satisfied
        print('Found 5! ')
        x += 1
        continue # will skip next lines and start next iteration
    print(x)
    x += 1


# ### For Loops #####
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)
    if num == 3:
        break

# ### Range Function
for i in range(10):
    print(i)

n = 0
for i in range(101):
    n += i
print(f'Sum is {n}')

n = int(input("type a number: "))
for i in range(1, 11,):
    t = n * i
    print(f'{n} * {i} = {t}')

# ######### Write a program to print numbers in reverse order

for i in range(-10,-1):
    print(i)


# ##### Nested Loops #########
nums = [1, 2, 3, 4, 5]
for num in nums :
    for letter in 'abc':
        print(num, letter)

rows = int(input('Enter the number of rows: '))
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
'''
n = int(input('Type a number: '))
i = 1
while i <= n:
    if (i % 3) == 0:
        if(i % 5) == 0:
            print('FizzBuzz')
            i += 1
            continue
        else:
            print('Fizz')
            i += 1
            continue
    elif(i % 5) == 0:
        print('buzz')
        i += 1
        continue
    print(i)
    i += 1