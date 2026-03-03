# Program     : pertemuan2.py
# Deskripsi   : Belajar Ekspresi Dasar
# NIM/Nama    : 24060124120026/Gregorius Septiano Ariadi
# Tanggal     : 04/09/2024
# ===========================================================================
# DEFINISI DAN SPESIFIKASI
# ===========================================================================
# Belajar Ekspresi Dasar
# ===========================================================================
# REALISASI
# ===========================================================================

# angka = 1024                    # integer
# desimal = 3.14                  # real/float
# karakter = 'a'                  # char
# teks = "Solkhan's always"       # string
# bool = True                     # boolean
# masukan = input("Masukkan teks: ")

# print(angka)
# print(desimal)
# print(karakter)
# print(teks, bool)                   # contoh output dan variabel
# print(masukan, "berhasil dicetak")  # contoh output variabel dan teks

"""def kuadrat(x):
    return x*x

print(kuadrat(6))"""

def Isorigin(x,y) :
    return (x == 0) and (y == 0)

print(Isorigin(0,0))
print(Isorigin(5,10))

# control z = ngembaliin 
# control slash + pagar
# shift slash = menghapus

def max2(a, b):
    return ((a + b) + abs(a - b)) // 2

def max3(a, b, c):
    return max2(max2(a, b), c)

print(max2(5, 10))
print(max3(5, 10, 15))
