List = [45, 76, 20, 467, 34, 10]
for i in range(0, 6):
    temp = 0
    for j in range(0, 6):
        if List[i] < List[j]:
            temp = List[i]
            List[i] = List[j]
            List[j] = temp
print(List)
