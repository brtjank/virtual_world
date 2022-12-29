from tkinter import *
from vw_brtjank import Antylopa
from vw_brtjank import Mlecz
from vw_brtjank import Owca
from vw_brtjank import Swiat
from vw_brtjank import Zolw
from vw_brtjank import Lis
from vw_brtjank import Czlowiek
from vw_brtjank import Jagoda
from vw_brtjank import Guarana
from vw_brtjank import Trawa
from vw_brtjank import Wilk
from vw_brtjank import Barszcz

# Zawiera metody obslugujaca okna symulacji oraz wyboru
# oraz metode __main__()

world = Swiat.Swiat()
okno = Tk()  #glowne okno planszy

# Legenda po prawej stronie okna symulacji; 
# oznajmia, ktore kolory oznaczaja poszczegolne organizmy
def wypiszLegende(okno,world):
    legenda = Label(okno,text = "LEGENDA",bg='lightblue')
    legenda.place(x=490,y=15)
    zolwkwadrat = Frame(okno,bg='darkgreen')
    zolwkwadrat.place(x=450,y=40,width=20,height=20)
    zolw = Label(okno,text = "Zólw",bg='lightblue')
    zolw.place(x=480,y=40)
    liskwadrat = Frame(okno,bg='darkorange')
    liskwadrat.place(x=450,y=70,width=20,height=20)
    lis = Label(okno,text = "Lis",bg='lightblue')
    lis.place(x=480,y=70)
    wilkwadrat = Frame(okno,bg='gray')
    wilkwadrat.place(x=450,y=100,width=20,height=20)
    wilk = Label(okno,text = "Wilk",bg='lightblue')
    wilk.place(x=480,y=100)
    owcakwadrat = Frame(okno,bg='black')
    owcakwadrat.place(x=450,y=130,width=20,height=20)
    owca = Label(okno,text = "Owca",bg='lightblue')
    owca.place(x=480,y=130)
    antylopakwadrat = Frame(okno,bg='brown')
    antylopakwadrat.place(x=450,y=160,width=20,height=20)
    antylopa = Label(okno,text = "Antylopa",bg='lightblue')
    antylopa.place(x=480,y=160)
    trawakwadrat = Frame(okno,bg='lightgreen')
    trawakwadrat.place(x=450,y=190,width=20,height=20)
    trawa = Label(okno,text = "Trawa",bg='lightblue')
    trawa.place(x=480,y=190)
    mleczkwadrat = Frame(okno,bg='yellow')
    mleczkwadrat.place(x=450,y=220,width=20,height=20)
    mlecz = Label(okno,text = "Mlecz",bg='lightblue')
    mlecz.place(x=480,y=220)
    guaranakwadrat = Frame(okno,bg='blue')
    guaranakwadrat.place(x=450,y=250,width=20,height=20)
    guarana = Label(okno,text = "Guarana",bg='lightblue')
    guarana.place(x=480,y=250)
    jagodykwadrat = Frame(okno,bg='purple')
    jagodykwadrat.place(x=450,y=280,width=20,height=20)
    jagody = Label(okno,text = "Wilcze Jagody",bg='lightblue')
    jagody.place(x=480,y=280)
    barszczkwadrat = Frame(okno, bg='red')
    barszczkwadrat.place(x=450, y=310, width=20, height=20)
    barszcz = Label(okno, text="Barszcz Sosnowskiego", bg='lightblue')
    barszcz.place(x=480, y=310)
    czlowiekkwadrat = Frame(okno,bg='lightpink')
    czlowiekkwadrat.place(x=450,y=340,width=20,height=20)
    czlowiek = Label(okno,text = "Czlowiek",bg='lightblue')
    czlowiek.place(x=480,y=340)

