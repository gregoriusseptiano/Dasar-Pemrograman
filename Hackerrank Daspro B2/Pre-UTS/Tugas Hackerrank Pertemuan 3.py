# def jumlahbulan(m):
#         if m == 1 : return 1
#         elif m == 2 : return 32
#         elif m == 3 : return 60
#         elif m == 4 : return 91
#         elif m == 5 : return 121
#         elif m == 6 : return 152
#         elif m == 7 : return 182
#         elif m == 8 : return 213
#         elif m == 9 : return 244
#         elif m == 10 : return 274
#         elif m == 11 : return 305
#         elif m == 12 : return 335
#         else: return "None"
    
# def HariKe(d,m,y):
#     return jumlahbulan(m) + d - 1

# print(eval(input()))



# def IsKabisat(y):
#     if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
#         return True
#     else:
#         return False
    
# def jumlahbulan(m):
#         if m == 1 : return 1
#         elif m == 2 : return 32
#         elif m == 3 : return 60
#         elif m == 4 : return 91
#         elif m == 5 : return 121
#         elif m == 6 : return 152
#         elif m == 7 : return 182
#         elif m == 8 : return 213
#         elif m == 9 : return 244
#         elif m == 10 : return 274
#         elif m == 11 : return 305
#         elif m == 12 : return 335
#         else: return print("BULAN INVALID")
        
# def HariKe(d,m,y):
#     if IsKabisat(y) and m > 2 :
#         return jumlahbulan(m) + d - 1 + 1
#     else :
#         return jumlahbulan(m) + d - 1
    
# print(eval(input()))



# def Konversi(x,y):
#     if y == 1:
#         return int(x*4/5)
#     elif y == 2:
#         return int((x*9/5)+32)
#     elif y == 3:
#         return int(x+273)
#     else:
#         return "None"

# print(eval(input()))



# def WujudAir(x):
#     if x <= 0:
#         return "padat"
#     elif 0 < x < 100:
#         return "cair"
#     elif x >= 100:
#         return "gas"
    
# print (eval(input()))



# def JenisSegitiga(a,b,c):
#     if (a == b == c):
#         return "sama sisi"
#     elif ((a == b and b != c) or (b == c and c != a) or (c == a and b != y )):
#         return "sama kaki"
#     else: 
#         return "sembarang"

# print(eval(input()))



# def JenisSegitiga(a,b,c):
#     if a + b > c and a + c > b and b + c > a:
#         if a == b == c:
#             return "sama sisi"
#         elif a == b or b == c or c == a:
#             return "sama kaki"
#         else: 
#             return "sembarang"
#     else:
#         return "tidak terbentuk"
    
# print (eval(input()))



# def diskriminan(x,y,z):
#     return y**2 - 4 * x * z

# def x1(x,y,z):
#     return(-y + (diskriminan(x,y,z) ** 0.5)) / (2 * x)

# def x2(x,y,z):
#     return(-y - (diskriminan(x,y,z) ** 0.5)) / (2 * x)

# def AkarKuadrat(a,b,c):
#     if diskriminan(a,b,c) < 0:
#         return "Akar kompleks"
#     else:
#         if x1(a,b,c) > x2(a,b,c):
#             return x1(a,b,c) / x2(a,b,c)
#         else:
#             return x2(a,b,c) / x1(a,b,c)
        
# print(AkarKuadrat(3,4,-5))


