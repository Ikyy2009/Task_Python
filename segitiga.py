def segitiga():
    print('='*10)
    print('SEGITIGA')
    print('='*10)

    a = int(input('Masukkan Alas   :'))
    t = int(input('Masukkan Tinggi :'))

    luas_segitiga = lambda a,t: 1/2 * a * t

    print('Luas segitiga adalah :',luas_segitiga(a,t))

segitiga()