# Fungsi untuk menghitung luas persegi
def luas_persegi(sisi):
    # Menghitung luas persegi
    return sisi ** 2

# Contoh penggunaan
if __name__ == '__main__':
    # Input panjang sisi persegi
    sisi = float(input("Masukkan panjang sisi persegi: "))
    
    # Menghitung luas persegi
    luas = luas_persegi(sisi)
    
    # Menampilkan hasil
    print(f"Luas persegi dengan sisi {sisi} adalah {luas}")
