L = [100, 390, 200, 500, 450, 479]
S = L[0]
l = L[0]
for i in range(1, 6):
    if L[i] < S:
        s = L[i]
    if L[i] > l:
        l = L[i]
print("smallest element is", S)
print("largest element is", l)
