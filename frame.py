class DataFrame:
    def __init__(self, frame):
        self.frame = frame
        frames = frame.split(';')
        self.serial = frames[0]
        self.nopol = frames[1]
        self.transaksi = frames[2]
        self.nip = frames[3]
        self.expired = frames[4]
        self.st_masuk = frames[5]
        self.st_kartu = frames[6]
        self.kode_gate = frames[7]
