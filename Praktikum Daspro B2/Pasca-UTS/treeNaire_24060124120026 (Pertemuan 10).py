# Nama File : treeNaire_24060124120026.py
# Deskripsi : File untuk implementasi pohon n-aire
# Pembuat   : 24060124120026/Gregorius Septiano Ariadi
# Tanggal   : Rabu, 20 November 2024

from listFunctions import *

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
def makePN(A,PN):
    return [A,PN]

#DEFINISI DAN SPESIFIKASI SELEKTOR
def akar(PN):
    return PN[0]

def anak(PN):
    return PN[1]

#DEFINISI DAN SPESIFIKASI PREDIKAT
def isTreeNEmpty(PN):
    return PN == []

def isOneElmt(PN):
    return (isTreeNEmpty(PN) == False) and (isTreeNEmpty(anak(PN)) == True)

def NbNElmt(PN):
    # Basis: Jika pohon kosong
    if isTreeNEmpty(PN):
        return 0

    # Jika hanya ada satu elemen (akar saja)
    if isOneElmt(PN):
        return 1

    # Hitung 1 untuk akar, dan rekursif pada setiap anak pohon
    # Tanpa menggunakan loop, kita memanggil fungsi untuk setiap anak secara rekursif
    # Pertama pada anak pertama
    return 1 + NbNElmt(anak(PN)[0]) + NbNElmtChild(anak(PN)[1:])

# Fungsi tambahan untuk menghitung jumlah elemen pada sisa anak-anak
def NbNElmtChild(PN):
    # Basis: Jika tidak ada anak
    if isTreeNEmpty(PN):
        return 0

    # Jika ada anak, rekursif pada anak pertama dan sisa anak-anak
    return NbNElmt(PN[0]) + NbNElmtChild(PN[1:])

def NbNDaun(PN):
    # Basis: Jika pohon kosong
    if isTreeNEmpty(PN):
        return 0

    # Jika pohon adalah daun (anak kosong)
    if isOneElmt(PN) and isTreeNEmpty(anak(PN)):
        return 1

    # Rekursi pada akar dan anak-anak
    return NbNDaunChild(anak(PN))

# Fungsi tambahan untuk menghitung jumlah daun pada sisa anak-anak
def NbNDaunChild(PN):
    # Basis: Jika tidak ada anak
    if isTreeNEmpty(PN):
        return 0

    # Jika ada anak, rekursif pada anak pertama dan sisa anak-anak
    return NbNDaun(PN[0]) + NbNDaunChild(PN[1:])

#APLIKASI
T = makePN(2,[])
print(makePN(2,[]))
print(isTreeNEmpty(T))
print(isOneElmt(T))
T2 = makePN('A',[makePN('B',[makePN('D',[]),makePN('E',[]),makePN('F',[])]),makePN('C',[makePN('G',[]),makePN('H',[makePN('I',[])])])])
print(T2)
print(NbNElmt(T2))
print(NbNDaun(T2))