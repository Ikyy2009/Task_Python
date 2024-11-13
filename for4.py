jumlah = 0
for y in range(2,11,2):
    if y < 10:
        print(y,end =' + ')
    else :
        print(y,end =' = ')
    jumlah = jumlah + (y)
print(jumlah)