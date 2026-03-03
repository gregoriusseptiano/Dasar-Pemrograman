#PERPUSTAKAAN AGUNG
# from LOL import *
# from list import *


# type shelf: <tag: string,
#               book: list of string>

# koleksi objek
# type shelves: <rakbuku: list of shelf>

# NOTE: tag dan book adalah komponen dari shelf
#       shelf adalah elemen dari shelves 

# --------------- LIBRARY LoL AND List ------------------

def MakeList(a):
    return [a]

def Konso(e, L):
    return [e] + L

def Konsi(L, e):
    return L + [e]

def concatList(L1, L2):
    return L1 + L2

def FirstElmt(L):
    return L[0]

def LastElmt(L):
    return L[-1]

def Head(L):
    return L[:-1]

def Tail(L):
    return L[1:]

def IsEmpty(L):
    return L == []

def FirstList(LoL):
    return LoL[0]

def LastList(LoL):
    return LoL[-1]

def HeadList(LoL):
    return LoL[:-1]

def TailList(LoL):
    return LoL[1:]

def IsEmpty(LoL):
    if LoL == []:
        return True
    else:
        return False

def IsAtom(LoL):
    if type(LoL) == list:
             return False
    else:
        return True

def IsList(LoL):
    if IsAtom(LoL) == False:
        return True
    else:
        return False

# --------------- FUNCTION USED IN ADDBOOKS --------------

# SELEKTOR
def getTag(shelf):
    return FirstElmt(FirstList(shelf))

def getBooks(shelf):
    return LastElmt(FirstList(shelf))

# FUNGSI KHUSUS
# bersifat opsional, tidak harus digunakan
# boleh buat fungsi antara sendiri

def Konkat(L1,L2):
    if IsEmpty(L1):
        return L2
    else:
        return Konkat(Head(L1), Konso(LastElmt(L1),L2))

# makeShelf: string, list -> shelf
# fungsi ini membuat sebuah shelf baru dengan komponen tag dan book
def makeShelf(tag, book):
    return [[tag] + [book]]

# AddToShelf: string, list -> shelf
# fungsi ini menambahkan buku ke sebuah shelf dengan tag tertentu
def AddToShelf(tag, book):
    return [tag] + [book]

def MasukanRak(shelves,book):
    return AddToShelf(getTag(shelves),Konkat(getBooks(shelves),book))
# ----------------- FUNCTION ------------------------

# AddBooks: shelves, string, list -> shelves
# fungsi ini mengeluarkan shelves yang sudah ada dengan menambahkan buku ke sebuah shelf dengan tag tertentu
def AddBooks(shelves, tag, book):
    if IsEmpty(book):
        return shelves
    elif IsEmpty(shelves):
            return Konsi(shelves, AddToShelf(tag,book))
    else:
        if getTag(shelves) == tag:
            return Konso(MasukanRak(shelves,book), TailList(shelves))
        elif getTag(shelves) != tag:
            return Konso(FirstList(shelves), AddBooks(TailList(shelves), tag, book))
        
# ----------------- APLIKASI ------------------------

# print(eval(input()))
print(MasukanRak([['Self Development', ['The 5 AM Club']], ['Biologi', ['Sobotta']], ['Novel', ['Bumi', 'Matahari']], ['Komputer', ['BCI', 'DSA', 'HCI']]], ['A Brief History of Time']))
print(AddBooks([['Self Development', ['The 5 AM Club']], ['Biologi', ['Sobotta']], ['Novel', ['Bumi', 'Matahari']], ['Komputer', ['BCI', 'DSA', 'HCI']]], "Fisika", ['A Brief History of Time']))
print(AddBooks([['Cerita Anak', ['Matilda', 'Peter Pan']], ['Self Development', ['Atomic Habits', 'The 5 AM Club']]], "Self Development", ['Outliers']))
# SEMANGAT ^^

#Petualangan di Dunia Lumerion
def IsEmpty(S):
    return S == []

def FirstList(S):
    return S[0]

def LastList(S):
    return S[-1]

def TailList(S):
    return S[1:]

def EvaluateExpression(A):
    if IsEmpty(A):
        return []
    elif FirstList(A) == '+':
        return FirstList(TailList(A)) + LastList(A)
    elif FirstList(A) == '-':
        return FirstList(TailList(A)) - LastList(A)
    elif FirstList(A) == '*':
        return FirstList(TailList(A)) * LastList(A)
    elif FirstList(A) == '/':
        return FirstList(TailList(A)) / LastList(A)
    
# print(eval(input()))