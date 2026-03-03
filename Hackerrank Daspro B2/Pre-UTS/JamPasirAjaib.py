# Program     : JamPasirAjaib.py
# Deskripsi   : Source Code Hackerrank Jam Pasir Ajaib
# NIM/Nama    : 24060124120026/Gregorius Septiano Ariadi
# Tanggal     : 18/09/2024

def jam(j,m,s):
    if 0 <= j and j >= 24 and 0 <= m and m >= 60 and 0 <= s or s >= 60:
        return "Waktu tidak valid"
    else: return (f"Jam: {j}, Menit: {m}, Detik: {s}")
    
print(jam(12,30,45))
print(jam(12,45,60))
print(jam(12,16,45))
    