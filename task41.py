# Fungsi untuk mencetak pola bintang berbentuk hati
def pola_hati():
    baris = 6  # Jumlah baris untuk pola hati
    for i in range(baris // 2, baris, 2):
        # Cetak spasi di awal
        for j in range(1, baris - i, 2):
            print(" ", end="")
        
        # Cetak bintang pertama
        for j in range(1, i + 1, 1):
            print("*", end="")
        
        # Cetak spasi di tengah
        for j in range(1, baris - i, 1):
            print(" ", end="")
        
        # Cetak bintang kedua
        for j in range(1, i + 1, 1):
            print("*", end="")
        
        print()
    
    # Bagian bawah hati (segitiga)
    for i in range(baris, 0, -1):
        # Cetak spasi di awal
        for j in range(i, baris, 1):
            print(" ", end="")
        
        # Cetak bintang
        for j in range(1, (i * 2) - 1, 1):
            print("*", end="")
        
        print()

# Menampilkan pola hati
pola_hati()
