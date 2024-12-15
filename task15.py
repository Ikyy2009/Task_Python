# Fungsi untuk menghitung faktorial menggunakan perulangan
def hitung_faktorial(n):
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i  # Mengalikan hasil dengan angka i pada setiap iterasi
    return hasil

# Input dari pengguna
try:
    angka = int(input("Masukkan angka untuk menghitung faktorial: "))
    
    # Memeriksa jika angka negatif
    if angka < 0:
        print("Faktorial tidak terdefinisi untuk angka negatif.")
    else:
        # Menghitung dan menampilkan hasil faktorial
        faktorial = hitung_faktorial(angka)
        print(f"Faktorial dari {angka} adalah {faktorial}.")
except ValueError:
    print("Masukkan angka yang valid.")
