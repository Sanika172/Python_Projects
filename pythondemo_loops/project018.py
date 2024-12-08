n = int(input("emter any number to check"))
temp = 0
for i in range(2, (n // 2 + 1)):
    if n % i == 0:
        temp = 1
        break
if temp == 0:
    print("number is prime")
else:
    print("no prime")
