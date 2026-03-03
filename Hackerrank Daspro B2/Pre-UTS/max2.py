def max2(a,b) :
    if a >= b :
        return a
    else :
        return b

#Aplikasi
print("Maksimun dari 10 dan 7 adalah", max2(10,7))
print("Maksimun dari 3 dan 5 adalah", max2(3,5))
print("Maksimun dari 20 dan 20 adalah", max2(20,20))


def max2(a,b) :
    return (a if a >= b else b)

#Aplikasi
print("Maksimun dari 10 dan 7 adalah", max2(10,7))
print("Maksimun dari 3 dan 5 adalah", max2(3,5))
print("Maksimun dari 20 dan 20 adalah", max2(20,20))


def max3(a,b,c) :
    if a > b and a > c :
        return a
    elif b > a and b > c :
        return b
    elif c > a and c > b :
        return c

#Aplikasi
print("Maksimun dari 10, 7, dan 5 adalah", max3(10,7,5))
print("Maksimun dari 3, 5, dan 2 adalah", max3(3,5,2))
print("Maksimun dari 20, 20, dan 20 adalah", max3(20,20,20))


def max3(a,b,c) :
    if a > b :
        if a > c :
            return a
        else :
            return c
    else :
        if b > c :
            return b
        else :
            return c

#Aplikasi
print("Maksimun dari 10, 7, dan 5 adalah", max3(10,7,5))
print("Maksimun dari 3, 5, dan 2 adalah", max3(3,5,2))
print("Maksimun dari 20, 20, dan 20 adalah", max3(20,20,20))


def is_segitiga(a,b,c):
    if (a == b and b == c):
        return "segitiga sama sisi"
    elif ((a == b and b != c)or (b == c and c != a)or (c == a and a != b )):
        return "segitiga sama kaki"
    else:
        return "segitiga sembarang"
    
print(is_segitiga(5,5,5))

def IsAnSegitiga(x,y,z):
    if (x == y == z):
        return "Segitiga Sama Sisi"
    elif ((x == y and y != z) or (y == z and z != x) or (z == x and x != y )):
        return "Segitiga Sama Kaki"
    else: 
        return "Segitiga Sembarang"
        
print(IsAnSegitiga(5,5,5))
print(IsAnSegitiga(5,10,5))
print(IsAnSegitiga(100,200,500))
