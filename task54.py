import datetime
import calendar

# Fungsi untuk menghitung jumlah hari libur
def hitung_libur(tahun):
    # Daftar hari libur tetap
    libur_tetap = [
        datetime.date(tahun, 1, 1),   # Tahun Baru
        datetime.date(tahun, 5, 1),   # Hari Buruh
        datetime.date(tahun, 8, 17),  # Hari Kemerdekaan
        datetime.date(tahun, 12, 25), # Hari Natal
    ]
    
    jumlah_libur = 0

    # Memeriksa setiap bulan dalam tahun
    for bulan in range(1, 13):  # Untuk setiap bulan
        # Mendapatkan jumlah hari dalam bulan tersebut
        jumlah_hari = calendar.monthrange(tahun, bulan)[1]

        for hari in range(1, jumlah_hari + 1):  # Untuk setiap hari dalam bulan tersebut
            # Membuat objek tanggal
            tanggal = datetime.date(tahun, bulan, hari)

            # Memeriksa apakah tanggal adalah hari libur tetap
            if tanggal in libur_tetap:
                jumlah_libur += 1
            # Memeriksa apakah tanggal adalah akhir pekan (Sabtu atau Minggu)
            elif tanggal.weekday() == 5 or tanggal.weekday() == 6:
                jumlah_libur += 1

    return jumlah_libur

# Contoh penggunaan
if __name__ == "__main__":
    tahun = int(input("Masukkan tahun untuk menghitung hari libur: "))
    total_libur = hitung_libur(tahun)
    print(f"Jumlah hari libur di tahun {tahun} adalah {total_libur} hari.")
