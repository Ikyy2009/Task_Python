# Fungsi untuk mencetak tabel perkalian berdasarkan input pengguna
def cetak_tabel_perkalian(angka):
    print(f"Tabel Perkalian untuk {angka}:")
    for i in range(1, 11):
        print(f"{angka} x {i} = {angka * i}")

# Input dari pengguna
try:
    angka = int(input("Masukkan angka untuk mencetak tabel perkalian: "))
    cetak_tabel_perkalian(angka)
except ValueError:
    print("Masukkan angka yang valid.")
