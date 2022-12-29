from tkinter import Label
from random import *
from vw_brtjank import Organizm

# Klasa obejmujaca wszystkie rosliny
# Akcja - standardowe rozmnazazanie roslin (prawdopodobienstwo 1/30); 
#       nowa roslina rodzi sie na sasiednim losowym polu
class Rosliny(Organizm.Organizm):
    
    def akcja(self,okno):
        ptr = randint(0,30)
        if ptr == 1:
            tmp = randint(0,3)
            if tmp == 0:
                if (int(self.x) <= 360 and self.czyZajete(self.World,self.x+20,self.y) == False):
                    info = Label(okno, text=self.nazwa + " rozmnaza sie ", bg='lightblue')
                    info.place(x=10, y=400 + self.World.licznikLogi * 15)
                    self.World.licznikLogi += 1
                    self.dodaj(self.World,self.x+20,self.y,self.sila)
            elif tmp == 1:
                if (int(self.y) <= 360 and self.czyZajete(self.World,self.x,self.y+20) == False):
                    info = Label(okno, text=self.nazwa + " rozmnaza sie ", bg='lightblue')
                    info.place(x=10, y=400 + self.World.licznikLogi * 15)
                    self.World.licznikLogi += 1
                    self.dodaj(self.World,self.x,self.y+20,self.sila)
            elif tmp == 2:
                if (int(self.y) >= 20 and self.czyZajete(self.World,self.x,self.y-20) == False):
                    info = Label(okno, text=self.nazwa + " rozmnaza sie ", bg='lightblue')
                    info.place(x=10, y=400 + self.World.licznikLogi * 15)
                    self.World.licznikLogi += 1
                    self.dodaj(self.World,self.x,self.y-20,self.sila)
            elif tmp == 3:
                if (int(self.x >= 20) and self.czyZajete(self.World,self.x-20,self.y) == False):
                    info = Label(okno, text=self.nazwa + " rozmnaza sie ", bg='lightblue')
                    info.place(x=10, y=400 + self.World.licznikLogi * 15)
                    self.World.licznikLogi += 1
                    self.dodaj(self.World,self.x-20,self.y,self.sila)

    # metoda abstrakcyjna
    def umiejetnosc(self,organizm,okno):
        pass

    # metoda abstrakcyjna
    def dodaj(self,world,x,y,sila):
        pass
