# Fungsi untuk menghitung suku ke-n dari barisan aritmatika
def suku_arti(a1, d, n):
    return a1 + (n - 1) * d

# Input dari pengguna
a1 = int(input("Masukkan suku pertama (a1): "))
d = int(input("Masukkan beda antar suku (d): "))
n = int(input("Masukkan urutan suku yang ingin dicari (n): "))

# Menghitung suku ke-n
hasil = suku_arti(a1, d, n)

print(f"Suku ke-{n} dari barisan aritmatika adalah: {hasil}")
