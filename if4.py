print('~'*70)
print('\tMendapat diskon 50% jika total harga barang diatas 100rb')
print('~'*70)

harga = int(input('Masukkan harga barang:'))

if harga > 100000:
    diskon = harga * 0.50
    print('Barang mendapat diskon 50%. Total harga : ',diskon)

else :
    print('Barang tidak mendapat diskon. Total harga : ',harga)