def prisma_segi_lima():
    print('='*10)
    print('PRISMA SEGI LIMA')
    print('='*10)

    la = int(input('Masukkan luas alas      :'))
    ls = int(input('Masukkan luas selimut   :'))

    lp = lambda la,ls: 2 * la * ls

    print('Luas permukaan prisma segi lima :',lp(la,ls))

prisma_segi_lima()