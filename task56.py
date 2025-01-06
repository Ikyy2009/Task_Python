# Fungsi untuk menghitung jumlah karakter dalam string
def hitung_karakter(string):
    return len(string)

# Contoh penggunaan
if __name__ == "__main__":
    input_string = input("Masukkan sebuah string: ")
    jumlah_karakter = hitung_karakter(input_string)
    print(f"Jumlah karakter dalam string tersebut adalah: {jumlah_karakter}")
