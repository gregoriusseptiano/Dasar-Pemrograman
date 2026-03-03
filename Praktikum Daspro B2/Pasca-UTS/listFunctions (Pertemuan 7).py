# Program   : listfunctions.py
# Deskripsi : Fungsi-fungsi untuk operasi list
# NIM/Nama  : 24060124120026/Gregorius Septiano Ariadi
# Tanggal   : 30/10/2024

#REALISASI SELEKTOR AGAR FUNGSI BISA BERJALAN
# Head: List tidak kosong -> List
def Head(L):
    if IsEmpty(L):
        return None
    else: 
        return L[:-1]

# Tail: List tidak kosong -> boolean
def Tail(L):
    if IsEmpty(L):
        return None
    else: 
        return L[1:]

# REALISASI KONSTRUKTOR
# Konso: elemen, List -> List
def Konso(e, L):
    return [e] + L

# Konsi: List, elemen -> List
def Konsi(L, e):
    return L + [e]

# print("Hasil Konso:", Konso(1, [2, 3, 4, 5]))
# print("Hasil Konsi:", Konsi([1, 2, 3, 4], 5))

# REALISASI PREDIKAT
# IsEmpty: List -> boolean
def IsEmpty(L):
    return L == []

# IsOneElmt: List -> boolean
def IsOneElmt(L):
    if IsEmpty(L):
        return False
    else:   
        return Tail(L) == [] and Head(L) == []

# print("\nHasil IsEmpty:", IsEmpty([]))
# print("Hasil IsEmpty:", IsEmpty([1,2,3,4,5]))
# print("Hasil IsOneElmt:", IsOneElmt([]))
# print("Hasil IsOneElmt:", IsOneElmt([1]))
# print("Hasil IsOneElmt:", IsOneElmt([1, 2, 3 ,4 ,5]))

# REALISASI SELEKTOR
# FirstElmt: List tidak kosong -> elemen
def FirstElmt(L):
    if IsEmpty(L):
        return None
    else: 
        return L[0]

# LastElmt: List tidak kosong -> elemen
def LastElmt(L):
    if IsEmpty(L):
        return None
    else: 
        return L[-1]

# Tail: List tidak kosong -> boolean
def Tail(L):
    if IsEmpty(L):
        return None
    else: 
        return L[1:]

# Head: List tidak kosong -> List
def Head(L):
    if IsEmpty(L):
        return None
    else: 
        return L[:-1]

# print("\nHasil FirstElmt:", FirstElmt([]))
# print("Hasil FirstElmt:", FirstElmt([1,2,3,4,5]))
# print("Hasil LastElmt:", LastElmt([]))
# print("Hasil LastElmt:", LastElmt([1,2,3,4,5]))

# print("\nHasil Tail:", Tail([0]))
# print("Hasil Tail:", Tail([1,2,3,4,5]))
# print("Hasil Head:", Head([0]))
# print("Hasil Head:", Head([1,2,3,4,5]))

# REALISASI OPERATOR
# NbElmt: List -> integer
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else: 
        return 1 + NbElmt(Tail(L))

# print("\nHasil NbElmt:", NbElmt([]))
# print("Hasil NbElmt:", NbElmt([0]))
# print("Hasil NbElmt:", NbElmt([1, 1, 1, 1, 1]))
# print("Hasil NbElmt:", NbElmt([1, 2, 3, 4, 5]))

# TUGAS REALISASI OPERATOR
# ElmtkeN: integer >= 0, List -> elemen
# ElmtkeN(N, L) : Mengirimkan elemen list yang ke N, N <= NbElmt(L) dan N>=0
def ElmtkeN(N,L):
    if N <= NbElmt(L) and N >= 0:
        if N == 0:
            return FirstElmt(L)
        else:
            return ElmtkeN(N-1, Tail(L))

# print(ElmtkeN(2, [3,4,5]))

# IsMember: elemen, List -> boolean
# IsMember(X,L) adalah benar jika X adalah elemen list L
def IsMember(x, L):
    if IsEmpty(L):
        return False
    else:
        if LastElmt(L) == x:
            return True
        else:
            return (IsMember(x, Head(L)))

