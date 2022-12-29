from random import *
from vw_brtjank import Organizm

# Klasa obejmujaca wszystkie zwierzeta
# Akcja - standardowe poruszanie sie zwierzat; o jedno pole w losowym kierunku
class Zwierze(Organizm.Organizm):
    
    def akcja(self,okno):
        tmp = randint(0,3)
        if tmp == 0:
            if int(self.x) <= 360:
                self.x += 20
        elif tmp == 1:
            if int(self.y) <= 360:
                self.y += 20
        elif tmp == 2:
            if int(self.y) >= 20:
                self.y -= 20
        else:
            if int(self.x) >= 20:
                self.x -=20

    def umiejetnosc(self,organizm,okno):
        pass

    def dodaj(self,world,x,y,sila):
        pass
