from math import pi as pi

def obvod_trojuhelnik(a,b,c):
    return a+b+c
def obsah_trojuhelnik(a,va):
    return (a*va)/2
def obvod_ctverec(a):
    return 4*a
def obsah_ctverec(a):
    return a*a
def obvod_obdelnik(a,b):
    return 2*(a+b)
def obsah_obdelnik(a,b):
    return a*b
def obvod_kruh(r):
    return 2*pi*r
def obsah_kruh(r):
    return pi*r*r
def obvod_pravidelny_nuhelnik(n,a):
    return n*a
def objem_krychle(a):
    return a*a*a
def povrch_krychle(a):
    return 6*a*a
def objem_kvadr(a,b,c):
    return a*b*c
def povrch_krychle(a,b,c):
    return (2*a*b)+(2*b*c)+(2*a*c)

print(obsah_kruh(5))