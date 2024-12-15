# Fungsi untuk menghitung volume kubus
def hitung_volume_kubus(sisi):
    volume = sisi ** 3  # Volume kubus = sisi^3
    return volume

# Input dari pengguna
try:
    sisi = float(input("Masukkan panjang sisi kubus: "))
    
    # Memastikan sisi kubus lebih besar dari 0
    if sisi <= 0:
        print("Panjang sisi harus lebih besar dari 0.")
    else:
        # Menghitung volume kubus
        volume = hitung_volume_kubus(sisi)
        print(f"Volume kubus dengan sisi {sisi} adalah {volume}")
except ValueError:
    print("Masukkan angka yang valid untuk panjang sisi.")
