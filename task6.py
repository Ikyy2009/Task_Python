# Fungsi untuk mengkonversi jam ke menit
def jam_ke_menit(jam):
    menit = jam * 60
    return menit

# Input dari pengguna
try:
    jam = float(input("Masukkan jumlah jam: "))
    
    # Mengkonversi jam ke menit
    menit = jam_ke_menit(jam)
    print(f"{jam} jam = {menit} menit")
except ValueError:
    print("Masukkan angka yang valid untuk jumlah jam.")
