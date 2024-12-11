# arbitrary arguments(multiple)
def sum(*marks):
    total = 0
    for m in marks:
        total = total + m
    print("total marks are", total)


sum(10, 30, 40)
sum(10, 30, 40, 60, 50)
