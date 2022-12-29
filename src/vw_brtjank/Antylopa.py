from random import randint
from tkinter import Label

from vw_brtjank import Zwierze

# Akcja - standardowa akcja antylopy to ruch co 2 pola w losowym kierunku
# Umiejetnosc - w przypadku walki ma 50% szans na ucieczke
#       zmienia wtedy pole na losowe sasiednie
class Antylopa(Zwierze.Zwierze):
    
    def __init__(self, world):
        self.sila = 4
        self.inicjatywa = 4
        self.World = world
        self.kolor = "brown"
        self.nazwa = "Antylopa"
        world.organizmy.append(self) 

    def dodaj(self, world, x, y, sila):
        a = Antylopa(world)
        a.x = x
        a.y = y
        a.sila = sila

    def akcja(self,okno):
        tmp = randint(0,3)
        if tmp == 0:
            if int(self.x) <= 340:
                self.prevX = self.x
                self.x += 40
        elif tmp == 1:
            if int(self.y) <= 340:
                self.prevY = self.y
                self.y += 40
        elif tmp == 2:
            if int(self.y) >= 40:
                self.prevY = self.y
                self.y -= 40
        else:
            if int(self.x) >= 40:
                self.prevX = self.x
                self.x -=40

    def umiejetnosc(self,organizm,okno):
        ptr = randint(0,1)
        if ptr == 0:
            tmp = randint(0,3)
            if tmp == 0:
                if int(self.x) <= 360:
                    self.prevX = self.x
                    self.x += 20
            elif tmp == 1:
                if int(self.y) <= 360:
                    self.prevY = self.y
                    self.y += 20
            elif tmp == 2:
                if int(self.y) >= 40:
                    self.prevY = self.y
                    self.y -= 20
            else:
                if int(self.x) >= 40:
                    self.prevX = self.x
                    self.x -=20

            info = Label(okno,text = "Antylopa unika walki",bg='lightblue')
            info.place(x=10,y=400 + self.World.licznikLogi * 15)
            self.World.licznikLogi += 1
        else:
            pass