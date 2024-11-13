jumlah = 0
for y in range(1,6):
    if y < 5:
        print(y,end =' + ')
    else :
        print(y,end =' = ')
    jumlah = jumlah + (y)
print(jumlah)