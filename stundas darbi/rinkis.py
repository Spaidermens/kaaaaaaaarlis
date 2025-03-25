class rinkis:
    def __init__(self, radiuss = 1):
        self.radiuss = radiuss
    def iestatit_radiusu(self):
        self.radiuss = input()
        if int(self.radiuss) < 1:
            self.radiuss = 1
    def izvadit_radiusu(self):
        print(f"radiuss ir {self.radiuss}")
    def diametrs(self):
        print(f"diametrs ir {int(self.radiuss) * 2}")
    def laukums(self):
        print(f"Ja rādiuss ir {int(self.radiuss)}, laukums ir {float(self.radiuss) * 3.14 :0.2f}")
    def rinka_linijas_garums(self):
        print(f"Ja rādiuss ir {int(self.radiuss)} riņķa līnijas garums ir {float(self.radiuss) * 2 * 3.14 :0.2f}")
        
rinkis1 = rinkis(4)
 
rinkis1.izvadit_radiusu()
rinkis1.iestatit_radiusu()
rinkis1.izvadit_radiusu()
rinkis1.diametrs()
rinkis1.laukums()
rinkis1.rinka_linijas_garums()
        