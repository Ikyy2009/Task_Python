# Fungsi untuk mencetak pola bintang berbentuk hati
def cetak_hati():
    hati = [
        "  *****     *****  ",
        "*********   *********",
        "*********** ***********",
        "***********************",
        " *********************",
        "  *******************",
        "   *****************",
        "    ***************",
        "     *************",
        "      ***********",
        "       *********",
        "        *******",
        "         *****",
        "          ***",
        "           *"
    ]
    
    # Mencetak pola hati
    for baris in hati:
        print(baris)

# Contoh penggunaan
if __name__ == "__main__":
    cetak_hati()
