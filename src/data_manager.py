import sqlite3
from datetime import datetime

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
            denda INTEGER DEFAULT 0,
            tanggal_bayar TEXT
        )
    ''')
    
    # --- LOGIKA ANTI ERROR (Migrasi Kolom) ---
    try:
        cursor.execute("ALTER TABLE siswa ADD COLUMN tanggal_bayar TEXT")
    except sqlite3.OperationalError:
        pass # Kolom sudah ada, abaikan error

    # Tabel Pengeluaran
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pengeluaran (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            jumlah INTEGER,
            tanggal_keluar TEXT
        )
    ''')
    
    try:
        cursor.execute("ALTER TABLE pengeluaran ADD COLUMN tanggal_keluar TEXT")
    except sqlite3.OperationalError:
        pass # Kolom sudah ada, abaikan error

    conn.commit()
    conn.close()

buat_tabel()

def tambah_siswa(nama):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO siswa (nama) VALUES (?)", (nama,))
        conn.commit()
    except sqlite3.IntegrityError:
        pass 
    finally:
        conn.close()

def hapus_siswa(nama):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM siswa WHERE nama = ?", (nama,))
    conn.commit()
    conn.close()

def catat_pembayaran(nama, jumlah, denda):
    conn = connect_db()
    cursor = conn.cursor()
    waktu = datetime.now().strftime("%A, %d-%m-%Y %H:%M")
    cursor.execute("""
        UPDATE siswa 
        SET bayar = bayar + ?, denda = denda + ?, tanggal_bayar = ? 
        WHERE nama = ?
    """, (jumlah, denda, waktu, nama))
    conn.commit()
    conn.close()

def tambah_pengeluaran(jumlah):
    conn = connect_db()
    cursor = conn.cursor()
    waktu = datetime.now().strftime("%A, %d-%m-%Y %H:%M")
    cursor.execute("INSERT INTO pengeluaran (jumlah, tanggal_keluar) VALUES (?, ?)", (jumlah, waktu))
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
    cursor.execute("SELECT SUM(bayar) FROM siswa")
    total_masuk = cursor.fetchone()[0] or 0
    cursor.execute("SELECT SUM(jumlah) FROM pengeluaran")
    total_keluar = cursor.fetchone()[0] or 0
    
    cursor.execute("SELECT nama, bayar, tanggal_bayar FROM siswa WHERE bayar > 0")
    riwayat_siswa = cursor.fetchall()
    
    conn.close()
    return total_masuk, total_keluar, riwayat_siswa