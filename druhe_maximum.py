import random

seznam = [99,99,98]
length = int(input())
for i in range(length):
    seznam.append(random.randint(0, 100))
print(seznam)
if seznam[0]>seznam[1]:
    max = seznam.pop(0)
    max2 = seznam.pop(0)
else: max = seznam.pop(1)
max2= seznam.pop(0)
for i in seznam:
    if i>max:
        max2 =max
        max = i
    elif i>max2 and i!=max:
        max2 = i
    elif max == max2 and max2 != i:
        max2 = i
if max == max2:
    max2 = "none"
print(max, max2)
