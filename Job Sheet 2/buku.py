class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.status = "Tersedia"

    def tampilkan_info(self):
        print(f"Judul: {self.judul}")
        print(f"Pengarang: {self.pengarang}")
        print(f"Tahun Terbit: {self.tahun_terbit}")
        print(f"Status: {self.status}")

    def pinjam(self):
        if self.status == "Tersedia":
            self.status = "Dipinjam"
            print(f"Buku '{self.judul}' telah dipinjam.")
        else:
            print(f"Buku '{self.judul}' sedang dipinjam.")

    def kembalikan(self):
        if self.status == "Dipinjam":
            self.status = "Tersedia"
            print(f"Buku '{self.judul}' telah dikembalikan.")
        else:
            print(f"Buku '{self.judul}' tidak sedang dipinjam.")
