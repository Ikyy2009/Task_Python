def bola():
    print('='*10)
    print(' BOLA')
    print('='*10)

    phi = 22/7
    r = int(input('Masukkan Jari-Jari :'))

    volume = lambda r: 4/3 * (phi * r * r * r)
    luas = lambda r: 4 * phi * r * r 

    print('Luas volume bola adalah :',luas(r))
    print('volume bola adalah :',volume(r))

bola()