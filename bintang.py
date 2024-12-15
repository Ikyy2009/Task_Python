# Fungsi untuk mencetak pola bintang
def cetak_pola_bintang(baris):
    for i in range(1, baris + 1):
        print('*' * i)

# Input jumlah baris dari pengguna
try:
    baris = int(input("Masukkan jumlah baris pola bintang: "))
    if baris <= 0:
        print("Jumlah baris harus lebih besar dari 0.")
    else:
        # Mencetak pola bintang
        cetak_pola_bintang(baris)
except ValueError:
    print("Masukkan angka yang valid untuk jumlah baris.")
