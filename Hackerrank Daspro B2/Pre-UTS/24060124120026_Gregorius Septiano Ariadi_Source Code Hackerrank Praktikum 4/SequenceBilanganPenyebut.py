# Program     : SequenceBilanganPenyebut.py
# Deskripsi   : Source Code Hackerrank Sequence Bilangan Penyebut
# NIM/Nama    : 24060124120026/Gregorius Septiano Ariadi
# Tanggal     : 18/09/2024

def denumeratorSeq(x):
    if (10 ** len(x) - 1) % int(x) == 0:
        return f'Ada: {(10 ** len(x) - 1) // int(x)}'
    return 'Tidak ada'
 
print(denumeratorSeq('3'))
print(denumeratorSeq('166'))
print(denumeratorSeq('5'))