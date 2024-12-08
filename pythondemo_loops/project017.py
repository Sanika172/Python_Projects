n = int(input("enter any number"))
sum = 0
while n > 0:
    r = n % 10
    sum = sum + r
    n = n // 10
print("addition of given digits of a number", sum)
