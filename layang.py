def layang():
    print('Layang-layang')

    p = int(input('masukan nilai panjang'))
    l = int(input('masukan nilai lebar'))
    d1 = int(input('masukan nilai diagonal 1'))
    d2 = int(input('masukan nilai diagonal 2'))

    luas = lambda p,l,d1,d2: d1 * d2/2
    kel = lambda p,l,d1,d2: (2 * p) + (2 * l)

    print ('luas :',luas(p,l,d1,d2))
    print ('keliling :',kel(l,p,d1,d2))

layang()