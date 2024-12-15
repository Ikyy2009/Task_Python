# Fungsi untuk mengkonversi waktu 24 jam ke 12 jam
def konversi_ke_12_jam(waktu_24_jam):
    # Membagi waktu menjadi jam dan menit
    jam, menit = map(int, waktu_24_jam.split(":"))
    
    # Menentukan AM atau PM
    if jam == 0:
        jam_12_jam = 12
        period = "AM"
    elif jam < 12:
        jam_12_jam = jam
        period = "AM"
    elif jam == 12:
        jam_12_jam = 12
        period = "PM"
    else:
        jam_12_jam = jam - 12
        period = "PM"
    
    # Mengembalikan waktu dalam format 12 jam
    return f"{jam_12_jam}:{menit:02d} {period}"

# Input waktu dalam format 24 jam
waktu_24_jam = input("Masukkan waktu dalam format 24 jam (HH:MM): ")

# Mengonversi ke format 12 jam
waktu_12_jam = konversi_ke_12_jam(waktu_24_jam)

# Menampilkan hasil
print(f"Waktu dalam format 12 jam adalah: {waktu_12_jam}")
