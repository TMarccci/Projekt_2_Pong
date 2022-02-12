# Projektmunka - Feladat
### Pong Remastered 99% Veszély!!4!44!!4"Pong  Remastered

## A játék szabályai
•	Adott két játékos.
•	Van egy labda, amely oda-vissza pattog a pályán.
•	A két játékos fül-le tud mozogni a pályán.
•	A cél, hogy a labda beérjen az ellenfél térfelére anélkül, hogy visszapattanna.
•	Ha a labda hozzáér az egyik játékos térfelének széléhez, az ellenfele pontot szerez.
•	Vannak power-upok, amiket a működés részben még kifejtek.
 
## Működése
•	A játék python nyelven íródott, felhasznált könyvtár a pygame, time, sys, os és random.
•	A pygame előre elkészített képekkel dolgozik, azok lesznek a szereplők.
•	Minden egyes ciklusnál frissíti a képernyőt, így nem lesz végtelen szereplő.

•	Labda működése:
 
 
•	Labda ütközik a széllel, és újraindítja a kört:
 
## Power-upok:
o	Piros pötty:
•	Megnöveli a játékos méretét a beállított időre.
o	Kék pötty:
•	Felgyorsítja a játékost a megadott időre.

o	Megjelenés logikája jelen esetben P1-nél:
 
## A bot logikája:
o	Működése viszonylag egyszerű, nagyon nem számol semmit, csak lekéri a labda helyzetét, és így követi azt.
o	Bot logikája:

## A játék kinézete:
Visszafogott, igyekszik minden szempontból az eredeti Pong-ra hasonlítani. Az egyetlen kinézetbeli különbségeket a pontszámlálók helyzete, illetve a power-upok.
o	Játékmód kiválasztása:
o	Játékmenet (élőben kicsivel látványosabb):

## Készítette:
	Tihanyi Marcell
	Szabó Szabolcs Zsolt
	Kun Géza Márk
