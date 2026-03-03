from math import sqrt

akar = int (sqrt(256))

print(akar)

import math

akar = int (math.sqrt(256))

print(akar)

from math import sqrt as akar

hasil = int (akar(256))

print(hasil)

def MakePoint(x, y):
    return [x, y]

def Absis(P):
    return P[0]

def Ordinat(P):
    return P[1]

P = MakePoint(4, 6)

print(P)
print(Absis(P))
print(Ordinat(P))

def IsOrigin(P):
    if Absis(P) == 4 and Ordinat(P) == 6:
        return True
    else:
        return False

P = MakePoint(4, 6)

print(IsOrigin(P))

def MakePoint(x,y):
    return [x,y]

def Absis(P):
    return P[0]

def Ordinat(P):
    return P[1]

P = MakePoint(10,15)

def Jarak0(P):
    return int (sqrt(Absis(P)**2 + Ordinat (P)**2))

print (Jarak0(P))


