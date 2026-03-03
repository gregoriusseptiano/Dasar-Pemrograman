# def rekursi_tanpa_basis(n):
#     return rekursi_tanpa_basis(n - 1)

# # Aplikasi
# print(rekursi_tanpa_basis(1))

def faktorial(n):
    if n!= 0: # Rekurens terjadi lebih dulu
        return n * faktorial(n - 1)
    else:     # Basis baru diperiksa setelah beberapa pemanggilan rekursif
        return 1

# Aplikasi
print(faktorial(1))
print(faktorial(3))
print(faktorial(6))


def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac (n-1)

# Aplikasi
print(fac(1))
print(fac(3))
print(fac(6))


# def fac(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fac (n+1) * (n+1)

# # Aplikasi
# print(fac(1))
# print(fac(3))
# print(fac(6))

def faciter(n, count, hasil):
    if n == count:
        return hasil * count
    else:
        return faciter(n, count + 1, hasil * count)

def fac(n):
    return faciter(n, 1, 1)

# Aplikasi
print(fac(1))
print(fac(3))
print(fac(6))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))

def plus(x,y):
    if y == 0:
        return x
    else:
        return 1 + plus(x,y-1)

print(plus(1,2))
print(plus(3,4))
print(plus(6,7))

def deret(n):
    if n == 1:
        return 1
    else:
        return n + deret(n - 1)

n = 5
print(f"S({n}) =", deret(5))

