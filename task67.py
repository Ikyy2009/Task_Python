 # Fungsi untuk mengkonversi bilangan ke hexadecimal
def konversi_ke_hexadecimal(bilangan):
    # Mengonversi bilangan desimal ke hexadecimal
    return hex(bilangan)

# Contoh penggunaan
if __name__ == "__main__":
    # Meminta input bilangan desimal dari pengguna
    bilangan = int(input("Masukkan bilangan desimal: "))

    # Mengonversi bilangan ke hexadecimal
    hasil_hex = konversi_ke_hexadecimal(bilangan)

    # Menampilkan hasil konversi
    print(f"Bilangan {bilangan} dalam format hexadecimal adalah: {hasil_hex}")
