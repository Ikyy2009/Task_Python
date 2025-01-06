# Fungsi untuk menentukan apakah bilangan ganjil atau genap
def cek_ganjil_genap(bilangan):
    if bilangan % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

# Contoh penggunaan
if __name__ == "__main__":
    bilangan = int(input("Masukkan sebuah bilangan: "))

    hasil = cek_ganjil_genap(bilangan)
    print(f"Bilangan {bilangan} adalah {hasil}.")
