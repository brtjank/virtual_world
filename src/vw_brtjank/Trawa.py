from vw_brtjank import Rosliny

# Akcja - standardowe rozmnazanie
# Umiejetnosc - brak
class Trawa(Rosliny.Rosliny):

    def __init__(self,world):
        self.sila = 0
        self.World = world
        self.kolor = "lightgreen"
        self.nazwa = "Trawa"
        world.organizmy.append(self)

    def dodaj(self,world,x,y,sila):
        a = Trawa(world)
        a.x = x
        a.y = y
        a.sila = sila

