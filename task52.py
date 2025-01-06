import calendar

# Fungsi untuk mencetak kalender bulan
def cetak_kalender_bulan(tahun, bulan):
    # Mencetak kalender bulan yang diberikan
    print(calendar.month(tahun, bulan))

# Contoh penggunaan
if __name__ == '__main__':
    # Input tahun dan bulan
    tahun = int(input("Masukkan tahun (misal 2025): "))
    bulan = int(input("Masukkan bulan (1-12): "))
    
    # Mencetak kalender bulan
    cetak_kalender_bulan(tahun, bulan)
