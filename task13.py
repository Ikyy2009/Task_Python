# Variabel untuk menyimpan jumlah bilangan ganjil
jumlah_ganjil = 0

# Perulangan untuk memeriksa setiap angka dari 1 hingga 100
for i in range(1, 101):
    if i % 2 != 0:  # Mengecek apakah angka adalah ganjil
        jumlah_ganjil += i  # Menambahkan angka ganjil ke jumlah

# Menampilkan hasil
print(f"Jumlah bilangan ganjil dari 1 hingga 100 adalah: {jumlah_ganjil}")
