print('NILAI RAPORT')

nilai = int(input('Masukkan nilai raport :'))

if nilai >= 101:
    print('Angka tidak valid')

elif nilai >= 80:
    print('Nilai A')

elif nilai >= 70:
    print('Nilai B')

elif nilai >= 60:
    print('Nilai C')

elif nilai <= 60:
    print('Nilai D')

else :
    print('Inputan error, coba lagi')