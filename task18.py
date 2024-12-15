import string

# Fungsi untuk memeriksa apakah kalimat adalah palindrome
def is_palindrome(kalimat):
    # Menghapus spasi dan tanda baca, serta mengubah semua huruf menjadi kecil
    kalimat = kalimat.lower()
    kalimat = kalimat.translate(str.maketrans('', '', string.punctuation))
    kalimat = kalimat.replace(" ", "")
    
    # Memeriksa apakah kalimat sama jika dibaca dari belakang
    return kalimat == kalimat[::-1]

# Input dari pengguna
kalimat = input("Masukkan kalimat: ")

# Memeriksa apakah kalimat palindrome
if is_palindrome(kalimat):
    print("Kalimat tersebut adalah palindrome.")
else:
    print("Kalimat tersebut bukan palindrome.")
