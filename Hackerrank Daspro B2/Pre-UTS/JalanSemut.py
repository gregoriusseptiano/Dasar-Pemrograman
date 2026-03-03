# Program     : JalanSemut.py
# Deskripsi   : Source Code Hackerrank Jalan Semut
# NIM/Nama    : 24060124120026/Gregorius Septiano Ariadi
# Tanggal     : 18/09/2024

def jalanSemut(x, y, z):
    d1 = x + y + z
    d2 = ((x + y)**2 + z**2)**0.5
    d3 = ((x + z)**2 + y**2)**0.5
    d4 = ((y + z)**2 + x**2)**0.5
    
    min_distance = min(d1, d2, d3, d4)
    
    return round(min_distance, 3)

print(jalanSemut(3,4,5))
print(jalanSemut(1,2,7))
print(jalanSemut(4,5,7))