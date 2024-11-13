tahun=int(input('masukan tahun:'))
if tahun / 400*100==0:
    print('tahun tersebut adalah kabisat')
elif tahun / 4 > 100:
    print('tahun tersebut bukan tahun kabisat')
else:
    print('masukan tahun dengan benar')