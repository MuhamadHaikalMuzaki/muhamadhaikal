from Animal import Animal

class Bird(Animal):
    # Konstruktor dengan properti tambahan
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.paruh = paruh

    # Method untuk menampilkan informasi burung
    def info_bird(self):
        super().info_animal()
        print(
            f"\nWarna\t\t\t: {self.warna}\n"
            f"\nJenis Paruh\t\t: {self.paruh}\n"
        )

elang = Bird("Elang", "Daging", "Di tebing", "Menghasilkan telur", "Coklat", "Bangkok dan Lancip")

print("## Informasi Burung Elang ##")
elang.info_bird()
