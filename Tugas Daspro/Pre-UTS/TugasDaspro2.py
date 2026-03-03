#NOMOR 2

#DEFINISI DAN SPESIFIKASI TYPE
#type point : <x:integer,y:integer>
#   {<x:integer,y:integer x adalah acuan titik pada sumbu-x dan y adalah acuan titik pada sumbu-y}

#type garis : <P1: point,P2: point>
#   {<P1: point,P2: point> menarik garis antara P1 dan P2}

#DEFINISI DAN SPESIFIKASI SELEKTOR
# Point1 : garis --> point
#   {Point1(L) memberikan point titik pertama dari sebuah garis}
#Realisasi dalam Python
def Point1(L):
    return L [0]

# Point2 : garis --> point
#   {Point2(L) memberikan point titik kedua dari sebuah garis}
#Realisasi dalam Python
def Point2(L):
    return L [1]

#X : point --> real
#   {X(P) memberikan acuan titik pada sumbu-x}
#Realisasi dalam Python
def X(P):
    return P [0]

#Y : point --> real
#   {Y(P) memberikan acuan titik pada sumbu-y}
#Realisasi dalam Python
def Y(P):
    return P [1]

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
#MakePoint : 2 integer --> point
#   {MakePoint(x,y) membentuk suatu point di sumbu-x dan sumbu-y}
#Realisasi dalam Python
def MakePoint(x,y):
    return [x,y]

#MakeLine : 2 point --> garis
#   {MakeLine(P1,P2) membentuk suatu garis antara point P1 dan point P2}
#Realisasi dalam Python
def MakeLine(P1,P2):
    return [P1,P2]

#DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI LAIN TERHADAP GARIS
#PanjangGaris : garis --> real
#   {PanjangGaris(L) menghitung panjang garis dari titik P1 ke titik P2}
#Realisasi dalam Python
def PanjangGaris(L):
    return ((X(Point2(L)) - (X(Point1(L))))**2 + (Y(Point2(L)) - Y(Point1(L)))**2)**0.5

#gradien : garis --> real
#   {gradien(L) menghitung gradien dari suatu garis}
def gradien(L):
    return (Y(Point2(L)) - Y(Point1(L))) / (X(Point2(L)) - X(Point1(L)))

#DEFINISI DAN SPESIFIKASI PREDIKAT
#IsSejajar : 2 garis --> boolean
#   {IsSejajar(L1,L2) benar jika gradien L1 = gradien L2}
#Realisasi dalam Python
def IsSejajar(L1,L2):
    return gradien(L1) == gradien(L2)

#IsTegakLurus : 2 garis --> boolean
#   {IsTegakLurus(L1,L2) benar jika gradien L1 x gradien L2 = -1}
#Realisasi dalam Python
def IsTegakLurus(L1,L2):
    return gradien(L1)*gradien(L2)==-1

#APLIKASI
print(PanjangGaris(MakeLine(MakePoint(0,0),MakePoint(7,0))))
print(PanjangGaris(MakeLine(MakePoint(1,1),MakePoint(8,1))))
print(gradien(MakeLine(MakePoint(0,0),MakePoint(2,2))))
print(gradien(MakeLine(MakePoint(1,1),MakePoint(3,3))))
print(IsSejajar(MakeLine(MakePoint(0,0),MakePoint(3,3)),MakeLine(MakePoint(1,0),MakePoint(4,3))))
print(IsSejajar(MakeLine(MakePoint(1,1),MakePoint(4,4)),MakeLine(MakePoint(2,1),MakePoint(5,4))))
print(IsTegakLurus(MakeLine(MakePoint(1,1),MakePoint(4,4)),MakeLine(MakePoint(1,-1),MakePoint(2,-2))))
print(IsTegakLurus(MakeLine(MakePoint(2,2),MakePoint(5,5)),MakeLine(MakePoint(2,0),MakePoint(3,-1))))