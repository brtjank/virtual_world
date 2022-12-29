from vw_brtjank import Zwierze

# Akcja - standardowe poruszanie sie (o jedno pole w losowym kierunku)
# Umiejetnosc - brak
class Owca(Zwierze.Zwierze):

    def __init__(self, world):
        self.sila = 4
        self.inicjatywa = 4
        self.World = world
        self.kolor = "black"
        self.nazwa = "Owca"
        world.organizmy.append(self)
    
    def dodaj(self,world,x,y,sila):
        a = Owca(world)
        a.x = x
        a.y = y
        a.sila = sila