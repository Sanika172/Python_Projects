for i in range(5, 0, -1):
    for j in range(4, 5 - i, -1):
        print(" ", end=" ")
    for k in range(1, 7 - i):
        print(k, end=" ")
    print("\n")
