# Fungsi untuk menghitung jumlah bilangan ganjil dalam rentang
def jumlah_bilangan_ganjil(start, end):
    count = 0
    for angka in range(start, end + 1):  # Rentang termasuk angka 'end'
        if angka % 2 != 0:  # Jika angka adalah ganjil
            count += 1
    return count

# Menerima input dari pengguna
start = int(input("Masukkan angka mulai: "))
end = int(input("Masukkan angka akhir: "))

# Menghitung jumlah bilangan ganjil dalam rentang
jumlah_ganjil = jumlah_bilangan_ganjil(start, end)

# Menampilkan hasil
print(f"Jumlah bilangan ganjil dalam rentang {start} sampai {end} adalah: {jumlah_ganjil}")
