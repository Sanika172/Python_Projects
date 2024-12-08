sum = 0
n1 = int(input("enter starting value"))
n2 = int(input("enter ending number"))
for i in range(n1, n2 + 1):
    if i % 2 == 0:
        sum = sum + i
print("sum of even numbers are", sum)