# metoda obslugujaca zdarzenia wywolane kliknieciem myszy
# za pomoca myszy mozna dodac nowe organizmy do swiata
def mysz(event):
    try:
        nazwa = event.widget.widgetName
        if nazwa == 'Pole':
            x,y = event.x,event.y
            # przystosowanie wspolrzednych do planszy (kazdy organizm stoi na polu wielokrotnosci 20)
            if x % 20 != 0: 
                for i in range(19):
                    if (x % 20 != 0):
                        x-=1
                    else:
                        pass
            if y % 20 != 0:
                for i in range(19):
                    if (y % 20 != 0):
                        y-=1
                    else:
                        pass

            # obsluga okna wyboru nowego organizmu
            oknowyboru = Tk()
            oknowyboru.geometry("200x190")
            info = Label(oknowyboru,text = "Jaki organizm chcesz stworzyć?")
            info.place(x=10,y=10)
            # podajemy dodatkowe metody do tworzenia
            # nie mozna korzystac z domyslnych metod klas bo nie uzywamy tutaj zadnego obiektu
            # przekazujemy tam odpowiednie parametry potrzebne do utworzenia organizmu
            Lis = Button(oknowyboru, text="Lis",command=lambda: Liss(world,x,y,oknowyboru,okno))
            Lis.place(width = 100,y = 40, x = 100)
            Wilk = Button(oknowyboru, text="Wilk",command=lambda: Wilkk(world,x,y,oknowyboru,okno))
            Wilk.place(width = 100,y = 40)
            Owca = Button(oknowyboru, text="Owca",command=lambda: Owcaa(world,x,y,oknowyboru,okno))
            Owca.place(width = 100,y = 70, x = 100)
            Antylopa = Button(oknowyboru, text="Antylopa",command=lambda: Antylopaa(world,x,y,oknowyboru,okno))
            Antylopa.place(width = 100,y = 70)
            Zolw = Button(oknowyboru, text="Żółw",command=lambda: Zolww(world,x,y,oknowyboru,okno))
            Zolw.place(width = 100,y = 100, x = 100)
            Mlecz = Button(oknowyboru, text="Mlecz",command=lambda: Mleczz(world,x,y,oknowyboru,okno))
            Mlecz.place(width = 100,y = 100)
            Jagoda = Button(oknowyboru, text="Wilcza Jagoda",command=lambda: Jagodaa(world,x,y,oknowyboru,okno))
            Jagoda.place(width = 100,y = 130, x = 100)
            Guarana = Button(oknowyboru, text="Guarana",command=lambda: Guaranaa(world,x,y,oknowyboru,okno))
            Guarana.place(width = 100,y = 130)
            Barszcz = Button(oknowyboru, text="Barszcz Sosnowskiego", command=lambda: Barszczz(world, x, y, oknowyboru, okno))
            Barszcz.place(width=100, y=160, x=100)
            Trawa = Button(oknowyboru, text="Trawa",command=lambda: Trawaa(world,x,y,oknowyboru,okno))
            Trawa.place(width = 100,y = 160)
    except BaseException:
        print("Nie mozna tutaj utworzyc organizmu w miejscu wkazanym kliknieciem myszy!") #wyjatek

#
# metody zastepcze do tworzenia nowych obiektow
#
def Liss(world,x,y,oknowyboru,okno):
    a = Lis.Lis(world)
    a.x = x
    a.y = y
    world.rysujSwiat(okno)
    oknowyboru.destroy()

def Wilkk(world,x,y,oknowyboru,okno):
    a = Wilk.Wilk(world)
    a.x = x
    a.y =y
    world.rysujSwiat(okno)
    oknowyboru.destroy()

def Owcaa(world,x,y,oknowyboru,okno):
    a = Owca.Owca(world)
    a.x = x
    a.y =y
    world.rysujSwiat(okno)
    oknowyboru.destroy()

def Antylopaa(world,x,y,oknowyboru,okno):
    a = Antylopa.Antylopa(world)
    a.x = x
    a.y =y
    world.rysujSwiat(okno)
    oknowyboru.destroy()

def Zolww(world,x,y,oknowyboru,okno):
    a = Zolw.Zolw(world)
    a.x = x
    a.y =y
    world.rysujSwiat(okno)
    oknowyboru.destroy()

def Mleczz(world,x,y,oknowyboru,okno):
    a = Mlecz.Mlecz(world)
    a.x = x
    a.y =y
    world.rysujSwiat(okno)
    oknowyboru.destroy()

def Jagodaa(world,x,y,oknowyboru,okno):
    a = Jagoda.Jagoda(world)
    a.x = x
    a.y =y
    world.rysujSwiat(okno)
    oknowyboru.destroy()

def Barszczz(world, x, y, oknowyboru, okno):
    a = Barszcz.Barszcz(world)
    a.x = x
    a.y = y
    world.rysujSwiat(okno)
    oknowyboru.destroy()

def Guaranaa(world,x,y,oknowyboru,okno):
    a = Guarana.Guarana(world)
    a.x = x
    a.y =y
    world.rysujSwiat(okno)
    oknowyboru.destroy()

def Trawaa(world,x,y,oknowyboru,okno):
    a = Trawa.Trawa(world)
    a.x = x
    a.y =y
    world.rysujSwiat(okno)
    oknowyboru.destroy()


if __name__ == "__main__":
    world.stworzPoczatek() # tworzy poczatkowe obiekty
    world.wykonajTure(okno) # obsluga zerowej tury (wyswietlenie obiektow)
    okno.configure(background='lightblue')

    gora = Frame(okno,bg='white')
    gora.pack(fill = NONE,expand=NO)
    gora.place( width = 400, height = 400)

    wypiszLegende(okno,world)
    okno.geometry("600x600")
    okno.resizable(False, False)

    world.tury = 0
    world.rysujSwiat(okno)
    world.tury += 1

    # przyciski sterujace symulacja
    start = Button(okno, text="Kolejna Tura",command=lambda: world.wykonajTure(okno))
    start.place(x = 262, y = 575)
    save = Button(okno, text="Zapisz",command=lambda: world.zapisz())
    save.place(x = 215, y = 575)
    load = Button(okno, text="Wczytaj",command=lambda: world.wczytaj(okno))
    load.place(x = 160, y = 575)
    load = Button(okno, text="Nowa Symulacja",command=lambda: world.nowaSymulacja(okno))
    load.place(x = 60, y = 575)

    okno.bind('<1>', mysz) #binduje klawisz myszy pod metode mysz
    okno.mainloop() #metoda do sterowania oknem