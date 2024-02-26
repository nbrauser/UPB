"""

print("hello")

# ## Normal Statements ##
a = 5
b = 0

# Critical Statement
try:
    print(a/b)
except Exception:
    print('Cannot divide by zero')
print('bye')

try:
    a = int(input('Enter first number: '))
    b = int(input('enter second number: '))
    result = a/b
    print('Connection opened')
except ZeroDivisionError as e:
    print('Something went wrong. ', e)
except ValueError as e:
    print('Something went wrong. ', e)
except Exception as e:
    print(e)
else:
    print(result)
finally:
    print("connection closed")
"""

numbers = [1, 2, 3, 0,  4, 5]
for num in numbers:
    try:
        result = 10/num
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print(result)