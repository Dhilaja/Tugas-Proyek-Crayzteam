import sqlite3

def connect_db():
    return sqlite3.connect('kas_kelas.db')

def buat_tabel():
    conn = connect_db()
    cursor = conn.cursor()
    # Tabel Siswa
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS siswa (
            nama TEXT PRIMARY KEY,
            bayar INTEGER DEFAULT 0,
            denda INTEGER DEFAULT 0
        )
    ''')
    # Tabel Pengeluaran (untuk mencatat total pengeluaran)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pengeluaran (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            jumlah INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Jalankan pembuatan tabel saat pertama kali import
buat_tabel()

def tambah_siswa(nama):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO siswa (nama) VALUES (?)", (nama,))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # Siswa sudah ada
    finally:
        conn.close()

def catat_pembayaran(nama, jumlah, denda):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE siswa 
        SET bayar = bayar + ?, denda = denda + ? 
        WHERE nama = ?
    """, (jumlah, denda, nama))
    conn.commit()
    conn.close()

def tambah_pengeluaran(jumlah):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pengeluaran (jumlah) VALUES (?)", (jumlah,))
    conn.commit()
    conn.close()

def siswa_belum_bayar():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT nama FROM siswa WHERE bayar = 0")
    hasil = [row[0] for row in cursor.fetchall()]
    conn.close()
    return hasil

def laporan_kas():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Hitung total pemasukan dari tabel siswa
    cursor.execute("SELECT SUM(bayar) FROM siswa")
    total_masuk = cursor.fetchone()[0] or 0
    
    # Hitung total pengeluaran
    cursor.execute("SELECT SUM(jumlah) FROM pengeluaran")
    total_keluar = cursor.fetchone()[0] or 0
    
    conn.close()
    return total_masuk, total_keluar