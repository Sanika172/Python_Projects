def square(x):
    return x ** 2


numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
for result in squared_numbers:
    print(result)

# result=list(squared_numbers)
# print(result)
