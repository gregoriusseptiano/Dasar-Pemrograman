print("Pilih Operasi")
print("1. Pertambahan \"+\"")
print("2. Pengurangan \"-\"")
print("3. Perkalian \"*\"")
print("4. Pembagian \"÷\"")
print("5. Perpangkatan \"**\"")
operation = input("Masukkan Jawaban :").strip().lower()

if operation == "1" or operation == "Penambahan":
    num1 =input("Nomor Pertama: ")
    num2 =input("Nomor Kedua: ")
    print("Equals to " + str(int(num1) + int(num2)))
elif operation == "2" or operation == "Pengurangan":
    num1 = input("Nomor Pertama: ")
    num2 = input("Nomor Kedua: ")
    print("Equals to " + str(int(num1) - int(num2)))
elif operation == "3" or operation == "Perkalian":
    num1 = input("Nomor Pertama: ")
    num2 = input("Nomor Kedua: ")
    print("Equals to " + str(int(num1) * int(num2)))
elif operation == "4" or operation == "Pembagaian":
    num1 = input("Nomor Pertama: ")
    num2 = input("Nomor Kedua: ")
    print("Equals to " + str(int(num1) / int(num2)))
elif operation == "5" or operation == "Perpangkatan":
    num1 = input("Nilai: ")
    num2 = input("Nilai: ")
    print("Equals to " + str(int(num1) ** int(num2)))
else:
    print("Gagal")