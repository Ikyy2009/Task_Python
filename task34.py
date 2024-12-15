import datetime

# Daftar hari libur nasional (contoh: Tahun Baru, Hari Kemerdekaan, dll)
libur_nasional = [
    "01-01",  # Tahun Baru
    "17-08",  # Hari Kemerdekaan
    "25-12",  # Natal
]

# Fungsi untuk menghitung jumlah hari libur nasional
def hitung_libur_nasional(tahun):
    jumlah_libur = 0
    for libur in libur_nasional:
        # Membuat tanggal dari string tanggal yang ada di daftar
        tanggal_libur = datetime.datetime.strptime(f"{libur}-{tahun}", "%d-%m-%Y")
        
        # Mengecek apakah libur tersebut jatuh pada hari kerja
        # 5 = Sabtu, 6 = Minggu, maka jika itu Sabtu atau Minggu, kita tidak menghitung
        if tanggal_libur.weekday() < 5:  # Hari kerja adalah Senin sampai Jumat
            jumlah_libur += 1
    return jumlah_libur

# Input tahun dari pengguna
tahun = int(input("Masukkan tahun: "))

# Menghitung jumlah hari libur nasional
jumlah_libur = hitung_libur_nasional(tahun)

# Menampilkan hasil
print(f"Jumlah hari libur nasional dalam tahun {tahun} adalah: {jumlah_libur} hari")
