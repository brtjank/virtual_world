from tkinter import *
import operator
import linecache
import os
from vw_brtjank import Antylopa
from vw_brtjank import Mlecz
from vw_brtjank import Owca
from vw_brtjank import Zolw
from vw_brtjank import Lis
from vw_brtjank import Czlowiek
from vw_brtjank import Wilk
from vw_brtjank import Guarana
from vw_brtjank import Jagoda
from vw_brtjank import Trawa
from vw_brtjank import Barszcz

# Klasa obejmujaca swiat i organizmy w nim zyjace
class Swiat:

    organizmy = list()  # lista organizmow (pososrtowane wg inicjatywy)
    licznikLogi = 1 #licznik do wypisywania logow na ekranie (aby nie nachodzily na siebie)
    tury = 0 # licznik tur
    silaCzlowieka = 0 # zmienna przechowujaca sile czlowieka
    licznikSupermocy = 0 # zmienna przechowujaca liczbe tur, ktore uplynely od aktywacji supermocy

    # metoda obslugujaca przebieg tury
    def wykonajTure(self,okno):
        napis = Frame(okno,bg='lightblue')
        napis.place( width = 400, height = 150,x = 0 , y = 400) # tu beda wypisywane logi

        self.organizmy[:] = sorted(self.organizmy, key=operator.attrgetter('inicjatywa'),reverse=True)

        for organizm in self.organizmy:
                if organizm.nazwa == "Czlowiek":
                    okno.bind('<Key>', organizm.akcja) # ruch za pomoca klawiszy
                    
                    if organizm.uzycieMocy == True:
                        info = Label(okno,text = "Czlowiek uzywa supermocy",bg='lightblue')
                        info.place(x=10,y=400 + self.licznikLogi * 15)
                        self.licznikLogi += 1
                        organizm.uzycieMocy = False

                    organizm.blokada = False # zwolnienie blokady ruchu
                    self.silaCzlowieka = organizm.sila
                    self.licznikSupermocy = organizm.czasOdAktywacji
                else:
                    organizm.akcja(okno)
                
        for organizm in self.organizmy:
            organizm.kolizja(self,okno)

        self.rysujSwiat(okno)

        self.licznikLogi = 1 # po kazdej turze licznik logow jest resetowany
        self.tury += 1

    # metoda rysujaca swiat
    def rysujSwiat(self,okno):
        gora = Frame(okno,bg='white')
        gora.place( width = 400, height = 400)
        gora.widgetName = 'Pole'
        gumka = Frame(okno,bg='lightblue')
        gumka.place( width = 150, height = 60,x = 420, y = 370)
        tury = Label(okno,text = "Tura: ",bg='lightblue')
        tury.place(x=420,y=370)
        tury2 = Label(okno,text = int(self.tury),bg='lightblue')
        tury2.place(x=450,y=370)
        sila = Label(okno, text="Sila czlowieka: ", bg='lightblue')
        sila.place(x=420, y=390)
        sila2 = Label(okno, text=int(self.silaCzlowieka), bg='lightblue')
        sila2.place(x=500, y=390)
        supermoc = Label(okno, text="licznik Supermocy: ", bg='lightblue')
        supermoc.place(x=420, y=410)
        supermoc2 = Label(okno, text=int(self.licznikSupermocy), bg='lightblue')
        supermoc2.place(x=530, y=410)

        for organizm in self.organizmy:
            tmp = Frame(okno,bg=organizm.kolor)
            tmp.place(x=organizm.x,y=organizm.y,width=20,height=20)

    # zapisuje obecny stan gry (nr tury i info o organizmach) do pliku o nazwie save.txt
    def zapisz(self):
        dirname = os.path.dirname(os.path.abspath(__file__))
        if (os.path.exists(dirname + '/save.txt')):
            os.remove(dirname + '/save.txt')
        plik = open((dirname + '/save.txt'), 'w')
        try:
            plik.write("tura " + str(self.tury - 1) + " \n")
            for organizm in self.organizmy:
                plik.write(str(organizm.nazwa) + " " + str(organizm.x) + " " + str(organizm.y)+ " " + str(organizm.sila) + " \n")
        finally:
            plik.close()
    
    
    # wczytuje zapiany stan gry z pliku o nazwie save.txt
    def wczytaj(self,okno):
        dirname = os.path.dirname(os.path.abspath(__file__))
        plik = open((dirname + '/save.txt'), 'r')
        numer_wiersza = 1
        del self.organizmy[0:(len(self.organizmy))] # kasuje wszystkie organizmy
        try:
            for linia in plik:
                dirname = os.path.dirname(os.path.abspath(__file__))
                linia = linecache.getline(dirname + '/save.txt', numer_wiersza) # pobieram linie
                organizm = [list(map(str,linia.split(' ')))] # oddzielam kazdy element spacja
                tablica = organizm[0]  # pobieram cala rozdzielona tablice
                if tablica[0] == 'tura':
                    self.tury = int(tablica[1]) # pobranie numeru tury z pliku
                else:
                    rasa = tablica[0] # pobieram pierwszy element
                    if rasa == 'Zolw':
                        a =  Zolw.Zolw(self)
                        self.dodajdolisty(a,int(tablica[1]),int(tablica[2]),int(tablica[3]))
                    elif rasa == 'Czlowiek':
                        a =  Czlowiek.Czlowiek(self)
                        self.dodajdolisty(a,int(tablica[1]),int(tablica[2]),int(tablica[3]))
                    elif rasa == 'Wilk':
                        a =  Wilk.Wilk(self)
                        self.dodajdolisty(a,int(tablica[1]),int(tablica[2]),int(tablica[3]))
                    elif rasa == 'Owca':
                        a =  Owca.Owca(self)
                        self.dodajdolisty(a,int(tablica[1]),int(tablica[2]),int(tablica[3]))
                    elif rasa == 'Antylopa':
                        a =  Antylopa.Antylopa(self)
                        self.dodajdolisty(a,int(tablica[1]),int(tablica[2]),int(tablica[3]))
                    elif rasa == 'Lis':
                        a =  Lis.Lis(self)
                        self.dodajdolisty(a,int(tablica[1]),int(tablica[2]),int(tablica[3]))
                    elif rasa == 'Trawa':
                        a =  Trawa.Trawa(self)
                        self.dodajdolisty(a,int(tablica[1]),int(tablica[2]),int(tablica[3]))
                    elif rasa == 'Guarana':
                        a =  Guarana.Guarana(self)
                        self.dodajdolisty(a,int(tablica[1]),int(tablica[2]),int(tablica[3]))
                    elif rasa == 'Wilcza':
                        a =  Jagoda.Jagoda(self)
                        self.dodajdolisty(a,int(tablica[2]),int(tablica[3]),int(tablica[4]))
                    elif rasa == 'Barszcz':
                        a = Barszcz.Barszcz(self)
                        self.dodajdolisty(a, int(tablica[2]), int(tablica[3]), int(tablica[4]))
                    elif rasa == 'Mlecz':
                        a =  Mlecz.Mlecz(self)
                        self.dodajdolisty(a,int(tablica[1]),int(tablica[2]),int(tablica[3]))
                numer_wiersza += 1
            linecache.clearcache()
            self.rysujSwiat(okno)
            self.tury += 1
            self.wykonajTure(okno)
        finally:
            plik.close()


    # utworzenie poczatkowego zestawu organizmow
    def stworzPoczatek(self):  
        a= Lis.Lis(self)
        a.x = 20
        a.y = 20
        b= Owca.Owca(self)
        b.x = 80
        b.y = 40
        c= Wilk.Wilk(self)
        c.x = 160
        c.y = 80
        d = Czlowiek.Czlowiek(self)
        d.x = 200
        d.y = 200
        e= Zolw.Zolw(self)
        e.x = 280
        e.y = 60
        f= Antylopa.Antylopa(self)
        f.x = 340
        f.y = 360
        g= Mlecz.Mlecz(self)
        g.x = 260
        g.y = 380
        h = Trawa.Trawa(self)
        h.x = 340
        h.y = 20
        i = Jagoda.Jagoda(self)
        i.x = 320
        i.y = 120
        j= Guarana.Guarana(self)
        j.x = 320
        j.y = 260
        k = Barszcz.Barszcz(self)
        k.x = 120
        k.y = 260


    # tworzy nowa symulacje
    def nowaSymulacja(self,okno):
        self.tury = 0
        del self.organizmy[0:(len(self.organizmy))] # kasuje wszystkie organizmy
        self.stworzPoczatek()
        self.rysujSwiat(okno)
        self.tury += 1
        self.wykonajTure(okno)

    # dodaje podany organizm do listy organizmow istenijacych w swiecie
    def dodajdolisty(self,rasa,x,y,sila):
        rasa.x = x
        rasa.y = y
        rasa.sila = sila


