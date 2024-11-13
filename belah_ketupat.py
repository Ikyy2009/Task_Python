def Belah_Ketupat():
    print('='*10)
    print('BELAH KETUPAT')
    print('='*10)

    d1 = int(input('Masukkan Diagonal 1 :'))
    d2 = int(input('Masukkan Diagonal 2 :'))
    s = int(input('Masukkan Sisi        :'))

    l = lambda d1,d2,s: 1/2 * d1 * d2
    k = lambda d1,d2,s: 4 * s

    print('Luas belah ketupat adalah        :',l(d1,d2,s))
    print('Keliling belah ketupat adalah    :',k(d1,d2,s))

Belah_Ketupat()