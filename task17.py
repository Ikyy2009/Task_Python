# Meminta input dari pengguna
kalimat = input("Masukkan kalimat: ")

# Menggunakan metode split() untuk memisahkan kalimat menjadi kata-kata
kata_kata = kalimat.split()

# Menghitung jumlah kata
jumlah_kata = len(kata_kata)

# Menampilkan hasil
print("Jumlah kata dalam kalimat:", jumlah_kata)
