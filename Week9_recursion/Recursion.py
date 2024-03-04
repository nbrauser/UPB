'''
def sayhello(name):
    print(f"hello {name}!")


def user_details():
    user_name = input("enter a name: ")
    sayhello(user_name)
    user_city = input("enter your city: ")
    print(f"You are from {user_city}")


user_details()
'''


def test1(n):
    if n > 0:
        print("printing the value")
        print(n)
        print("calling the function ")
        test1(n-1)


test1(3)
print()


def test2(n):
    if n > 0:
        print("calling the function ")
        test1(n-1)
        print("printing the value")
        print(n)


test2(3)
