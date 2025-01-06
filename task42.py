# Menerima input dari pengguna
angka_input = input("Masukkan angka-angka (pisahkan dengan koma): ")
angka = [int(x) for x in angka_input.split(",")]

# Menghitung nilai maksimum dan minimum
nilai_maksimum = max(angka)
nilai_minimum = min(angka)

# Menampilkan hasil
print(f"Nilai maksimum: {nilai_maksimum}")
print(f"Nilai minimum: {nilai_minimum}")
