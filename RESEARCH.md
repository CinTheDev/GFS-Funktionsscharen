# Recherche

Hier sind Notizen über Unterpunkte und Recherche.

## Definition Funktionsscharen

### Definition und grundlegende Begriffe

Funktionsscharen sind Funktionen mit mindestens einem zusätzlich frei wählbaren Paremeter
neben dem "normalen" Parameter in den Klammern. Dieser zusätzliche Parameter kann überall
in der Funktion sein.

Andere Namen sind "Funktionenscharen", "Kurvenschar", oder "Parameterfunktion".

Funktionsscharen die man mit nur einem Parameter darstellen kann, nennt man *Büschel*.
In der GFS werde ich zum größten Teil solche Scharen behandeln, und für Einfachheit
trotzdem "Funktionsscharen" nennen.

Falls man eine Funktionsschar als Graph darstellt, wird nur der "normale" Parameter auf
einer Achse dargestellt. Der zusätzliche Parameter kann somit die Kurve ändern, und man
kann nicht alle möglichen Werte auf einmal darstellen, ohne in die 3. Dimension zu gehen.

### Verhalten von Funktionsscharen

(Darstellung mit einem Graph)

- Das Verändern des Parameters verändert die Funktion in irgendeiner Weise
- (Einfache Beispiele: Verschiebung, Sreckung / Stauchung)
- Bündel & Wie kann man solche in der Funktion erkennen (siehe unten)
- Extrempunkte können sich bewegen, auftauchen und verschwinden

#### Bündel

*Bündel* sind Punkte, durch welche alle Funktionen der Schar durchgehen.

### Rechnen mit Funktionsscharen

Man kann mit Funktionsscharen alles machen, was man mit einer normalen Funktion
auch machen kann. Man muss nur immer den zusätzlichen Parameter "mitschleppen".

Wenn man z.B. Schnittpunkte berechnet, ist oft der Schnittpunkt vom zusätzlichen
Parameter abhängig, was man auch im Graph sehen kann.

Falls sich bei irgendeiner Sache dieser Parameter herauskürzt, dann gilt die
Lösung für jede mögliche Funktion der Schar, bzw. ändern sich nicht wenn der
Parameter sich ändert.

Die meisten Lösungen werden aber abhängig vom Parameter sein.

## Flächeninhalt

Wie kann man Flächeninhalt bestimmen?

Man berechnet den Flächeninhalt normal aus (mit Integralen), und mit der Variable wird
weitergerechnet.

- (Beispiele aufführen, am besten aus dem Buch)

## Gemeinsame Punkte (Funktionsbündel)

Methoden, um gemeinsame Punkte (genannt Funktionsbündel) zu bestimmen

### Methode aus dem Buch (zwei Werte einsetzen)

Man setzt zwei Werte für den Parameter ein, und setzt beide Funktionen gleich. Die
Schnittpunkte, die unabhängig vom Parameter sind, sind potentielle Bündel. Man muss
diese prüfen indem man die Höhe dieser berechnet. Falls die Höhe auch unabhängig vom
Parameter ist, dann ist dieser Punkt ein Bündel der Funktion.

- (Beispiel aus dem Buch)

## Tiefste Hochpunkt der Schar

Exprempunkte (wie z.B. Hochpunkte) können sich bei Funktionsscharen "bewegen". Wie kann man
den tiefsten oder höchsten Punkt der Extrempunkte finden?

Man kann die Höhe der Extrempunkte berechnen (wo das Ergebnis abhängig von a ist).
Falls man dann im Ergebnis a als unabhängige Variable betrachtet, ergibt sich eie neue Funktion,
welcher die Höhe des Extrempunkts für alle Werte von a darstellt. Man kann diese Funktion nun
auf Extremstellen untersuchen, und so einen "Tiefpunkt" oder "Hochpunkt" für den Extrempunkt
der ursprünglichen Funktion berechnen.

- (Mehrere Beispiele)

## Ortskurven

Definition, und bestimmen von Ortskurven

### Definition Ortskurven

Man bezeichnet als Ortskurven den "Weg" von bestimmten speziellen Punkten in einer Funktionenschar.
Falls man den Parameter ändert, können Punkte wie z.B. Extrempunkte sicht bewegen, wobei der
zurückgelegte Weg ebenfalls auf einer Kurve liegt.

