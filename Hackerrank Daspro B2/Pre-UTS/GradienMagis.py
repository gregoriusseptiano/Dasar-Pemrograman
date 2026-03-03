# Program     : GradienMagis.py
# Deskripsi   : Source Code Hackerrank Gradien Magis
# NIM/Nama    : 24060124120026/Gregorius Septiano Ariadi
# Tanggal     : 18/09/2024

def gradien(a,b):
    return ((3*(a**2) + 2*a - 5) - ((3*(b**2)+2*b-5))) / (a-b)

print(gradien(3,1))
print(gradien(4,2))
print(gradien(7,1))