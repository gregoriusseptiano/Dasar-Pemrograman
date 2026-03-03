# Nama File : set_24060124120026.py
# Deskripsi : Program yang berisi implementasi operasi-operasi himpunan
# Pembuat   : 24060124120026/Gregorius Septiano Ariadi
# Tanggal   : Rabu, 6 November 2024

#DEFINISI DAN SPESIFIKASI TYPE
#Set adalah sebuah tipe bentukan yang berisi kumpulan elemen yang unik dan tidak terurut.abs

from listFunctions import * # listFunctions bisa diganti dengan file yang berisi operasi-operasi list

#DEFINISI DAN SPESIFIKASI OPERASI LIST YANG DIPERLUKAN UNTUK HIMPUNAN
# Rember: elemen, list -> list
# Rember(x,L) menghapus sebuah elemen x dari list L
#   Jika x ada di list L, maka elemen L berkurang 1.
#   Jika x tidak ada di list L maka L tetap.
#   List kosong tetap menjadi list kosong.
def Rember(x,L):                #Menghapus elemen x yang ditemui pertama kali dari list L.
    if IsEmpty(L):
        return L
    else:
        if FirstElmt(L) == x:
            return Tail(L)
        else:
            return Konso(FirstElmt(L),Rember(x, Tail(L)))

# print(Rember(2, [1,2,3,2]))

def Rember2(x,L):                #Menghapus elemen x yang ditemui pertama kali dari list L.
    if IsEmpty(L):
        return []
    else:
        if LastElmt(L) == x:
            return Head(L)
        else:
            return Konso(LastElmt(L),Rember2(x, Head(L)))

# print(Rember2(5, [5,5,6,7,3,5]))

# MultiRember: elemen, list -> list
# MultiRember(x,L) menghapus semua kemunculan elemen x dari list L.
#   List baru yang dihasilkan tidak lagi memiliki elemen x.
#   List kosong tetap menjadi list kosong.
def MultiRember(x, L):
    if IsEmpty(L):
        return L
    else:
        if FirstElmt(L) == x:
            return MultiRember(x, Tail(L))
        else:
            return Konso(FirstElmt(L), MultiRember(x, Tail(L)))
            
# print(MultiRember(3, [1,2,3,3,4]))

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR SET DARI LIST
# MakeSet: list -> set
# MakeSet(L) membuat set dari list L dengan menghapus semua kemunculan lebih dari satu kali
#   list kosong tetap menjadi himpunan kosong
def MakeSet(L):                     #Memanfaatkan fungsi IsMember(x,L) untuk mengecek duplukasi elemen.
    if IsEmpty(L):
        return L
    else:
        if IsMember(FirstElmt(L), Tail(L)):
            return MakeSet(Tail(L))
        else:
            return [FirstElmt(L)] + MakeSet(Tail(L))

# print(MakeSet([1,3,3,3,4]))

def MakeSet2(L):                     #Memanfaatkan fungsi MultiMember(x,L) untuk menghapus duplukasi elemen.
    if IsEmpty(L):
        return L
    else:
        return Konso(FirstElmt(L),MakeSet2(MultiRember(FirstElmt(L),Tail(L))))

# print(MakeSet2([1,1,3,3,2]))

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR SET
# KonsoSet: elemen, set -> set
# KonsoSet(e,H) menambahkan sebuah elemen e sebagai elemen pertama set H
#   dengan syarat e belum ada di dalam himpunan H
def KonsoSet(e, H):
    if IsMember(e, H):
        return H
    else:
        return Konso(e, H)
    
# print(KonsoSet(1, [2, 3, 4, 5]))

#DEFINISI DAN SPESIFIKASI PREDIKAT
# IsSet: list -> boolean
# IsSet(L) mengembalikan true jika L adalah sebuah set
def IsSet(L):
    if IsEmpty(L):
        return True
    else:
        if IsMember(FirstElmt(L), Tail(L)):
            return False
        else:
            return IsSet(Tail(L))

# print(IsSet([1, 2, 3, 4, 5]))

# IsSubset: 2 set -> boolean
# IsSubset(H1,H2) mengembalikan ture jika H1 merupakan subset dari H2
def IsSubSet(H1, H2):
    if IsEmpty(H1):
        return True
    else:
        if not IsMember(FirstElmt(H1), H2):
            return False
        else:
            return IsSubSet(Tail(H1), H2)

# print(IsSubSet([1, 2, 3, 10, 4, 5], [2, 3, 10, 4, 5, 9, 1]))

# IsEqualSet: 2 set -> boolean
# IsEqualSet(H1,H2) benar jika H1 adalah set yang sama dengan H2
def IsEqSet(H1, H2):                   #Memanfaatkan Fungsi IsSubset(H1,H2)
    return IsSubSet(H1, H2) and IsSubSet(H2, H1)

