from tkinter import Label
from random import *
from vw_brtjank import Rosliny

# Akcja - standardowo sie rozmnaza, oraz zabija wszystkie zwierzeta w poblizu 1 pola
# Umiejetnosc - zjedzenie barszczu powoduje smierc; zabija organizm ktory na niego napotka
class Barszcz(Rosliny.Rosliny):

    def __init__(self,world):
        self.sila = 10
        self.World = world
        self.kolor = "red"
        self.nazwa = "Barszcz Sosnowskiego"
        world.organizmy.append(self)

    def dodaj(self, world, x, y, sila):
        a = Barszcz(world)
        a.x = x
        a.y = y
        a.sila = sila

    def akcja(self, okno):
        ptr = randint(0,30)
        if ptr == 1:
            tmp = randint(0,3)
            if tmp == 0:
                if (int(self.x) <= 360 and self.czyZajete(self.World, self.x + 20, self.y) == False):
                    info = Label(okno, text=self.nazwa + " rozmnaza sie ", bg='lightblue')
                    info.place(x = 10, y = 400 + self.World.licznikLogi * 15)
                    self.World.licznikLogi += 1
                    self.dodaj(self.World, self.x+20, self.y, self.sila)
            elif tmp == 1:
                if (int(self.y) <= 360 and self.czyZajete(self.World, self.x, self.y + 20) == False):
                    info = Label(okno, text=self.nazwa + " rozmnaza sie ", bg='lightblue')
                    info.place(x = 10, y = 400 + self.World.licznikLogi * 15)
                    self.World.licznikLogi += 1
                    self.dodaj(self.World, self.x, self.y + 20, self.sila)
            elif tmp == 2:
                if (int(self.y) >= 20 and self.czyZajete(self.World, self.x, self.y - 20) == False):
                    info = Label(okno, text=self.nazwa + " rozmnaza sie ", bg='lightblue')
                    info.place(x = 10, y = 400 + self.World.licznikLogi * 15)
                    self.World.licznikLogi += 1
                    self.dodaj(self.World, self.x, self.y - 20, self.sila)
            elif tmp == 3:
                if (int(self.x >= 20) and self.czyZajete(self.World, self.x - 20, self.y) == False):
                    info = Label(okno, text=self.nazwa + " rozmnaza sie ", bg='lightblue')
                    info.place(x = 10, y = 400 + self.World.licznikLogi * 15)
                    self.World.licznikLogi += 1
                    self.dodaj(self.World, self.x - 20, self.y, self.sila)

        # zabicie zwierzat na sasiednich polach (zwierzeta maja inicjatywe >0)          
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    for organizm in self.World.organizmy:
                        if organizm.x == self.x + i * 20 and organizm.y == self.y + j * 20 and organizm.inicjatywa > 0:
                            info = Label(okno, text=self.nazwa + " zabija " + organizm.nazwa, bg='lightblue')
                            info.place(x=10, y=400 + organizm.World.licznikLogi * 15)
                            organizm.World.licznikLogi += 1
                            self.World.organizmy.remove(organizm)
                            del organizm

    # organizm ktory wpadnie na barszcz, ginie
    def umiejetnosc(self,organizm,okno):
        info = Label(okno, text=organizm.nazwa + " zjada " + self.nazwa + " i ginie", bg='lightblue')
        info.place(x=10, y=400 + organizm.World.licznikLogi * 15)
        organizm.World.licznikLogi += 1
        organizm.czyZyje = False
        self.World.organizmy.remove(organizm)
        del organizm


