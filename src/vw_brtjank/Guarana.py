from vw_brtjank import Rosliny

# Akcja - standardowe rozmnazanie
# Umiejetnosc - dodaje sily temu, ktory ja zje
class Guarana(Rosliny.Rosliny):

    def __init__(self,world):
        self.sila = 0
        self.World = world
        self.kolor = "blue"
        self.nazwa = "Guarana"
        world.organizmy.append(self)
        
    def dodaj(self,world,x,y,sila):
        a = Guarana(world)
        a.x = x
        a.y = y
        a.sila = sila

    def umiejetnosc(self, organizm, okno):
        organizm.sila += 3