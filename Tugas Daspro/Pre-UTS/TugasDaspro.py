# Program     : TugasTipeBentukan.py
# Deskripsi   : Membuat sebuah tipe bentukan pencahan campuran dan sebuah tipe bentukan garis yang terdiri atas 2 point
# NIM/Nama    : 24060124120026/Gregorius Septiano Ariadi
# Tanggal     : 24/10/2024
# ===========================================================================
#NOMOR 1

#DEFINISI DAN SPESIFIKASI TYPE
#type Pecahan : <bil:integer, n:integer>=0, d:integer>0>
#   {<bil:integer, n:integer>=0, d:integer>0> bil merupakan bilangan bulat pecahan dapat bernilai
#positif, nol, maupun negatif. n merupakan pembilang (nominator), dapat bernilai integer positif atau nol.
#d merupakan penyebut (denonimator), hanya dapat bernilai integer positif lebih dari 0.
#pembilang selalu lebih kecil dari penyebut (n < d)}

#DEFINISI DAN SPESIFIKASI SELEKTOR
#Bil : pecahana --> integer
#   {Bil(P) memberikan bilangan bulat dari sebuah pecahan campuran}
#Realisasi dalam Phyton
def Bil(P):
    return P[0]

#Pemb : pecahana --> integer>=0
#   {Pemb(P) memberikan numerator pembilang dari pecahan campuran tersebut}
#Realisasi dalam Python
def Pemb(P):
    return P[1]

#Peny : pecahana --> integer>0
#   {Peny(P) memberikan denumerator penyebut dari pecahan campuran tersebut}
#Realisasi dalam Python
def Peny(P):
    return P[2]

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
#MakePA : integer, integer>=0, integer>0 --> pecahana
#   {MakePA(a,b,c) membentuk sebuah pecahan campuran dari bilangan a, pembilang b, dan penyebut c dengan a, b, dan c integer}
#Realisasi dalam Python
def MakePA(a,b,c):
    return [a,b,c]

#MakeP : integer, integer>0 --> pecahan
#   {MakeP(n,d) membentuk sebuah pecahan dari pembilang n dan penyebut y integer}
#Realisasi dalam Python
def MakeP(n,d):
    return [n,d]

#DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI LAIN TERHADAP PECAHAN
#KonversiPecahan : pecahana --> pecahan
#   {KonversiPecahan(P) mengubah pecahan campuran P ke tipe pecahan biasa}
#Realisasi dalam Python
def KonversiPecahan(P):
    if Bil(P) >= 0:
        return MakeP(Bil(P)*Peny(P)+Pemb(P),Peny(P))
    else:
        return MakeP(Bil(P)*Peny(P)-Pemb(P),Peny(P))

#KonversiReal : pecahana --> real
#   {KonversiReal(P) mengubah pecahan campuran P menjadi nilai real}
#Realisasi dalam Python
def KonversiReal(P):
    if Bil(P)>=0:
        return (Bil(P)*Peny(P)+Pemb(P)) / Peny(P)
    else:
        return (Bil(P)*Peny(P)-Pemb(P)) / Peny(P)

#NilaiPemb : pecahana --> integer
#   {NilaiPemb(P) mengubah pecahan campuran menjadi pembilang pecahan normal}
#Realisasi dalam Python
def NilaiPemb(P):
    if Bil(P)>=0:
        return (Bil(P)*Peny(P)+Pemb(P))
    else:
        return (Bil(P)*Peny(P)-Pemb(P))

