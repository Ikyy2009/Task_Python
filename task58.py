import datetime

# Fungsi untuk mengecek waktu dan mencetak kalimat
def salam_waktu():
    # Mendapatkan waktu saat ini
    sekarang = datetime.datetime.now()

    # Menentukan jam saat ini
    jam = sekarang.hour

    # Cek apakah waktu tersebut malam (misalnya dari jam 18 hingga 23)
    if jam >= 18:
        print("Selamat malam")
    else:
        print("Bukan waktu malam")

# Contoh penggunaan
if __name__ == "__main__":
    salam_waktu()
