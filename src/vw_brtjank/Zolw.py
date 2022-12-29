from random import randint
from tkinter import Label
from vw_brtjank import Zwierze

# Akcja - zolw ma 25% szans na standardowy ruch o jedno pole, tj. rusza sie rzadziej
# Umiejetnosc - odpiera ataki, jesli sila atakujacego <5 (sam zolw ma sile 2);
#           w takim wypadku nie ginie zaden z walczacych organizmow 
class Zolw(Zwierze.Zwierze):

    def __init__(self, world):
        self.sila = 2
        self.inicjatywa = 1
        self.World = world
        self.kolor = "darkgreen"
        self.nazwa = "Zolw"
        world.organizmy.append(self)
    
    def dodaj(self,world,x,y,sila):
        a = Zolw(world)
        a.x = x
        a.y = y
        a.sila = sila
    
    def akcja(self,okno):
        tmp = randint(0,3)
        ptr = randint(0,3)
        if ptr == 1:
            if tmp == 0:
                if int(self.x) <= 360:
                    self.prevX = self.x
                    self.x += 20
            elif tmp == 1:
                if  int(self.y) <= 360:
                    self.prevY = self.y
                    self.y += 20
            elif tmp == 2:
                if int(self.y) >= 20:
                    self.prevY = self.y
                    self.y -= 20
            else:
                if int(self.x) >= 20:
                    self.prevY = self.y
                    self.x -=20
    
    def umiejetnosc(self,organizm,okno):
        if organizm.sila < 5:
            organizm.x = organizm.prevX
            organizm.y = organizm.prevY
            info = Label(okno,text = "Żółw odpiera atak",bg='lightblue')
            info.place(x=10,y=400 + self.World.licznikLogi * 10)
            self.World.licznikLogi += 1
        else:
            pass