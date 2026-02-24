def hitung_denda(haritelat):
    if haritelat > 0:
        return haritelat * 2000
    return 0


def hitung_saldo(kasmasuk, kaskeluar, denda):
    if kasmasuk < 0 or kaskeluar < 0:
        return 0
    return kasmasuk - kaskeluar - denda


def hitung_total_kewajiban(kasmasuk, kaskeluar, haritelat):
    denda = hitung_denda(haritelat)
    saldo = hitung_saldo(kasmasuk, kaskeluar, denda)
    return saldo