nilaiA=int(input('masukan nilai A:'))
nilaiB=int(input('masukan nilai B:'))
hasil=input('penjumlahan, pengurangan, perkalian:').lower()

if hasil=='penjumlahan':
    print(nilaiA + nilaiB)
elif hasil=='pengurangan':
    print(nilaiA-nilaiB)
elif hasil=='perkalian':
    print(nilaiA*nilaiB)
else:
    print('jawban salah')