class Mobil:
    def __init__(self, merk, warna, tahun, harga):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun
        self.harga = harga

    def tampilkan_info(self):
        print(f"Mobil {self.merk} berwarna {self.warna}, tahun {self.tahun}, harga: Rp {self.harga}")

    def diskon(self, persen_diskon):
        diskon_harga = self.harga * (persen_diskon / 100)
        harga_setelah_diskon = self.harga - diskon_harga
        print(f"Harga setelah diskon {persen_diskon}%: Rp {harga_setelah_diskon}")

    def hitung_usia(self, tahun_sekarang):
        return tahun_sekarang - self.tahun

    def perbarui_harga(self, harga_baru, tahun_baru):
        self.harga = harga_baru
        self.tahun = tahun_baru
        print(f"Harga dan tahun mobil {self.merk} diperbarui menjadi Rp {self.harga} dan tahun {self.tahun}")
