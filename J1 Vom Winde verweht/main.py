# Importieren der notwendigen Libraries
from ast import Pass
from distutils import dist
import math

datei = open('Beispiel4.txt', 'r')          # Die Datei mit den vorgegebenen Beispielwerten öffnen
l = datei.readline().split()                # Die erste Zeile auslesen & Zahlen in einer Liste speichern

# Variablen für die Anzahl der Häuser und Windräder deklarieren & initialisieren
mengeh = int(l[0])
mengew = int(l[1])

# Listen für die Koordinaten der Häuser deklarieren
hauser = []
wind = []

# Funktion um den x-Wert aus einem String zu bekommen
def getx(S):
    k = S.split()                           # Den String aufteilen und in einer Liste speichern
    return(int(k[0]))                       # Den x-Wert als Integer zurückgeben

# Funktion um den y-Wert aus einem String zu bekommen
def gety(S):
    k = S.split()                           # Den String aufteilen und in einer Liste speichern
    return(int(k[1]))                       # Den y-Wert als Integer zurückgeben

# Die Listen mit den Werten aus der Datei befüllen
for i in range(0, mengeh):                  # Für Anzahl der Häuser wiederholen
    hauser.append(datei.readline())         # Die Liste mit jeweils einer Zeile der Datei befüllen
for f in range(0, mengew):                  # Für Anzahl der Windräder wiederholen
    wind.append(datei.readline())           # Die Liste mit jeweils einer Zeile der Datei befüllen

windheight = [10000] * mengew               # Eine Liste erstellen, die so lang ist, wie die Anzahl der Winräder
for k in range(0, mengew):                  # Für Anzahl der Windräder wiederholen
    for t in range(0, mengeh):              # Für Anzahl der Häuser wiederholen
        l = math.dist([getx(hauser[t]), gety(hauser[t])], [getx(wind[k]), gety(wind[k])])   # Die Distanz zwichen jeweils einem Haus und einem Windrad mit der Library math berechnen 
        l = l / 10                          # Die Distanz durch 10 teilen, um auf die Höhe zu kommen (10H-Regel)
        if windheight[k] > l:
            windheight[k] = round(l, 2)     # Die Höhe immer mit dem kleinsten möglichen Wert ersetzen und ggf. runden

print(windheight)                           # Die fertige Liste ausgeben
datei.close()                               # Die Datei schließen