def balok():    
    print('='*10)
    print(' BALOK')
    print('='*10)

    l = int(input('Masukkan Lebar  :'))
    p = int(input('Masukkan Panjang:'))
    t = int(input('Masukkan Tinggi :'))

    lp = lambda l,p,t: 2 * (p * l + p * t + l * t)
    vb = lambda l,p,t: p * l * t

    print("luas permukaan balok adalah :",lp(l,p,t))
    print("Volume balok adalh :",vb(l,p,t))

balok()