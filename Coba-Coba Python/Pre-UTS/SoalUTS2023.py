def HargaAir(kode, penggunaan):
    if (kode == "A"):
        if (penggunaan > 10):
            return 30000 + (penggunaan - 10) * 2500
        else:
            return 30000
    elif (kode == "B"):
        if (penggunaan > 10):
            return 40000 + (penggunaan - 10) * 3000
        else:
            return 40000
    elif (kode == "C"):
        if (penggunaan > 10):
            return 50000 + (penggunaan - 10) * 3500
        else:
            return 50000

print(HargaAir("A", 25))
print(HargaAir("B", 50))
print(HargaAir("C", 70))




def bulan(b):
    if b == 1:
        return 1
    elif b == 2:
        return 32
    elif b == 3:
        return 60
    elif b == 4:
        return 91
    elif b == 5:
        return 121
    elif b == 6:
        return 152
    elif b == 7:
        return 182
    elif b == 8:
        return 213
    elif b == 9:
        return 244
    elif b == 10:
        return 274
    elif b == 11:
        return 305
    elif b == 12:
        return 335

def hariTanpaKabisat(h, b, t):
    return bulan(b) + h - 1

def hariKabisat(h, m, t):
    if m > 2:
        return bulan(m) + h - 1 + 1
    else:
        return bulan(m) + h - 1

def jumlahHari(H, B, T):
    if T % 4 == 0 and T % 100 != 0 or T % 400 == 0:
        return hariKabisat(H, B, T)
    else:
        return hariTanpaKabisat(H, B, T)

def hariKe(x, y, z):
    if jumlahHari(x, y, z) % 7 == 1:
        return "Senin"
    elif jumlahHari(x, y, z) % 7 == 2:
        return "Selasa"
    elif jumlahHari(x, y, z) % 7 == 3:
        return "Rabu"
    elif jumlahHari(x, y, z) % 7 == 4:
        return "Kamis"
    elif jumlahHari(x, y, z) % 7 == 5:
        return "Jumat"
    elif jumlahHari(x, y, z) % 7 == 6:
        return "Sabtu"
    elif jumlahHari(x, y, z) % 7 == 0:
        return "Minggu"
       
def IsNextDayFriday(d, m, y):
    return hariKe(d, m, y) == "Kamis"
        

# print(IsNextDayFriday(2, 1, 1990))
# print(IsNextDayFriday(4, 1, 1990))
# print(IsNextDayFriday(9, 3, 1993))
print(IsNextDayFriday(4, 1, 2024))
print(IsNextDayFriday(10, 10, 1990))
print(IsNextDayFriday(5, 3, 2021))