# Fungsi untuk melakukan pencarian linear
def pencarian_linear(arr, x):
    # Iterasi melalui seluruh elemen array
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Mengembalikan indeks elemen yang ditemukan
    return -1  # Mengembalikan -1 jika elemen tidak ditemukan

# Input daftar bilangan dan elemen yang dicari
arr = list(map(int, input("Masukkan daftar bilangan (pisahkan dengan spasi): ").split()))
x = int(input("Masukkan elemen yang ingin dicari: "))

# Menjalankan pencarian linear
hasil = pencarian_linear(arr, x)

# Menampilkan hasil pencarian
if hasil != -1:
    print(f"Elemen {x} ditemukan pada indeks {hasil}.")
else:
    print(f"Elemen {x} tidak ditemukan dalam daftar.")
