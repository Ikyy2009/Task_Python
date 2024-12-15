# Fungsi untuk mencetak pola angka segitiga terbalik
def cetak_pola_segitiga_terbalik(baris):
    for i in range(baris, 0, -1):
        # Menampilkan angka dari 1 hingga i
        for j in range(1, i + 1):
            print(j, end="")
        # Pindah ke baris berikutnya
        print()

# Input jumlah baris dari pengguna
try:
    baris = int(input("Masukkan jumlah baris segitiga terbalik: "))
    
    # Memanggil fungsi untuk mencetak pola segitiga terbalik
    cetak_pola_segitiga_terbalik(baris)
except ValueError:
    print("Masukkan jumlah baris yang valid.")
