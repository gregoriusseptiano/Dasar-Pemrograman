# Nama File : LOL_24060124120026.py
# Deskripsi : Program yang berisi implementasi operasi-operasi List Of List
# Pembuat   : 24060124120026/Gregorius Septiano Ariadi
# Tanggal   : Rabu, 13 November 2024

from set_24060124120026 import *

#DEFINISI DAN SPESISIFIKASI TYPE PREDIKAT KHUSUS LIST
# IsEmpty : list of list -> boolean
# IsEmpty(L) true jika list of list kosong, false jika tidak
def IsEmpty(L) :
    return L == []

# IsAtom : list of list -> boolean
# IsAtom(L) true jika list of list L adalah sebuah Atom, false jika tidak
def IsAtom(L) :
    return type(L) != list

# IsList : list of list -> boolean
# IsList(L) true jika list of list L adalah sebuah List, false jika tidak
def IsList(L) :
    return type(L) == list

#DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstList : list of list tidak kosong -> list
# FirstList(S) mengembalikan elemen pertama dari list of list S (mungkin sebuah atom atau list).
def FirstList(S) :
    if IsEmpty(S):
        return []
    else:
        return S[0]

# LastList : list of list tidak kosong -> list
# LastList(S) mengembalikan elemen terakhir dari list of list S (mungkin sebuah atom atau list).
def LastList(S) :
    if IsEmpty(S):
        return []
    else:
        return S[-1]

# TailList : list of list tidak kosong -> list
# TailList(S) mengembalikan list of list yang elemen pertamanya dihapus.
def TailList(S) :
    if IsEmpty(S):
        return []
    else:
        return S[1:]

# HeadList : list of list tidak kosong -> list
# HeadList(S) mengembalikan list of list yang elemen terakhirnya dihapus.
def HeadList(S) :
    if IsEmpty(S):
        return []
    else:
        return S[:-1]

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# KonsLo : list, list of list -> list of list
# KonsLo(L, S) menambahkan list L sebagai elemen pertama dalam list of list S
def KonsLo(L, S):
    return [L] + S

# KonsLi : list of list, list -> list of list
# KonsLi(S, L) menambahkan list L sebagai elemen terakhir dalam list of list S
def KonsLi(S, L):
    return S + [L]

# Aplikasi
# print(KonsLo([1, 2, 3], [4, 5, 6]))       # [[1, 2, 3], 4, 5, 6]
# print(KonsLi([1, 2, 3], [4, 5, 6]))       # [1, 2, 3, [4, 5, 6]]
# print(FirstList([[1, 2, 3], 4, 5, 6]))    # [1, 2, 3]
# print(LastList([[1, 2, 3], 4, 5, 6]))     # 6
# print(TailList([[1, 2, 3], 4, 5, 6]))     # [4, 5, 6]
# print(HeadList([[1, 2, 3], 4, 5, 6]))     # [1, 2, 3]
# print(IsEmpty([]))                        # True
# print(IsEmpty([1]))                       # False
# print(IsAtom(1))                          # True
# print(IsAtom([1, 2, 3]))                  # False
# print(IsList([1, 2, 3]))                  # True
# print(IsList(1))                          # False

#REALISASI TUGAS SOURCE CODE PERTEMUAN 9
# IsMemberS: elemen, list of list -> boolean
# IsMemberS(x,S) mengembalikan true jika elemen x ada di dalam list of list S
#   Contoh aplikasi:
#   IsMemberS(3, []) {menghasilkan false}
#   IsMemberS(3, [2, 4, 3, [1], [4,5]]) {menghasilkan true}
#   IsMemberS(3, [2, 4, 7, [1], [3,5]]) {menghasilkan true}
def IsMemberS(x, S):
    if IsEmpty(S):
        return False
    elif IsAtom(FirstList(S)):
        if FirstList(S) == x:
            return True
        else:
            return IsMemberS(x, TailList(S))
    elif IsList(FirstList(S)):
        if IsMemberS(x, FirstList(S)):
            return True
        else:
            return IsMemberS(x, TailList(S))

# print(IsMemberS(3, []))
# print(IsMemberS(3, [2, 4, 3, [1], [4,5]]))
# print(IsMemberS(3, [2, 4, 7, [1], [3,5]]))

# Rember: elemen, list of list -> list of list
# Rember(x,S) menghapus semua elemen x yang ada di list of list S
#   Contoh aplikasi:
#   Rember*(3, []) {menghasilkan []}
#   Rember*(3, [4, 3, [2,4], 3]) {menghasilkan [4, [2,4]]}
#   Rember*(3, [2, 4, [3,6,9], 5, 3]) {menghasilkan [2, 4, [6,9], 5]}
def Rember(x,S):
    if IsEmpty(S):
        return S
    else:
        if IsList(FirstList(S)):
            return KonsLo(Rember(x,FirstList(S)),Rember(x,TailList(S)))
        else:
            if FirstList(S) == x:
                return Rember(x,TailList(S))
            else:
                return KonsLo(FirstList(S),Rember(x,TailList(S)))

# print(Rember(3, []))
# print(Rember(3, [4, 3, [2,4], 3])) 
# print(Rember(3, [2, 4, [3,6,9], 5, 3]))

# Max: list of list -> elemen
# Max(S) mengembalikan elemen maksimun di dalam list of list S
#   Contoh aplikasi:
#   Max([4, 5, 6, [8,9,10], [12,0], 8]) {menghasilkan 12}
#   Max([4, 15, 6, [8,9,10], [12,0], 8]) {menghasilkan 15}
def Max2(a,b):
    if a >= b:
        return a
    else:
        return b

