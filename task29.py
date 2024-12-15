# Fungsi untuk menghitung kecepatan
def hitung_kecepatan(jarak, waktu):
    return jarak / waktu

# Input dari pengguna
jarak = float(input("Masukkan jarak yang ditempuh (dalam meter atau kilometer): "))
waktu = float(input("Masukkan waktu yang dibutuhkan (dalam detik atau jam): "))

# Menghitung kecepatan
kecepatan = hitung_kecepatan(jarak, waktu)

# Menampilkan hasil
print(f"Kecepatan yang ditempuh adalah: {kecepatan:.2f} unit per waktu")
