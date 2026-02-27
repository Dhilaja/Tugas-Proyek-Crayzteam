import sqlite3  # Library bawaan Python untuk menggunakan database SQLite

def connect_db():
    return sqlite3.connect('kas_kelas.db')  # Menghubungkan / membuat file database kas_kelas.db

def buat_tabel():
    conn = connect_db()  # Membuka koneksi ke database
    cursor = conn.cursor()  # Membuat cursor untuk menjalankan perintah SQL

    # Tabel Siswa
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS siswa (  # Membuat tabel siswa jika belum ada
            nama TEXT PRIMARY KEY,          # Kolom nama (unik, tidak boleh sama)
            bayar INTEGER DEFAULT 0,        # Total uang yang dibayar (default 0)
            denda INTEGER DEFAULT 0         # Total denda (default 0)
        )
    ''')

    # Tabel Pengeluaran
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pengeluaran (  # Membuat tabel pengeluaran jika belum ada
            id INTEGER PRIMARY KEY AUTOINCREMENT, # ID unik bertambah otomatis
            jumlah INTEGER                        # Jumlah uang yang keluar
        )
    ''')

    conn.commit()  # Menyimpan perubahan ke database
    conn.close()   # Menutup koneksi database

# Jalankan pembuatan tabel saat pertama kali import
buat_tabel()  # Supaya tabel otomatis dibuat saat file dijalankan

def tambah_siswa(nama):
    conn = connect_db()  # Buka koneksi database
    cursor = conn.cursor()  # Buat cursor

    try:
        cursor.execute("INSERT INTO siswa (nama) VALUES (?)", (nama,))  # Tambah siswa baru
        conn.commit()  # Simpan perubahan
    except sqlite3.IntegrityError:
        pass  # Jika nama sudah ada (PRIMARY KEY), abaikan agar tidak error
    finally:
        conn.close()  # Tutup koneksi (pasti dijalankan)

def catat_pembayaran(nama, jumlah, denda):
    conn = connect_db()  # Buka koneksi
    cursor = conn.cursor()  # Buat cursor

    cursor.execute("""
        UPDATE siswa 
        SET bayar = bayar + ?, denda = denda + ?  # Menambahkan pembayaran & denda
        WHERE nama = ?                            # Berdasarkan nama siswa
    """, (jumlah, denda, nama))

    conn.commit()  # Simpan perubahan
    conn.close()   # Tutup koneksi

def tambah_pengeluaran(jumlah):
    conn = connect_db()  # Buka koneksi
    cursor = conn.cursor()  # Buat cursor

    cursor.execute("INSERT INTO pengeluaran (jumlah) VALUES (?)", (jumlah,))  # Tambah data pengeluaran
    conn.commit()  # Simpan perubahan
    conn.close()   # Tutup koneksi

def siswa_belum_bayar():
    conn = connect_db()  # Buka koneksi
    cursor = conn.cursor()  # Buat cursor

    cursor.execute("SELECT nama FROM siswa WHERE bayar = 0")  # Ambil siswa yang belum bayar
    hasil = [row[0] for row in cursor.fetchall()]  # Ubah hasil query jadi list nama

    conn.close()  # Tutup koneksi
    return hasil  # Kembalikan daftar siswa

def laporan_kas():
    conn = connect_db()  # Buka koneksi
    cursor = conn.cursor()  # Buat cursor

    cursor.execute("SELECT SUM(bayar) FROM siswa")  # Hitung total pemasukan
    total_masuk = cursor.fetchone()[0] or 0  # Ambil hasil, jika None jadi 0

    cursor.execute("SELECT SUM(jumlah) FROM pengeluaran")  # Hitung total pengeluaran
    total_keluar = cursor.fetchone()[0] or 0  # Ambil hasil, jika None jadi 0

    conn.close()  # Tutup koneksi
    return total_masuk, total_keluar  # Kembalikan total masuk & keluar