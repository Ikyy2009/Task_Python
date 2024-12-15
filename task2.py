import datetime

# Mendapatkan tanggal dan waktu saat ini
waktu_sekarang = datetime.datetime.now()

# Menampilkan tanggal dan waktu dalam format default
print("Tanggal dan waktu saat ini:", waktu_sekarang)

# Menampilkan tanggal dan waktu dengan format yang lebih spesifik
print("Tanggal dan waktu (DD-MM-YYYY HH:MM:SS):", waktu_sekarang.strftime("%d-%m-%Y %H:%M:%S"))
