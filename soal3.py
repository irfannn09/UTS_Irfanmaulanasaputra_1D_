jumlah=int(input('masukan jumlah barang belanjaan anda:'))
harga_barang=0
while True:
    for x in range(1,jumlah+1):
        harga=int(input(f'masukan harga barang ke{x}:'))
        harga_barang+=harga
    print(f'harga seluruh barang adalah{harga_barang}')
    blanja=input('apakah anda ingin lanjut belanja?(y/t):')
    if blanja=='t':
        break
