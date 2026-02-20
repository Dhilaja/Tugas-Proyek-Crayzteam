def simpan_data(nama, kasmasuk, kaskeluar, denda, saldo):
    with open("data_kas.txt", "a", encoding="utf-8") as file:
        file.write("=== DATA TRANSAKSI KAS KELAS ===\n")
        file.write(f"Nama Siswa   : {nama}\n")
        file.write(f"Kas Masuk    : Rp {kasmasuk}\n")
        file.write(f"Kas Keluar   : Rp {kaskeluar}\n")
        file.write(f"Denda        : Rp {denda}\n")
        file.write(f"Saldo Akhir  : Rp {saldo}\n")
        file.write("-" * 40 + "\n")