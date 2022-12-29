from tkinter import Label
from vw_brtjank import Zwierze

# Czlowiek sterowany jest przez gracza za pomoca klawiatury
# Posiada on mozliwosc aktywowania supermocy
class Czlowiek(Zwierze.Zwierze):
    
    def __init__(self, world):
        self.sila = 5
        self.inicjatywa = 4
        self.World = world
        self.kolor = "Lightpink"
        self.nazwa = "Czlowiek"
        self.blokada = False # blokada ruchu, aby czlowiek nie mogl sie ruszyc o wiecej niz jedno pole w ciagu tury
        self.wykorzystana = False # czy supermoc byla wykorzystana w ciagu ostatnich 10 tur
        self.czasOdAktywacji = 0 # liczba tur, ktore uplynely od ostatniego aktywowania supermocy
        self.uzycieMocy = False # czy supermoc zostala uzyta (zabicie organizmu)
        world.organizmy.append(self)

    # akcja czlowieka 
    # ruch - strzalki; aktywowanie supermocy - spacja
    # supermoc - przez 5 tur od aktywacji czlowiek zabija wzytskie organizmy na sasiednich polach
    # od momentu aktywacji supermocy czlowiek mui czekac 10 tur na mozliwosc ponownego jej wykorzystania
    def akcja(self,event):
        if event.keysym == 'space':
            if self.wykorzystana == False:
                self.wykorzystana = True
        elif self.blokada == False:
            # kontrola wykorzystania supermocy
            if self.czasOdAktywacji == 10: 
                self.czasOdAktywacji = 0
                self.wykorzystana = False
            elif self.wykorzystana == True:
                self.czasOdAktywacji += 1

            # ruch czlowieka
            if event.keysym == 'Down':
                if  int(self.y) <= 360:
                    self.prevY = self.y
                    self.y += 20
            elif event.keysym == 'Right':
                if int(self.x) <= 360:
                    self.prevX = self.x
                    self.x += 20
            elif event.keysym == 'Left':
                if int(self.x) >= 20:
                    self.prevX = self.x
                    self.x -= 20
            elif event.keysym == 'Up':
                if int(self.y) >= 20:
                    self.prevY = self.y
                    self.y -= 20

            # wychwycony i obsluzony ruch; blokada mozliwosci dalszego ruchu
            self.blokada = True 
            
        # wykorzystanie supermocy jesli jest ona aktywna
        # zabicie sasiednich organizmow
        if self.czasOdAktywacji > 0 and self.czasOdAktywacji <= 5:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i != 0 or j != 0:
                        for organizm in self.World.organizmy:
                            if organizm.x == self.x + i * 20 and organizm.y == self.y + j * 20:
                                self.World.organizmy.remove(organizm)
                                del organizm
                                self.uzycieMocy = True
                                