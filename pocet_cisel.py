import random

seznam = []
cisla = {}
length = int(input())
for i in range(length):
    seznam.append(random.randint(0, 100))

for i in seznam:
    if i in cisla:
        cisla[i] += 1
    else:
        cisla[i] = 1

print(seznam)
print(cisla)