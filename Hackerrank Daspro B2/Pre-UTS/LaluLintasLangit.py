# Program     : LaluLintasLangit.py
# Deskripsi   : Source Code Hackerrank Lalu Lintas Langit
# NIM/Nama    : 24060124120026/Gregorius Septiano Ariadi
# Tanggal     : 18/09/2024

def monitor_pesawat(x,y,z):
    if y > 900 or y < 200:
        return "Kecepatan Berbahaya"
    elif z < 20:
        return "Bahan Bakar Rendah"
    elif x > 12000: 
        return "Terlalu Tinggi"
    elif x < 5000 and 200 < y < 900 and z > 50:
        return "Aman untuk Mendarat"
    else: 
        return "Berjalan Normal"
    
print(monitor_pesawat(4000,850,55))
print(monitor_pesawat(5000,950,70))
print(monitor_pesawat(2000,850,2))