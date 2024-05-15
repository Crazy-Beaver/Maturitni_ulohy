import random

seznam = []
length = int(input())
for i in range(length):
    seznam.append(random.randint(0, 100))
print(seznam)
sum =0
for i in seznam:
    sum += i
prumer = sum/len(seznam)
print(prumer)