# print(IsEqSet([1, 2, 3, 10, 4, 5, 9], [2, 3, 10, 4, 5, 9, 1]))

def IsEqSet2(L1, L2):                   #Mengecek satu persatu elemen pada H1 dan H2
    if not IsSet(L1) or not IsSet(L2):
        return False
    else:
        if NbElmt(L1) != NbElmt(L2):
            return False
        else:
            if not IsMember(FirstElmt(L1), L2):
                return False
            else:
                return IsEqSet2(Tail(L1), Rember(FirstElmt(L1), L2))

# print(IsEqSet2([2,3,4],[4,3,2]))

# IsIntersect: 2 set -> boolean
# IsIntersect(H1,H2) benar jika H1 beririsan dengan H2
def IsIntersect(H1, H2):
    if IsEmpty(H1) or IsEmpty(H2):
        return False
    else:
        if IsMember(FirstElmt(H1), H2):
            return True
        else:
            return IsIntersect(Tail(H1), H2)

# print(IsIntersect([2, 10, 9, 8], [2, 0, 9, 7]))

#DEFINISI DAN SPESIFIKASI OPERASI TERHADAP HIMPUNAN
# MakeIntersect: 2 set -> set
# MakeIntersect(H1,H2) menghasilkan set baru yang merupakan hasil irisan antara H1 dan H2
def MakeIntersect(H1, H2):                  #Rekursif terhadap H1
    if IsEmpty(H1) or IsEmpty(H2):
        return []
    else:
        if IsMember(FirstElmt(H1), H2):
            return Konso(FirstElmt(H1), MakeIntersect(Tail(H1), H2))
        else:
            return MakeIntersect(Tail(H1), H2)

# print(MakeIntersect([2, 3, 6, 7], [1, 2, 5, 7]))

def MakeIntersect2(H1, H2):                 #Rekursif terhadap H2
    if IsEmpty(H1) or IsEmpty(H2):
        return []
    else:
        if IsMember(FirstElmt(H2), H1):
            return Konso(FirstElmt(H2), MakeIntersect2(H1, Tail(H2)))
        else:
            return MakeIntersect2(H1, Tail(H2))

# print(MakeIntersect2([2, 3, 6, 7], [1, 2, 5, 7]))

# MakeUnion: 2 set -> set
# MakeUnion(H1,H2) menghasilkan set baru yang merupakan hasil gabungan antara H1 dan H2
def MakeUnion(H1, H2):                      #Rekursif Terhadap H1
    if IsEmpty(H1) and IsEmpty(H2):
        return []
    elif not IsEmpty(H1) and IsEmpty(H2):
        return H1
    elif IsEmpty(H1) and not IsEmpty(H2):
        return H2
    else:
        if IsMember(FirstElmt(H1), H2):
            return MakeUnion(Tail(H1), H2)
        else:
            return Konso(FirstElmt(H1), MakeUnion(Tail(H1), H2))

# print(MakeUnion([1, 2, 3, 5], [1, 2, 4]))

def MakeUnion2(H1, H2):                      #Rekursif Terhadap H2
    if IsEmpty(H1) and IsEmpty(H2):
        return []
    elif not IsEmpty(H1) and IsEmpty(H2):
        return H1
    elif IsEmpty(H2) and not IsEmpty(H1):
        return H2
    else:
        if IsMember(FirstElmt(H2), H1):
            return MakeUnion2(H1, Tail(H2))
        else:
            return Konso(FirstElmt(H2), MakeUnion2(H1, Tail(H2)))

# print(MakeUnion2([1, 2, 3, 5], [1, 2, 4]))

# NBIntersect: 2 set -> integer
# NBIntersect(H1,H2) menghasilkan jumlah elemen yang beririsan pada H1 dan H2
#   tanpa memanfaatkan fungsi MakeIntersect(H1,H2).
def NBIntersect(H1, H2):
    if IsEmpty(H1) or IsEmpty(H2):
        return 0
    else:
        if IsMember(FirstElmt(H1), H2):
            return 1 + NBIntersect(Tail(H1), Rember(FirstElmt(H1), H2))
        else:
            return NBIntersect(Tail(H1), H2)
    
# print(NBIntersect([1,2,3,4], [5,7,2,1]))

# NBUnion: 2 set -> integer
# NBUnion(H1,H2) menghasilkan jumlah elemen hasil gabungan antara H1 dan H2
#   tanpa memanfaatkan fungsi MakeUnion(H1,H2).
def NBUnion(H1, H2):
    if IsEmpty(H1):
        return NbElmt(H2)
    elif IsEmpty(H2):
        return NbElmt(H1)
    else:
        if IsMember(FirstElmt(H1), H2):
            return NBUnion(Tail(H1), H2)
        else:
            return 1 + NBUnion(Tail(H1), H2)

# print(NBUnion([1,2,3,4,5],[2,3,5,7]))  