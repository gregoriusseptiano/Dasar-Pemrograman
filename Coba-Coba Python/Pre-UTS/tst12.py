# Nama File :
# Pembuat   :
# Tanggal   :
#Deskripsi: menentukan apakah suatu bilangan merupakan genap

#Definisi dan Spesifikasi
#IsGenap: Integer --> Boolean
#   IsGenap(x) untuk menentukan apakah bilangan x merupakan genap

#Realisasi
def IsGenap(x):
    return x % 2 == 0
def IsGanjil(y):
    return y % 4 == 3

#Aplikasi
print(IsGenap(150))
print(IsGanjil(43))
print(IsGanjil(51))