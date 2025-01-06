import sqlite3

# Fungsi untuk menghapus data
def hapus_data(id_data):
    try:
        # Membuka koneksi ke database
        conn = sqlite3.connect('nama_database.db')
        cursor = conn.cursor()

        # Query untuk menghapus data
        query = "DELETE FROM nama_tabel WHERE id = ?"
        
        # Mengeksekusi query dengan parameter id_data
        cursor.execute(query, (id_data,))

        # Menyimpan perubahan ke database
        conn.commit()

        print(f"Data dengan id {id_data} berhasil dihapus.")
        
    except sqlite3.Error as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        # Menutup koneksi database
        if conn:
            conn.close()

# Memanggil fungsi untuk menghapus data dengan id tertentu
hapus_data(1)
