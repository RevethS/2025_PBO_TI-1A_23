class Motor:
    def __init__(self, plat_nomor, merk, warna):
        self.plat_nomor = plat_nomor
        self.merk = merk
        self.warna = warna

    def tampilkan_info(self):
        return f"Motor {self.merk} ({self.warna}) - Plat: {self.plat_nomor}"

class Parkir:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.kendaraan = []

    def tambah_motor(self, motor):
        if len(self.kendaraan) < self.kapasitas:
            self.kendaraan.append(motor)
            return f"Motor {motor.plat_nomor} masuk parkiran."
        else:
            return "Parkiran penuh!"

    def keluar_motor(self, plat_nomor):
        for motor in self.kendaraan:
            if motor.plat_nomor == plat_nomor:
                self.kendaraan.remove(motor)
                return f"Motor {plat_nomor} keluar dari parkiran."
        return "Motor tidak ditemukan di parkiran."

    def tampilkan_kendaraan(self):
        if not self.kendaraan:
            return "Parkiran kosong."
        return "\n".join([motor.tampilkan_info() for motor in self.kendaraan])