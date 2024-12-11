# 1..with parameter with return value
def add(a, b):
    sum = a + b
    return sum


print("sum is", add(20, 40))


# 2..with parameter without return value
def mul(x, y):
    result = x * y
    print("result of multiplication is", result)


mul(4, 6)


# 3..without parameter with return value
def div():
    a = int(input("enter value of a"))
    b = int(input("enter value of b"))
    result = a / b
    return result


print("division of given numbers is", div())


# 4..without return value without parameters
def sub():
    n1 = int(input("enter first value"))
    n2 = int(input("enter second value"))
    result = n1 - n2
    print("subtraction of given numbers is", result)


sub()
