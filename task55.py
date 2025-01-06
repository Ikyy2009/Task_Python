# Fungsi untuk mengkonversi bilangan desimal ke biner
def desimal_ke_biner(bilangan):
    return bin(bilangan)[2:]  # Menghilangkan prefix '0b'

# Fungsi untuk mengkonversi bilangan desimal ke oktal
def desimal_ke_oktal(bilangan):
    return oct(bilangan)[2:]  # Menghilangkan prefix '0o'

# Fungsi untuk mengkonversi bilangan desimal ke heksadesimal
def desimal_ke_heksadesimal(bilangan):
    return hex(bilangan)[2:].upper()  # Menghilangkan prefix '0x' dan membuat huruf kapital

# Contoh penggunaan
if __name__ == "__main__":
    bilangan = int(input("Masukkan bilangan desimal: "))

    print(f"Bilangan desimal {bilangan} dalam biner adalah: {desimal_ke_biner(bilangan)}")
    print(f"Bilangan desimal {bilangan} dalam oktal adalah: {desimal_ke_oktal(bilangan)}")
    print(f"Bilangan desimal {bilangan} dalam heksadesimal adalah: {desimal_ke_heksadesimal(bilangan)}")
