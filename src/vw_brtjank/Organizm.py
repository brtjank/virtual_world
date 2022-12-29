from tkinter import Label
from random import *

# Klasa nadrzedna obejmujaca wszystkie rosliny i zwierzeta, wlacznie z czlowiekiem
class Organizm:

    sila = 0
    inicjatywa = 0
    World = None
    kolor = None
    blokada = False
    czyZyje = True
    x = 0
    y = 0
    prevX = x
    prevY = y
    nazwa = None

    # metoda abstrakcyjna
    def akcja(self,okno):
        pass

    # metoda abstrakcyjna
    def umiejetnosc(self,okno):
        pass

    # metoda sprawdzajaca czy na zadanym polu juz znajduje sie jakis organizm
    def czyZajete(self,world,x,y):
        for organizm in world.organizmy:
            if (self != organizm):
                if (x == organizm.x and y == organizm.y):
                    return True
        return False

    # metoda obslugujaca kolizje organizmow
    def kolizja(self,world,okno):
        for organizm in world.organizmy:
            if (self != organizm):  # bez tego warunku kazdy organizm by sie rozmnazal sam ze soba
                # rozne gatunki koliduja - walka
                if (self.x == organizm.x and self.y == organizm.y and self.kolor != organizm.kolor):
                    self.walka(organizm,okno)
                # te same gatunki koliduja - rozmnazanie (zwierzeta tez moga sie rozmnazac)
                elif (self.x == organizm.x and self.y == organizm.y and self.kolor == organizm.kolor):
                    tmp = randint(0,3)
                    if tmp == 0:
                        if (int(self.x) <= 360 and self.czyZajete(self.World,self.x+20,self.y) == False):
                            info = Label(okno,text = self.nazwa + " rozmnaza sie " ,bg='lightblue')
                            info.place(x=10,y=400 + organizm.World.licznikLogi * 15)
                            organizm.World.licznikLogi += 1
                            self.dodaj(self.World,self.x+20,self.y,self.sila)
                    elif tmp == 1:
                        if (int(self.y) <= 360 and self.czyZajete(self.World,self.x,self.y+20) == False):
                            info = Label(okno,text = self.nazwa + " rozmnaza sie " ,bg='lightblue')
                            info.place(x=10,y=400 + organizm.World.licznikLogi * 15)
                            organizm.World.licznikLogi += 1
                            self.dodaj(self.World,self.x,self.y+20,self.sila)
                    elif tmp == 2:
                        if (int(self.y) >= 20 and self.czyZajete(self.World,self.x,self.y-20) == False):
                            info = Label(okno,text = self.nazwa + " rozmnaza sie " ,bg='lightblue')
                            info.place(x=10,y=400 + organizm.World.licznikLogi * 15)
                            organizm.World.licznikLogi += 1
                            self.dodaj(self.World,self.x,self.y-20,self.sila)
                    else:
                        if (int(self.x) >= 20 and self.czyZajete(self.World,self.x-20,self.y) == False):
                            info = Label(okno,text = self.nazwa + " rozmnaza sie " ,bg='lightblue')
                            info.place(x=10,y=400 + organizm.World.licznikLogi * 15)
                            organizm.World.licznikLogi += 1
                            self.dodaj(self.World,self.x-20,self.y,self.sila)

    # metoda obslugujaca zdarzenie gdy napotykaja na siebie organizmy roznych gatunkow
    def walka(self,organizm,okno):
            #kazdy z organizmow uzywa swojej umiejetnosci w czasie walki
            self.umiejetnosc(organizm,okno) 
            organizm.umiejetnosc(self,okno)
            # po uzyciu umiejetnosci jeszcze raz sprawdzamy 
            # czy organizmy dalej stoja na tym samym miejscu i czy zyja
            if (self.x == organizm.x and self.y == organizm.y and self.czyZyje == True):
                if (self.sila > organizm.sila):
                    if(organizm.inicjatywa == 0): # jesli organizm ktory przegral to roslina
                        info = Label(okno,text = self.nazwa + " zjada " + organizm.nazwa,bg='lightblue')
                    else: # jesli organizm ktory przegral to zwierze
                        info = Label(okno, text=self.nazwa + " zabija " + organizm.nazwa, bg='lightblue')
                    info.place(x=10,y=400 + organizm.World.licznikLogi * 15)
                    organizm.World.licznikLogi += 1
                    self.World.organizmy.remove(organizm)
                    del organizm
                elif (self.sila < organizm.sila):
                    if (self.inicjatywa == 0): # jesli organizm ktory przegral to roslina
                        info = Label(okno, text=organizm.nazwa + " zjada " + self.nazwa, bg='lightblue')
                    else: # jesli organizm ktory przegral to zwierze
                        info = Label(okno, text=organizm.nazwa + " zabija " + self.nazwa, bg='lightblue')
                    info.place(x=10,y=400 + organizm.World.licznikLogi * 15)
                    self.World.licznikLogi += 1
                    organizm.World.organizmy.remove(self)
                    del self