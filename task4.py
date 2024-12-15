# Input nama pengguna
nama = input("Masukkan nama Anda: ")

# Input umur pengguna
try:
    umur = int(input("Masukkan umur Anda: "))
    
    # Menampilkan nama dan umur
    print(f"Nama Anda: {nama}")
    print(f"Umur Anda: {umur} tahun")
except ValueError:
    print("Masukkan umur yang valid (angka).")
