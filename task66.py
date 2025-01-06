import datetime

# Fungsi untuk mencetak salam berdasarkan waktu
def cetak_salam():
    # Mendapatkan waktu saat ini
    sekarang = datetime.datetime.now()

    # Menentukan jam saat ini
    jam = sekarang.hour

    # Menentukan salam berdasarkan jam
    if jam < 12:
        print("Selamat pagi")
    elif jam < 18:
        print("Selamat siang")
    else:
        print("Selamat malam")

# Contoh penggunaan
if __name__ == "__main__":
    cetak_salam()
