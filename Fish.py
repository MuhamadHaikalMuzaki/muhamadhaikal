from Animal import Animal

# Child class Fish
class Fish(Animal):
    # Konstruktor dengan properti tambahan
    def __init__(self, nama, makanan, hidup, berkembang_biak, bernapas, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bernapas = bernapas
        self.habitat = habitat

    def info_fish(self):
        super().info_animal()
        print(
            f"\nBernapas mengunakan\t\t\t: {self.bernapas}\n"
            f"\nHabitat Di\t\t: {self.habitat}\n"
        )
#objek
print()
ikan_hiu = Fish("Hiu", "Daging", "Air", "Bertelur dan Melahirkan", "Insang", "Laut")
ikan_gurame = Fish("Gurame", "Serangga", "Air", "Bertelur", "Insang", "Air Tawar")

# Menampilkan informasi ikan
print("## Informasi Ikan Hiu ##")
ikan_hiu.info_fish()

print("## Informasi Ikan Gurame ##")
ikan_gurame.info_fish()
