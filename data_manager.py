# data_manager.py
# File untuk menyimpan data ke dalam file txt

def simpan_data(nama, kasmasuk, kaskeluar, haritelat, denda, saldo):
    with open("data_kas.txt", "a") as file:
        file.write("=== DATA TRANSAKSI ===\n")
        file.write(f"Nama         : {nama}\n")
        file.write(f"Kas Masuk    : {kasmasuk}\n")
        file.write(f"Kas Keluar   : {kaskeluar}\n")
        file.write(f"Hari Telat   : {haritelat}\n")
        file.write(f"Denda        : {denda}\n")
        file.write(f"Saldo        : {saldo}\n")
        file.write("----------------------------\n")
