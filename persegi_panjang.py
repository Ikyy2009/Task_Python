def persegipanjang():
    print('='*15)
    print(' PERSEGI PANJANG')
    print('='*15)

    p = int(input('Masukkan Panjang :'))
    l = int(input('Masukkan Lebar   :'))

    L = lambda p,l: p * l
    kel = lambda p,l: 2 * (p * l)

    print('Luas persegi panjang adalah      :',L(p,l))
    print('Keliling persegi panjang adalah  :',kel(p,l))

persegipanjang()