# Fungsi untuk mengkonversi bilangan ke oktal menggunakan oct()
def konversi_ke_octal(bilangan):
    return oct(bilangan)[2:]  # oct() mengembalikan string yang dimulai dengan '0o', kita hilangkan dengan [2:]

# Input dari pengguna
bilangan = int(input("Masukkan bilangan desimal: "))

# Mengonversi ke oktal
hasil_octal = konversi_ke_octal(bilangan)

# Menampilkan hasil
print(f"Bilangan {bilangan} dalam oktal adalah: {hasil_octal}")
