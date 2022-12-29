from random import randint
from vw_brtjank import Rosliny

# Akcja - rozmnaza sie szybciej niz inne roliny
# probuje sie rozmnozyc 3 razy w ciagu jednej tury
class Mlecz(Rosliny.Rosliny):

    def __init__(self,world):
        self.sila = 0
        self.inicjatywa = 0
        self.World = world
        self.kolor = "yellow"
        self.nazwa = "Mlecz"
        world.organizmy.append(self)
    
    def dodaj(self,world,x,y,sila):
        a = Mlecz(world)
        a.x = x
        a.y = y
        a.sila = sila
    
    def akcja(self,okno):
        for i in range(3):
            ptr = randint(0,30)
            if ptr == 1:
                tmp = randint(0,3)
                if tmp == 0:
                    if (int(self.x) <= 360 and self.czyZajete(self.World,self.x+20,self.y) == False):
                        self.dodaj(self.World,self.x+20,self.y,self.sila)
                elif tmp == 1:
                    if (int(self.y) <= 360 and self.czyZajete(self.World,self.x,self.y+20) == False):
                        self.dodaj(self.World,self.x,self.y+20,self.sila)
                elif tmp == 2:
                    if (int(self.y) >= 20 and self.czyZajete(self.World,self.x,self.y-20) == False):
                        self.dodaj(self.World,self.x,self.y-20,self.sila)
                else:
                    if (int(self.x) >= 20 and self.czyZajete(self.World,self.x-20,self.y) == False):
                        self.dodaj(self.World,self.x-20,self.y,self.sila)