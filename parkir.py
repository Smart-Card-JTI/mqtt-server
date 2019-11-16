class Parkir:
    def __init__(self, serial, kode_gate, no_kendaraan, tanggal_transaksi,
                 tanggal_expired,
                 summary, status):
        self.serial = serial
        self.kode_gate = kode_gate
        self.no_kendaraan = no_kendaraan
        self.tanggal_transaksi = tanggal_transaksi
        self.tanggal_expired = tanggal_expired
        self.summary = summary
        self.status = status
