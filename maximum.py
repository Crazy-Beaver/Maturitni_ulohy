import random

seznam = []
length = int(input())
for i in range(length):
    seznam.append(random.randint(0, 100))
print(seznam)
max = seznam[0]
for i in seznam:
    if i>max:
        max = i
print(max)
