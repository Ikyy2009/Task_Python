def tabung():
    print('='*10)
    print(' TABUNG')
    print('='*10)

    ka = int(input('masukkan keliling alas :'))
    la = int(input('masukkan luas alas     :'))
    t = int(input('masukkan tingginya      :'))
    r = int(input('masukkan jari jari      :'))

    phi = 22/7
    luas = lambda ka,la,t,r: 2 * phi * r * (r * t)
    volume = lambda ka,la,t,r: phi * r * r * t

    print('Luas tabung adalah :',luas(ka,la,t,r))
    print('Volume tabung adalah :',volume(ka,la,t,r))

tabung()