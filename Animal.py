class Animal:
    # Konstruktor dengan properti
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    # Method untuk menampilkan informasi hewan
    def info_animal(self):
        print(
            f"\nNama Hewan\t\t\t: {self.nama}\n"
            f"Makanan              : {self.makanan}\n"
            f"Hidup di             : {self.hidup}\n"
            f"Berkembang biak dengan: {self.berkembang_biak}\n"
        )

# Membuat objek
kucing = Animal("Kucing", "Daging", "Darat", "Melahirkan")

# Memanggil metode info_animal untuk menampilkan informasi
kucing.info_animal()




        