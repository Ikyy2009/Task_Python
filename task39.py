# Fungsi untuk menghitung luas trapesium
def hitung_luas_trapesium(a, b, t):
    luas = (a + b) * t / 2
    return luas

# Input panjang sisi atas, sisi bawah, dan tinggi dari pengguna
a = float(input("Masukkan panjang sisi atas trapesium (a): "))
b = float(input("Masukkan panjang sisi bawah trapesium (b): "))
t = float(input("Masukkan tinggi trapesium (t): "))

# Menghitung luas trapesium
luas = hitung_luas_trapesium(a, b, t)

# Menampilkan hasil
print(f"Luas trapesium adalah: {luas}")