def Max(S):
    if IsOneElmt(S):
        if IsAtom(FirstList(S)):
            return FirstList(S)
        else:
            return Max(FirstList(S))
    else:
        if IsAtom(FirstList(S)):
            return Max2(FirstList(S),Max(TailList(S)))
        else:
            return Max2(Max(FirstList(S)),Max(TailList(S)))

# print(Max([4, 5, 6, [8,9,10], [12,0], 8]))
# print(Max([4, 15, 6, [8,9,10], [12,0], 8])) 

# NBElmtAtom: list of list -> integer
# NBElmtAtom(S) mengembalikan banyaknya elemen list of list S yang berupa atom
#   Contoh aplikasi:
#   NBElmtAtom([4, 5, 6, [8,9,10], [12,0], 8]) {menghasilkan 4}
#   NBElmtAtom([4, 15, 6, [8,9], 10, [12], 8]) {menghasilkan 5}
#   NBElmtAtom([[8,9,10]]) {menghasilkan 0}
def NBElmtAtom(S):
    if IsEmpty(S):
        return 0
    elif IsAtom(FirstList(S)):
        return 1 + NBElmtAtom(TailList(S))
    else:
        return NBElmtAtom(TailList(S))

# print(NBElmtAtom([4, 5, 6, [8,9,10], [12,0], 8]))
# print(NBElmtAtom([4, 15, 6, [8,9], 10, [12], 8]))
# print(NBElmtAtom([[8,9,10]]))

# NBElmtList: list of list -> integer
# NBElmtList(S) mengembalikan banyaknya elemen list of list S yang berupa list
#   Contoh aplikasi:
#   NBElmtList([4, 5, 6, [8,9,10], [12,0], 8]) {menghasilkan 2}
#   NBElmtList([[4, 15], 6, [8,9], 10, [12], 8]) {menghasilkan 3}
#   NBElmtList([[8,9,10]]) {menghasilkan 1}
def NBElmtList(S):
    if IsEmpty(S):
        return 0
    elif IsList(FirstList(S)):
        return 1 + NBElmtList(TailList(S))
    else:
        return NBElmtList(TailList(S))

# print(NBElmtList([4, 5, 6, [8,9,10], [12,0], 8]))
# print(NBElmtList([[4, 15], 6, [8,9], 10, [12], 8]))
# print(NBElmtList([[8,9,10]]))

# SumLoL: list of list -> integer
# SumLoL(S) mengembalikan jumlah semua elemen dalam list of list S
#   Contoh aplikasi:
#   SumLoL([[]]) {menghasilkan 0}
#   SumLoL([4, 5, 6, [2,3,1]]) {menghasilkan 21}
#   SumLoL([[2,3,4]]) {menghasilkan 9}
def SumLoL(S):
    if IsEmpty(S):
        return 0
    elif IsAtom(FirstList(S)):
        return FirstList(S) + SumLoL(TailList(S))
    elif IsList(FirstList(S)):
        return SumLoL(FirstList(S)) + SumLoL(TailList(S))

# print(SumLoL([[]]))
# print(SumLoL([4, 5, 6, [2,3,1]]))
# print(SumLoL([[2,3,4]]))

# MaxNBElmtList: list of list -> integer
# MaxNBElmtList(S) mengembalikan banyaknya elemen list maksimun yang ada pada list of list S 
#   Contoh aplikasi:
#   MaxNBElmtList([[4,5,6,7], [8,9,10], [12,0], 8]) {menghasilkan 4}
#   MaxNBElmtList([[4,15], 6, [8,9], 10, [12], 8]) {menghasilkan 2}
#   MaxNBElmtList([8,9,10]) {menghasilkan 0}
def NBElmt(S):
    if IsEmpty(S):
        return 0
    else: 
        return 1 + NBElmt(TailList(S))

def MaxNBElmtList(S):
    if IsEmpty(S):
        return 0
    elif IsList(FirstList(S)):
        return Max2(NBElmt(FirstList(S)), MaxNBElmtList(TailList(S)))
    else:
        return MaxNBElmtList(TailList(S))

# print(MaxNBElmtList([[4,5,6,7], [8,9,10], [12,0], 8]))
# print(MaxNBElmtList([[4,15], 6, [8,9], 10, [12], 8]))
# print(MaxNBElmtList([8,9,10]))

# MaxSumElmt: list of list -> integer
# MaxSumElmt(S) mengembalikan elemen maksimun pada list of list S 
#   jika elemen berupa list, maka dihitung jumlahan elemen dalam list tersebut
#   jika elemen atom, maka nilainya adalah elemen tersebut
#   Contoh aplikasi:
#   MaxSumElmt([1,2], 9, [4,5,6], 8]) {menghasilkan 15}
#   MaxSumElmt([1,2], 90, [4,5,6], 8]) {menghasilkan 90}
#   MaxSumElmt([8,9,10]) {menghasilkan 10}
#   MaxSumElmt([[8,9,10]]) {menghasilkan 27}
#   MaxSumElmt([[]]) {menghasilkan 0}
def MaxSumElmt(S):
    if IsEmpty(S):
        return 0
    elif IsList(FirstList(S)):
        return Max2(SumElmt(FirstList(S)), MaxSumElmt(TailList(S)))
    else:
        return Max2(FirstList(S), MaxSumElmt(TailList(S)))

# print(MaxSumElmt([[1,2], 9, [4,5,6], 8]))
# print(MaxSumElmt([[1,2], 90, [4,5,6], 8]))
# print(MaxSumElmt([8,9,10]))
# print(MaxSumElmt([[8,9,10]]))
# print(MaxSumElmt([[]]))


