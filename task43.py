# Fungsi untuk memeriksa tahun kabisat
def cek_tahun_kabisat(tahun):
    # Tahun kabisat jika dapat dibagi 4, kecuali tahun yang dapat dibagi 100, tetapi jika dapat dibagi 400, maka tahun tersebut kabisat
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

# Menerima input dari pengguna
tahun = int(input("Masukkan tahun: "))

# Memeriksa apakah tahun kabisat
if cek_tahun_kabisat(tahun):
    print(f"{tahun} adalah tahun kabisat.")
else:
    print(f"{tahun} bukan tahun kabisat.")
