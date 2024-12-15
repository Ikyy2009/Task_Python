# Fungsi untuk mengkonversi suhu dari Celcius ke Kelvin
def konversi_ke_kelvin(celcius):
    kelvin = celcius + 273.15
    return kelvin

# Input suhu dalam Celcius dari pengguna
celcius = float(input("Masukkan suhu dalam Celcius: "))

# Mengonversi suhu ke Kelvin
kelvin = konversi_ke_kelvin(celcius)

# Menampilkan hasil
print(f"Suhu {celcius}°C sama dengan {kelvin:.2f} K")
