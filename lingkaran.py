def lingkaran():
    print('='*12)
    print(' LINGKARAN')
    print('='*12)

    r = int(input('Masukkan Jari-Jari : '))

    luas = lambda r: 22/7 * r * r

    print('Luas lingkaran : ',luas(r))

lingkaran()