def kerucut():
    print('='*10)
    print('KERUCUT')
    print('='*10)

    phi = 22/7
    r = int(input('Masukkan Jari-Jari :'))
    t = int(input('Masukkan Tinggi    :'))
    s = int(input('Masukkan Sisi      :'))

    volume = lambda r,t,s: 1/3 * phi * phi * t
    lp = lambda r,t,s: phi * (r + s)

    print('Volume kerucut adalah  :',volume(r,t,s))
    print('Luas permukaan kerucut :',lp(r,t,s))

kerucut()