# Fungsi untuk menghitung luas persegi
def luas_persegi(sisi):
    return sisi ** 2

# Menerima input dari pengguna
sisi = float(input("Masukkan panjang sisi persegi: "))

# Menghitung luas persegi
luas = luas_persegi(sisi)

# Menampilkan hasil
print(f"Luas persegi dengan sisi {sisi} adalah: {luas}")
