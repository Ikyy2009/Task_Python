# Fungsi untuk mengurutkan daftar menggunakan Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    
    # Melakukan iterasi untuk setiap elemen dalam array
    for i in range(n):
        # Melakukan iterasi dari elemen pertama hingga elemen yang belum terurut
        for j in range(0, n-i-1):
            # Membandingkan elemen yang berdekatan
            if arr[j] > arr[j+1]:
                # Menukar elemen jika urutannya salah
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Input dari pengguna
arr = list(map(int, input("Masukkan daftar bilangan yang ingin diurutkan (pisahkan dengan spasi): ").split()))

# Mengurutkan array menggunakan Bubble Sort
bubble_sort(arr)

# Menampilkan hasil pengurutan
print("Daftar bilangan setelah diurutkan:", arr)
