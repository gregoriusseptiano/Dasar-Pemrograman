# Program     : BelajarTenang.py
# Deskripsi   : Source Code Hackerrank Belajar Tenang
# NIM/Nama    : 24060124120026/Gregorius Septiano Ariadi
# Tanggal     : 18/09/2024

def BelajarTenang(dB, m):
    return f'{15 * 10 ** ((dB - 40) / 20):.3f} meter' if 15 * 10 ** ((dB - 40) / 20) <= m else 'Isi bensin dulu, bang'

print(BelajarTenang(102, 20000))
print(BelajarTenang(100, 1300))
print(BelajarTenang(200, 130))
