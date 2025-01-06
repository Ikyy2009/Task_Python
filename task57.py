# Fungsi untuk menghitung luas trapesium
def luas_trapesium(a, b, t):
    return (a + b) * t / 2

# Contoh penggunaan
if __name__ == "__main__":
    # Input panjang sisi atas, sisi bawah, dan tinggi trapesium
    a = float(input("Masukkan panjang sisi atas trapesium: "))
    b = float(input("Masukkan panjang sisi bawah trapesium: "))
    t = float(input("Masukkan tinggi trapesium: "))

    # Menghitung luas trapesium
    luas = luas_trapesium(a, b, t)

    print(f"Luas trapesium dengan sisi atas {a}, sisi bawah {b}, dan tinggi {t} adalah: {luas}")
