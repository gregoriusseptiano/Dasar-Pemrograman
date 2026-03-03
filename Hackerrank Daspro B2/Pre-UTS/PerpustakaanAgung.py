# Program     : PerpustakaanAgung.py
# Deskripsi   : Source Code Hackerrank Perpustakaan Agung
# NIM/Nama    : 24060124120026/Gregorius Septiano Ariadi
# Tanggal     : 18/09/2024

def last3Week(hari):
    if hari == 'senin': return (5000 + 6000 + 4000) / 3
    elif hari == 'selasa': return (7000 + 5000 + 2000) / 3
    elif hari == 'rabu': return (4500 + 3500 + 3000) / 3
    elif hari == 'kamis': return (2900 + 2100 + 2000) / 3
    elif hari == 'jumat': return (3000 + 3000 + 3000) / 3
    elif hari == 'sabtu': return (2000 + 2500 + 2300) / 3
    elif hari == 'minggu': return (1100 + 900 + 1000) / 3

 
def estimation(D, X, Y, AS, AM, AIP):
    return (abs(Y - X) * (max(AS, AM, AIP) - min(AS, AM, AIP))) / last3Week(D)

def EstimateGreatLib(D, X, Y, SS, SR, AS, AM, AIP, R):
    if X < SR and Y > SS:
           return round((estimation(D, X, SR, AS, AM, AIP) * (R / 100)  
                      + estimation(D, SS, SR, AS, AM, AIP) + estimation(D, SS, Y, AS, AM, AIP) * (R/ 100)) / 3 , 5)
    elif X < SR and Y > SR:  
        return round((estimation(D, X, SR, AS, AM, AIP) * (R / 100)  
                      + estimation(D, SR, Y, AS, AM, AIP)) / 2 , 5)
    elif  Y > SS and X < SS: 
        return round((estimation(D, X, SS, AS, AM, AIP)  
                      + estimation(D, SS, Y, AS, AM, AIP) * (R / 100)) /2 , 5)
    elif (X < SR) or ((X > SS) and (Y < SR)) or (Y > SS):
        return round(estimation(D, X, Y, AS, AM, AIP)* (R / 100)  , 5)
    else:
        return round(estimation(D, X, Y, AS, AM, AIP) , 5)

print(EstimateGreatLib("jumat", 7, 8, 17, 6, 4000, 5500, 5000, 3))
print(EstimateGreatLib("senin", 12, 17, 18, 9, 6000, 5000, 4500, 50))
print(EstimateGreatLib("selasa", 8, 16, 20, 12, 7000, 5000, 2000, 75))