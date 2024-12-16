from Animal import Animal

class Ular(Animal):
    # Konstruktor dengan properti tambahan
    def __init__(self, nama, makanan, hidup, berkembang_biak, panjang, beracun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.panjang = panjang
        self.beracun = beracun

    # Method untuk menampilkan informasi ular
    def info_ular(self):
        super().info_animal()
        print(
            f"Panjang             : {self.panjang} meter\n"
            f"Beracun             : {'Ya' if self.beracun else 'Tidak'}\n"
        )

# Membuat objek Ular
ular_cobra = Ular("Cobra", "Daging", "Hutan", "Bertelur", 2.5, True)
ular_piton = Ular("Piton", "Daging", "Hutan", "Bertelur", 5.0, False)

print("## Informasi Ular Cobra ##")
ular_cobra.info_ular()

print("## Informasi Ular Piton ##")
ular_piton.info_ular()
