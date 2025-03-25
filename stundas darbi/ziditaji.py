class Ziditaji:
    def __init__(self,nosaukums, zobu_skaits=32, matu_krasa="blondi"):
        self.nosaukums = nosaukums
        self.zobu_skaits = zobu_skaits
        self.matu_krasa = matu_krasa
    def elpot(self):
        print("Uhh uhhh ahhh")
    def sasveicinaties(self):
        print(f"Labdien! Esmu {self.nosaukums}")
        
class Primati(Ziditaji):
    ...
class Pusaudzi(Ziditaji):
    def chau(self):
        print(f"Chau! Esmu {self.nosaukums}")
    def izrautzobu(self):
        self.zobu_skaits = self.zobu_skaits - 1

Peteris = Primati("Peteris", 12, "rudi")
Liene = Primati("Liene", 13, "tumsi")
Emils = Pusaudzi("Emīls", 14, "gaisi")
print(Peteris.zobu_skaits)
Peteris.elpot()
Liene.sasveicinaties()
Emils.chau()
Emils.izrautzobu()
print(Emils.zobu_skaits)