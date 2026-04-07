def hitung_denda(hari_telat):
    if hari_telat > 0:
        return hari_telat * 2000
    return 0

def hitung_saldo(total_masuk, total_keluar):
    return total_masuk - total_keluar