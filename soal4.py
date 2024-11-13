berat_badan=int(input('masukan berat badan anda:'))
print(f'{berat_badan}kg')
tinggi_badan=int(input('masukan tinggi badan anda:'))
print(f'{tinggi_badan}meter')
nilai_bmi=berat_badan/tinggi_badan
if nilai_bmi >18.5:
    print('berat badan anda kurang')
elif nilai_bmi <= 18.5 and nilai_bmi>29.9:
    print('berat badan normal')
elif nilai_bmi>=30:
    print('anda obesitas')
elif nilai_bmi<=25 and nilai_bmi<29.9:
    print('kelebihan bera badan')
else:
    ('mohon masukin dengan benar')