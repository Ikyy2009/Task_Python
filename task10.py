# Fungsi untuk memeriksa apakah suatu tahun kabisat
def cek_tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

# Input dari pengguna
try:
    tahun = int(input("Masukkan tahun: "))
    
    # Memeriksa apakah tahun tersebut kabisat
    if cek_tahun_kabisat(tahun):
        print(f"Tahun {tahun} adalah tahun kabisat.")
    else:
        print(f"Tahun {tahun} bukan tahun kabisat.")
except ValueError:
    print("Masukkan tahun yang valid.")
