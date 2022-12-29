from tkinter import Label

from vw_brtjank import Zwierze
from random import *

# Akcja - standardowe poruszanie sie (o jedno pole w losowym kierunku)
# Umiejetnosc - nos lisa, sprawiajacy ze lis nie ruszy sie na pole ktore zajmuje silniejszy organizm
class Lis(Zwierze.Zwierze):

    def __init__(self,world):
        self.sila = 3
        self.inicjatywa = 7
        self.World = world
        self.kolor = "darkorange"
        self.nazwa = "Lis"
        world.organizmy.append(self)

    def dodaj(self,world,x,y,sila):
        a = Lis(world)
        a.x = x
        a.y = y
        a.sila = sila

    # metoda zwraca true jesli organizm kolizyjny jest silniejszy
    # wykorzystywana jest w momencie akcji - nizej
    def nosLisa(self,world,x,y):
        for organizm in world.organizmy:
            if organizm != self:
                if (organizm.x == x and organizm.y == y and organizm.sila > self.sila):
                    return True
        return False

    def akcja(self,okno):
        tmp = randint(0,3)
        if tmp == 0:
            if int(self.x) <= 360:
                if (self.nosLisa(self.World,self.x + 20, self.y) == False):
                    self.prevX = self.x
                    self.x += 20
                else:
                    info = Label(okno,text = "Lis wyczuwa zagrozenie",bg='lightblue')
                    info.place(x=10,y=400 + self.World.licznikLogi * 15)
                    self.World.licznikLogi += 1
        elif tmp == 1:
            if int(self.y) <= 360:
                if (self.nosLisa(self.World,self.x , self.y+20) == False):
                    self.prevY = self.y
                    self.y += 20
                else:
                    info = Label(okno,text = "Lis wyczuwa zagrozenie",bg='lightblue')
                    info.place(x=10,y=400 + self.World.licznikLogi * 15)
                    self.World.licznikLogi += 1
        elif tmp == 2:
            if int(self.y) >= 20:
                if (self.nosLisa(self.World,self.x , self.y-20) == False):
                    self.prevY = self.y
                    self.y -= 20
                else:
                    info = Label(okno,text = "Lis wyczuwa zagrozenie",bg='lightblue')
                    info.place(x=10,y=400 + self.World.licznikLogi * 15)
                    self.World.licznikLogi += 1
        else:
            if int(self.x) >= 20:
                if (self.nosLisa(self.World,self.x-20 , self.y) == False):
                    self.prevX = self.x
                    self.x -=20
                else:
                    info = Label(okno,text = "Lis wyczuwa zagrozenie",bg='lightblue')
                    info.place(x=10,y=400 + self.World.licznikLogi * 15)
                    self.World.licznikLogi += 1