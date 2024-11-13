def persegi():
    print('='*10)
    print(' PERSEGI')
    print('='*10)

    s = int(input('Masukkan sisi : '))
    luas = lambda s: s * s
    kel = lambda s: 4 * s
    print('Luas persegi : ',luas(s))
    print('Keliling persegi : ',kel(s))

persegi()