# print(IsMember(2, [3, 4, 6, 2]))

# Copy: List -> List
# Copy(L) : Menghasilkan list yang identik dengan list asal
def Copy(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L), Copy(Tail(L)))

# print(Copy([2, 3, 4, 5]))

# Inverse: List -> List
# Inverse(L) : Menghasilkan list L yang dibalik, yaitu yang urutan elemennya
#   adalah kebalikan dari list asal
def Inverse(L):
    if IsEmpty(L):
        return []
    else:
        return Konsi(Inverse(Tail(L)), FirstElmt(L))

# print(Inverse([3, 70, 40, 55]))

# Konkat: 2 List -> List
# Konkat(L1,L2) : Menghasilkan konkatenasi 2 buah list, dengan list L2 "sesudah" list L1
def Konkat(L1, L2):
    if IsEmpty(L2):
        return L1
    else:
        return Konkat(L1 + [FirstElmt(L2)], Tail(L2))

# print(Konkat([10, 14, 60, 100], [35, 66, 90]))

# SumElmt: List of integer -> integer
# SumElmt(L) menghasilkan jumlahan dari setiap elemen di list L
def SumElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return FirstElmt(L) + SumElmt(Tail(L))

# print(SumElmt([1, 2, 3, 4, 5]))

# AvgElmt: List of integer -> integer
# AvgElmt(L) menghasilkan nilai rata-rata
def AvgElmt(L):
    return int(SumElmt(L)/NbElmt(L))

# print(AvgElmt([1, 2, 3, 4, 5]))

# MaxElmt: List of integer -> integer
# MaxElmt(L) mengembalikan elemen maksimun dari list L
def max2(x,y):
    return int((x+y+(abs(x-y)))/2)

def MaxElmt(L):
    if IsOneElmt(L):
        return LastElmt(L)
    else:
        return max2(FirstElmt(L), MaxElmt(Tail(L)))

# print(MaxElmt([1, 2, 10, 2, 3]))

# MaxNB: List of integer -> <integer, integer>
# MaxNB(L) menghasilkan <max,countMax>
#   dengan max adalah elemen maksimun list L
#   dan countMax adalah banyaknya kemunculan max di list L
def maxlist(x):
    if IsOneElmt(x):
        return LastElmt(x)
    else:
        return max2(LastElmt(x), maxlist(Head(x)))

def NbOcc(x, L):
    if IsOneElmt(L):
        if x == FirstElmt(L):
            return 1
        else:
            return 0
    else:
        if x == FirstElmt(L):
            return 1 + NbOcc(x, Tail(L))
        else:
            return NbOcc(x, Tail(L))

def MaxNb(L):
    return [maxlist(L), NbOcc(maxlist(L), L)]

# print(MaxNb([100, 100000, 3000000, 30000000, 30000000, 1000000000]))

# AddList: 2 List of integer -> List of integer
# AddList(L1,L2) menghasilkan list baru yang setiap elemennya
#   adalah hasil penjumlahan setiap elemen di L1 dan L2 pada posisi yang sama
def AddList(L1, L2):
    if IsEmpty(L1) or IsEmpty(L2):
        return []
    else:
        return Konso((FirstElmt(L1) + FirstElmt(L2)), AddList(Tail(L1), Tail(L2)))

# print(AddList([1, 6, 10], [3, 9, 6]))

# IsPalindrom: List of character -> boolean
# IsPalindrom(L) benar jika L merupakan kata palindrom
#   yaitu kata yang sama jika dibaca dari kiri atau kanan
#   contoh: RUSAK, KASUR RUSAK, NABABAN
def IsPalindrom(L):
    if IsEmpty(L):
        return True
    elif IsOneElmt(L):
        return True
    else:
        return FirstElmt(L) == LastElmt(L) and IsPalindrom(Head(Tail(L)))

# print(IsPalindrom(['K', 'A', 'T', 'A', 'K']))

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