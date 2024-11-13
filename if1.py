input = int(input('Tebak angka yang benar dari 1-10 :'))

angka_benar = 7

if input == angka_benar:
    print('Kamu berhasil menemukan angka')

elif input < 11:
    print('Kurang beruntung, coba lagi')

else :
    print('Inputan yang kamu masukkan salah')