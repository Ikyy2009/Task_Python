# Fungsi untuk menghitung jumlah kata dalam paragraf
def hitung_jumlah_kata(paragraf):
    # Memecah paragraf menjadi kata-kata berdasarkan spasi
    kata_list = paragraf.split()
    # Mengembalikan jumlah kata
    return len(kata_list)

# Input paragraf dari pengguna
paragraf = input("Masukkan paragraf: ")

# Menghitung jumlah kata
jumlah_kata = hitung_jumlah_kata(paragraf)

# Menampilkan hasil
print(f"Jumlah kata dalam paragraf adalah: {jumlah_kata}")