#AddP : 2 pecahana --> pecahana
#   {AddP(P1,P2) menjumlahkan pecahan campuran P1 dan P2}
#Realisasi dalam Python
def AddP(P1,P2):
    if (KonversiReal(P1)+KonversiReal(P2))>=0:
        return MakePA((NilaiPemb(P1)*Peny(P2) + NilaiPemb(P2)*Peny(P1)) // (Peny(P1)*Peny(P2)),
        (NilaiPemb(P1)*Peny(P2) + NilaiPemb(P2)*Peny(P1)) % (Peny(P1)*Peny(P2)) , Peny(P1)*Peny(P2))
    elif -1<(KonversiReal(P1)+KonversiReal(P2))<0:
        return MakePA(0, -((abs(NilaiPemb(P1)*Peny(P2) + NilaiPemb(P2)*Peny(P1))) % (Peny(P1)*Peny(P2))),
        Peny(P1)*Peny(P2))
    elif (KonversiReal(P1)+KonversiReal(P2))<=-1:
        return MakePA(-((abs(NilaiPemb(P1)*Peny(P2) + NilaiPemb(P2)*Peny(P1))) // (Peny(P1)*Peny(P2))),
        (abs(NilaiPemb(P1)*Peny(P2) + NilaiPemb(P2)*Peny(P1))) % (Peny(P1)*Peny(P2)), (Peny(P1)*Peny(P2)))

#SubP : 2 pecahana --> pecahana
#   {SubP(P1,P2) operasi pengurangan P1 dengan P2 atau selisih}
#Realisasi dalam Python
def SubP(P1,P2):
    if  (KonversiReal(P1)-KonversiReal(P2))>=0:
        return MakePA((NilaiPemb(P1)*Peny(P2) - NilaiPemb(P2)*Peny(P1)) // (Peny(P1)*Peny(P2)),
        (NilaiPemb(P1)*Peny(P2) - NilaiPemb(P2)*Peny(P1)) % (Peny(P1)*Peny(P2)) , Peny(P1)*Peny(P2))
    elif -1<(KonversiReal(P1)-KonversiReal(P2))<0:
        return MakePA(0, -((abs(NilaiPemb(P1)*Peny(P2) - NilaiPemb(P2)*Peny(P1))) % (Peny(P1)*Peny(P2))),
        Peny(P1)*Peny(P2))
    elif (KonversiReal(P1)-KonversiReal(P2))<=-1:
        return MakePA(-((abs(NilaiPemb(P1)*Peny(P2) - NilaiPemb(P2)*Peny(P1))) // (Peny(P1)*Peny(P2))),
        (abs(NilaiPemb(P1)*Peny(P2) - NilaiPemb(P2)*Peny(P1))) % (Peny(P1)*Peny(P2)), (Peny(P1)*Peny(P2)))

#DivP : 2 pecahana --> pecahana
#   {DivP(P1,P2) membagi pecahan campuran P1 dan P2}
#Realisasi dalam Python
def DivP(P1,P2):
    if (KonversiReal(P1)/KonversiReal(P2))>=0:
        return MakePA((NilaiPemb(P1)*Peny(P2)) // (NilaiPemb(P2)*Peny(P1)), abs((NilaiPemb(P1)*Peny(P2)) % (NilaiPemb(P2)*Peny(P1))),
        abs(Peny(P1)*NilaiPemb(P2)))
    elif -1<(KonversiReal(P1)/KonversiReal(P2))<0:
        return MakePA(0,-((abs(NilaiPemb(P1)*Peny(P2))) % abs(NilaiPemb(P2)*Peny(P1))), abs(Peny(P1)*NilaiPemb(P2)))
    elif (KonversiReal(P1)/KonversiReal(P2))<=-1:
        return MakePA(-((abs(NilaiPemb(P1)*Peny(P2))) // (NilaiPemb(P2)*Peny(P1))), abs(NilaiPemb(P1)*Peny(P2)) % abs(NilaiPemb(P2)*Peny(P1)),
        abs(Peny(P1)*NilaiPemb(P2)))

#MulP : 2 pecahana --> pecahana
#   {MulP(P1,P2) mengalikan pecahan P1 dan P2}
#Realisasi dalam Python
def MulP(P1,P2):
    if (KonversiReal(P1)*KonversiReal(P2))>=0:
        return MakePA((NilaiPemb(P1)*NilaiPemb(P2)) // (Peny(P1)*Peny(P2)), (NilaiPemb(P1)*NilaiPemb(P2)) % (Peny(P1)*Peny(P2)),
        Peny(P1)*Peny(P2))
    elif -1<(KonversiReal(P1)*KonversiReal(P2))<0:
        return MakePA(0,-((abs(NilaiPemb(P1)*NilaiPemb(P2))) % Peny(P1)*Peny(P2)), Peny(P1)*Peny(P2))
    else:
        return MakePA(-((abs(NilaiPemb(P1)*NilaiPemb(P2))) // (Peny(P1)*Peny(P2))), (abs(NilaiPemb(P1)*NilaiPemb(P2))) % (Peny(P1)*Peny(P2)),
        Peny(P1)*Peny(P2))

#DEFINISI DAN SPESIFIKASI PREDIKAT
#IsEqP : 2 pecahana --> boolean
#   {IsEqP(P1,P2) bernilai benar jika P1 sama dengan P2}
#Realisasi dalam Python
def IsEqP(P1,P2):
    return NilaiPemb(P1)*Peny(P2) == NilaiPemb(P2)*Peny(P1)

#IsLtP : 2 pecahana --> boolean
#   {IsLtP(P1,P2) bernilai benar jika P1 kurang dari P2}
#Realisasi dalam Python
def IsLtP(P1,P2):
    return NilaiPemb(P1)*Peny(P2)<NilaiPemb(P2)*Peny(P1)

#IsGtP : 2 pecahana --> boolean
#   {IsGtP(P1,P2) bernilai benar jika P1 lebih dari P2}
#Realisasi dalam Python
def IsGtP(P1,P2):
    return NilaiPemb(P1)*Peny(P2)>NilaiPemb(P2)*Peny(P1)

#APLIKASI
print(AddP(MakePA(1,0,3),MakePA(0,-2,3)))
print(AddP(MakePA(5,8,11),MakePA(23,1,3)))
print(SubP(MakePA(6,3,-3),MakePA(-1,-3,3)))
print(SubP(MakePA(-2,6,3),MakePA(-1,-2,3)))
print(DivP(MakePA(2,1,8),MakePA(1,2,3)))
print(DivP(MakePA(-3,1,2),MakePA(4,1,2)))
print(MulP(MakePA(1,5,7),MakePA(2,9,3)))
print(MulP(MakePA(9,1,2),MakePA(-2,1,6)))
print(IsEqP(MakePA(1,4,10),MakePA(1,8,20)))
print(IsLtP(MakePA(-1,1,2),MakePA(3,6,8)))
print(IsGtP(MakePA(6,1,2),MakePA(-4,1,3)))