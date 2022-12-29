from tkinter import Label
from vw_brtjank import Rosliny

# Akcja - standardowe rozmnazanie
# Umiejetnosc - zabija organizm, ktory ja zje
class Jagoda(Rosliny.Rosliny):

    def __init__(self,world):
        self.sila = 99
        self.World = world
        self.kolor = "purple"
        self.nazwa = "Wilcza jagoda"
        world.organizmy.append(self)
    
    def dodaj(self,world,x,y,sila):
        a = Jagoda(world)
        a.x = x
        a.y = y
        a.sila = sila
    
    def umiejetnosc(self,organizm,okno):
        info = Label(okno, text=organizm.nazwa + " zjada " + self.nazwa + " i ginie", bg='lightblue')
        info.place(x=10, y=400 + organizm.World.licznikLogi * 15)
        organizm.World.licznikLogi += 1
        organizm.czyZyje = False
        self.World.organizmy.remove(organizm)
        del organizm
