class Dzivnieks:
    def __init__(self, nosaukums = "cilveks", kaju_skaits = 2):
        self.nosaukums = nosaukums
        self.kaju_skaits = kaju_skaits
    def izvadit_kaju_skaitu(self):
        print(f"{self.nosaukums} - {self.kaju_skaits} kājas")
        
govs = Dzivnieks("Govs", 4)
cilveks = Dzivnieks("Cilvēks",2)
cilveks1 = Dzivnieks()
astonkajis = Dzivnieks("Astoņkājis",8)

govs.izvadit_kaju_skaitu()
cilveks.izvadit_kaju_skaitu()
cilveks1.izvadit_kaju_skaitu()
astonkajis.izvadit_kaju_skaitu()