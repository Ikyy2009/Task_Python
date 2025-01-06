from datetime import datetime

# Fungsi untuk mengonversi waktu ke format 24 jam
def konversi_ke_24_jam(waktu_str):
    # Mengonversi waktu dari format 12 jam (AM/PM) ke format 24 jam
    waktu_24_jam = datetime.strptime(waktu_str, '%I:%M %p').strftime('%H:%M')
    return waktu_24_jam

# Contoh penggunaan
if __name__ == "__main__":
    # Meminta input waktu dalam format 12 jam
    waktu_12_jam = input("Masukkan waktu (format 12 jam, contoh 02:30 PM): ")

    # Mengonversi waktu ke format 24 jam
    waktu_24_jam = konversi_ke_24_jam(waktu_12_jam)

    print(f"Waktu dalam format 24 jam adalah: {waktu_24_jam}")
