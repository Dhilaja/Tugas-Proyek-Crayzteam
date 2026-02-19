from kas_logic import hitung_denda, hitung_saldo
from data_manager import simpan_data

def main():
    print("=== SISTEM INFORMASI KAS KELAS - CrazyTeam ===")

    namasiswa = input("Masukan Nama siswa: ")
    kasmasuk = int(input("Masukan kas masuk: "))
    kaskeluar = int(input("Masukan kas keluar: "))
    haritelat = int(input("Masukan jumlah hari telat: "))

    denda = hitung_denda(haritelat)
    saldo = hitung_saldo(kasmasuk, kaskeluar, denda)

    print("Denda:", denda)
    print("Saldo akhir:", saldo)

    simpan_data(namasiswa, kasmasuk, kaskeluar, denda, saldo)

if __name__ == "__main__":
    main()
