# Fungsi untuk menghitung jumlah karakter tanpa spasi
def hitung_jumlah_karakter_sans_spasi(kalimat):
    return len(kalimat.replace(" ", ""))

# Input dari pengguna
kalimat = input("Masukkan kalimat: ")

# Menghitung jumlah karakter tanpa spasi
jumlah_karakter = hitung_jumlah_karakter_sans_spasi(kalimat)

# Menampilkan hasil
print(f"Jumlah karakter tanpa spasi dalam kalimat: {jumlah_karakter}")
