class Mahasiswa:
    def __init__(self, nama, nim, umur):
        self.nama = nama
        self.nim = nim
        self.umur = umur

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Umur: {self.umur} tahun")

    def ubah_umur(self, umur_baru):
        self.umur = umur_baru
