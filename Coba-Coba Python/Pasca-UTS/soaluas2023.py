from listFunctions import *
from BST_24060124120026 import *
from treeNaire_24060124120026 import *
from Lambda_24060124120026 import *

# IsExistLeft: Pohon Biner --> Boolean
# {IsExistLeft(P) mengembalikkan nilai true jika pohon memiliki subpohon kiri}
def IsExistLeft(P):
    return not IsEmpty(Left(P))

# IsExistRight: Pohon Biner --> Boolean
# {IsExistRight(P) mengembalikkan nilai true jika pohon memiliki subpohon kanan}
def IsExistRight(P):
    return not IsEmpty(Left(P))

def Konso(e, L):
    return [e] + L

def FirstElmt(L):
    if IsEmpty(L):
        return None
    else: 
        return L[0]

def Tail(L):
    if IsEmpty(L):
        return None
    else: 
        return L[1:]

def IsEmpty(L):
    return L == []

def FilterGenap(L):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L) % 2 == 0:
            return Konso(FirstElmt(L), FilterGenap(Tail(L)))
        else:
            return FilterGenap(Tail(L))

print(FilterGenap([6, 3, 1, 28, 12, 9, 4]))

def FirstList(S) :
    if IsEmpty(S):
        return []
    else:
        return S[0]

def TailList(S) :
    if IsEmpty(S):
        return []
    else:
        return S[1:]

def IsList(L) :
    return type(L) == list

def IsContainList(S):
    if IsEmpty(S):
        return False
    else: 
        if IsList(FirstList(S)):
            return True
        else:
            return IsContainList(TailList(S))

print(IsContainList([6, [3, 1], [28, 12, 9], 41]))
print(IsContainList([6, 3, 1, 28, 12, 9, 4]))

def SubMember(P, x):
    if isTreeNEmpty(P):
        return []
    elif(akar(P) == x):
        if IsList(P):
            return [akar(P), anak(P)]
        else:
            return P
    else:
        return SubMember(anak(P), x)

print(SubMember(["G",[["R",["I","U","P"]], ["E",[["T",[]],["A",['N','O']]]]]], "A"))

def MaxKabisat(P):
    if isTreeNEmpty(P):
        return False
    elif(Right(P) == []):
        x = lambda a : a % 4 == 0        
        return x(akar(P))
    else:
        return MaxKabisat(Right(P))


print(MaxKabisat([4,[2,[],[]],[9,[],[]]]))


        




    



    




