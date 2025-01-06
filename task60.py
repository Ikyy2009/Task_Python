# Fungsi untuk menghitung nilai maksimum dan minimum
def hitung_maksimum_minimum(daftar_bilangan):
    maksimum = max(daftar_bilangan)
    minimum = min(daftar_bilangan)
    return maksimum, minimum

# Contoh penggunaan
if __name__ == "__main__":
    # Meminta input daftar bilangan dari pengguna
    daftar = list(map(int, input("Masukkan daftar bilangan (pisahkan dengan spasi): ").split()))

    # Menghitung nilai maksimum dan minimum
    maksimum, minimum = hitung_maksimum_minimum(daftar)

    print(f"Nilai maksimum: {maksimum}")
    print(f"Nilai minimum: {minimum}")