Man kann den Extrempunkt berechnen (x und y). Dieses Ergebnis lässt sich als Parameterisierte Funktion
interpretieren, welche in eine einfache Funktion umgewandelt werden kann.

### Kurzer Exkurs: Parameterisierte Funktionen

Parameterfunktionen (2D) bestehen aus 2 Teilfunktionen für die x-Komponente und y-Komponente. Beide
Funktionen zusammen stellen einen Punkt dar, der sich nach der unabhängigen Variable bewegen. Falls man
alle möglichen Punkte für alle einsetzbaren Werte darstellt, ergibt sich ein Graph.

Man kann eine Parameterisierte Funktion in die Form `y = ... [x]` bringen, indem man den x-Teil
nach dem Parameter auflöst, und dann in den y-Teil einsetzt.

Falls man es andersherum macht kommt die Form `x = ... [y]` heraus, was ein normales Ergebnis ist,
die andere Form wird aber offensichtlich bevorzugt.

### Betimmen Ortskurve von Extrempunkten

1. f_a(x) nach x Ableiten und nullsetzen
2. Nach a auflösen
3. a in ursprüngliche Funktion einsetzen.

- (1-2 Beispiele)

## Hüllkurven

### Einführung mit Parabel und Tangente

Tangente soll parameterisiert sein, damit ist Tangentenfunktion eine Funktionenschar.

Die Parabel ist die Hüllkurve der Schar.

### Herleitung einer Hüllkurve

1. Funktion nach Parameter (a) ableiten
2. Funktion nullsetzen und nach a auflösen
3. a in ursprüngliche Funktion einsetzen

Die neue Funktion (falls eine Lösung möglich ist) ist die Hüllkurve von der ursprünglichen
Funktion.

- (Ein oder zwei schnelle Beispiele)

#### Erklärung der Schritte

Man kann sich vorstellen, dass Schritt 1 tatsächlich aus zwei Schritten besteht:

1.1. a und x umtauschen
1.2. Funktion ableiten

Schritt 1.1 tauscht die Bedeutung der Variablen von a und von x. Eine Interpretation ist, dass
man einen bestimmten Wert für x in der Funktion f_a(x) einsetzt, was eine bestimmte Höhe an der
Stelle x angibt. Diese Höhe ist abhängig von a.

Falls man alle reelen Zahlen für a einsetzt, kommt man auf eine Funktion, wie die Höhe sich an der
Stelle x verändert. Diese Funktion kann man nun analysieren.

Falls diese Funktion Extremwerte hat, dann gibt es folgende Besonderheiten: Bestimmte Höhen an der
Stelle x können nicht erreicht werden egal welches a man einsetzt. Es gibt eine maximale bzw.
minimale Höhe an dieser Stelle.

Man soll nun herausfinden, für welches a man den höchsten / niedrigsten Punkt erreicht. Dies ist
ein typisches Extremwertproblem, welches gelöst werden kann, falls man die Ableitung nullsetzt.
Dies wird getan, indem man die originale Funktion nach a Ableitet und dann nullsetzt. Dadurch
bekommt man heraus, für welches a die höchste bzw. tiefste Stelle erreicht wird.

Anmerkung: Für bestimmte Funktionen gibt es mehrere Extremstellen, aber es wird nur nach globalen
Maxima bzw. Minima gesucht. Lokale, nicht globale Extremstellen werden nicht beachtet.

Die Lösung für a ist meistens von x abhängig. Dann kann man für jede Stelle x den höchsten bzw.
tiefsten möglichen Wert berechnen.

Man setzt nun a in die originale Funktion ein. Man kann sich es so vorstellen, dass jetzt für
jede Stelle das a unterschiedlich ist. Spezifisch ist a genau der Wert, für welchen die Höhe
maximal oder minmal ist. Damit bekommt man eine Funktion, welche für jedes x die Grenzwerte
darstellt.

Diese Funktion ist die Hüllkurve der Funktionenschar. Diese ist wie eine "Grenze" für die
Funktionenschar. Egal welches a man einsetzt, kommt die Funktion niemals aus dieser "Grenze".

### Wurfbahn

Wurfbahnen können als Funktionsschar dargestellt werden, um alle möglichen Wurfbahnen darzustellen.
Die Hüllkurve markiert die Grenze, wo das Wurfobjekte hinkommen kann, und welchen Bereich es
niemals erreichen wird.
