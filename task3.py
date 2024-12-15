# Fungsi untuk mengkonversi suhu dari Celcius ke Fahrenheit
def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

# Input dari pengguna
try:
    celcius = float(input("Masukkan suhu dalam Celcius: "))
    # Mengkonversi suhu ke Fahrenheit
    fahrenheit = celcius_ke_fahrenheit(celcius)
    print(f"{celcius}°C = {fahrenheit}°F")
except ValueError:
    print("Masukkan angka yang valid untuk suhu.")
