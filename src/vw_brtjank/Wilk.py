from vw_brtjank import Zwierze

# Akcja - standardowe poruszanie sie (o jedno pole w losowym kierunku)
# Umiejetnosc - brak
class Wilk(Zwierze.Zwierze):

    def __init__(self, world):
        self.sila = 9
        self.inicjatywa = 5
        self.World=world
        self.kolor = "gray"
        self.nazwa = "Wilk"
        world.organizmy.append(self)
    
    def dodaj(self,world,x,y,sila):
        a = Wilk(world)
        a.x = x
        a.y = y
        a.sila = sila


