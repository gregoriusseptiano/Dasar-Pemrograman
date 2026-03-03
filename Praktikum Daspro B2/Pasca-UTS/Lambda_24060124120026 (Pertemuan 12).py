lambda x: x % 2 == 0
lambda x, y: x if x > y else y

usia = [5, 10, 18, 20]
kategori = list(map(lambda x: x >= 18, usia))

for i in kategori:
    if i:
        print("Dewasa")
    else:
        print("Anak")

