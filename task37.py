# Fungsi untuk mencetak pola angka piramida terbalik
def piramida_terbalik(n):
    for i in range(n, 0, -1):  # Mulai dari baris n, turun hingga baris 1
        # Mencetak spasi untuk perataan
        print(" " * (n - i), end="")
        # Mencetak angka dalam satu baris
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()  # Pindah ke baris berikutnya

# Input jumlah baris dari pengguna
n = int(input("Masukkan jumlah baris: "))

# Menampilkan pola piramida terbalik
piramida_terbalik(n)
