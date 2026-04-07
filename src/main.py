from kas_logic import hitung_denda, hitung_saldo
from data_manager import *

def menu():
    while True:
        print("\n" + "="*30)
        print("   SISTEM KAS KELAS")
        print("="*30)
        print("1. Tambah Siswa")
        print("2. Catat Pembayaran")
        print("3. Tambah Pengeluaran")
        print("4. Lihat Siswa Belum Bayar")
        print("5. Lihat Laporan Kas & Riwayat")
        print("6. Keluar")
        print("7. Hapus Siswa")
        print("-"*30)

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Nama siswa: ")
            tambah_siswa(nama)
            print(f"Siswa '{nama}' berhasil ditambahkan!")

        elif pilihan == "2":
            nama = input("Nama siswa: ")
            jumlah = int(input("Jumlah bayar: "))
            hari_telat = int(input("Hari telat: "))
            denda = hitung_denda(hari_telat)
            catat_pembayaran(nama, jumlah, denda)
            print(f"Pembayaran Berhasil! Denda: Rp{denda}")

        elif pilihan == "3":
            jumlah = int(input("Jumlah pengeluaran: "))
            tambah_pengeluaran(jumlah)
            print("Pengeluaran berhasil dicatat!")

        elif pilihan == "4":
            belum = siswa_belum_bayar()
            print("\nSiswa belum bayar:")
            for s in belum:
                print(f"- {s}")

        elif pilihan == "5":
            masuk, keluar, riwayat = laporan_kas()
            saldo = hitung_saldo(masuk, keluar)
            print("\n" + "-"*10 + " LAPORAN KAS " + "-"*10)
            print(f"Total Pemasukan  : Rp{masuk}")
            print(f"Total Pengeluaran : Rp{keluar}")
            print(f"Saldo Akhir       : Rp{saldo}")
            print("-" * 33)
            print("RIWAYAT PEMBAYARAN SISWA:")
            for r in riwayat:
                # r[0]=nama, r[1]=jumlah, r[2]=tanggal
                print(f"[{r[2]}] {r[0]} - Rp{r[1]}")

        elif pilihan == "6":
            print("Terima kasih! Program selesai.")
            break

        elif pilihan == "7":
            nama = input("Nama siswa yang ingin dihapus: ")
            hapus_siswa(nama)
            print(f"Data siswa '{nama}' telah dihapus.")

        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    menu()