# Program     : ShopSmart.py
# Deskripsi   : Source Code Hackerrank Shop Smart
# NIM/Nama    : 24060124120026/Gregorius Septiano Ariadi
# Tanggal     : 18/09/2024

def handle_diskon(total_pembayaran, kategori, iSVIP, hari):

    return (
        total_pembayaran * (0.7 if iSVIP and kategori == "elektronik" else
                            0.9 if kategori == "elektronik" else
                            0.8 if iSVIP and kategori == "pakaian" else
                            0.95 if kategori == "pakaian" else
                            0.85 if iSVIP and kategori == "makanan" else
                            0.98 if kategori == "makanan" else 1) *
        (0.95 if (iSVIP and (hari == "Jumat" or hari == "Sabtu")) or (hari == "Rabu" and kategori == "pakaian") else 1)
    )

def handle_pajak(total_pembayaran, lokasi_toko, hari):
   
    return (
        total_pembayaran * (1.2 if lokasi_toko == "luar negeri" else 1.1) *
        (1.05 if hari == "Minggu" else 1)
    )

def hargaAkhir(total_pembayaran, kategori, iSVIP, lokasi_toko, hari):
    return int(handle_pajak(handle_diskon(total_pembayaran, kategori, iSVIP, hari), lokasi_toko, hari))

print(hargaAkhir(1000000, "elektronik", True, "dalam negeri", "Senin"))
print(hargaAkhir(500000, "pakaian", False, "luar negeri", "Rabu"))
print(hargaAkhir(700000, "makanan", False, "luar negeri", "Selasa"))