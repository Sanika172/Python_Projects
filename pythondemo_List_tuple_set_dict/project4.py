# list operations
# 1.Repitation
from pythondemo_Decorators.project07 import result

L1 = [23, 2, 5, 6, "paneer"]
print(L1 * 2)

# 2.Concatenation
L = [3, 6, 7, "tanuja", "sara,3.7"]
L2 = ["kavya", 4.5, 56, "c", 10]
print(L + L2)

# 3..Membership
list = [3, 5.6, "sara", "nitya", 34]
if "sara" in list:
    result = True
else:
    result = False

print(result)
# updating list elements
L = [34, 98, "laxmi", "poonam", 5.4]
print(L)
L[1] = 34
L[2] = "sumit"
print(L)
