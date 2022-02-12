# Projektmunka - Feladat
### Pong Remastered 99% Veszély!!4!44!!4"Pong Remastered
## A játék szabályai
Adott két játékos.
Van egy labda, amely oda-vissza pattog a pályán.
A két játékos fül-le tud mozogni a pályán.
A cél, hogy a labda beérjen az ellenfél térfelére anélkül, hogy visszapattanna.
Ha a labda hozzáér az egyik játékos térfelének széléhez, az ellenfele pontot szerez.
Vannak power-upok, amiket a működés részben még kifejtek.

![](https://raw.githubusercontent.com/TMarccci/PongRemastered_Proj/master/screenshots/1.png)
  

## Működése
A játék python nyelven íródott, felhasznált könyvtár a pygame, time, sys, os és random.
A pygame előre elkészített képekkel dolgozik, azok lesznek a szereplők.
Minden egyes ciklusnál frissíti a képernyőt, így nem lesz végtelen szereplő.

![](https://raw.githubusercontent.com/TMarccci/PongRemastered_Proj/master/screenshots/2.png)

### Labda működése:

![](https://raw.githubusercontent.com/TMarccci/PongRemastered_Proj/master/screenshots/3.png)

### Labda ütközik a széllel, és újraindítja a kört:

![](https://raw.githubusercontent.com/TMarccci/PongRemastered_Proj/master/screenshots/4.png)

## Power-upok:

###  1. Piros pötty:
     Megnöveli a játékos méretét a beállított időre.

###  2. Kék pötty:
	 Felgyorsítja a játékost a megadott időre.

Megjelenés logikája jelen esetben P1-nél:

![](https://raw.githubusercontent.com/TMarccci/PongRemastered_Proj/master/screenshots/5.png)

## A bot logikája:
Működése viszonylag egyszerű, nagyon nem számol semmit, csak lekéri a labda helyzetét, és így követi azt.

### Bot logikája:
![](https://raw.githubusercontent.com/TMarccci/PongRemastered_Proj/master/screenshots/6.png)

  

## A játék kinézete:
Visszafogott, igyekszik minden szempontból az eredeti Pong-ra hasonlítani. Az egyetlen kinézetbeli különbségeket a pontszámlálók helyzete, illetve a power-upok.

### Játékmód kiválasztása:

![](https://raw.githubusercontent.com/TMarccci/PongRemastered_Proj/master/screenshots/7.png)

### Játékmenet (élőben kicsivel látványosabb):

![](https://raw.githubusercontent.com/TMarccci/PongRemastered_Proj/master/screenshots/8.png)

  

## Készítette:
 - **Tihanyi Marcell** 
 - **Szabó Szabolcs Zsolt** 
 - **Kun Géza Márk**
