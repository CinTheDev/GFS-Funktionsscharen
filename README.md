# GFS Funktionsscharen

NOTE: If you stumbled across this repository, this is a part of a school project, so you're
probably not very interested unless you know me personally. Also, this isn't my usual coding
and git style, so don't expect too high code quality, as that is not the focus of the
project. And everything's in german.

Repository zur GFS über Funktionsscharen.

Die GFS wurde mit git versioniert. Dies dient hauptsächlich für Backup-Gründe, man kann aber auch
sich die Arbeitsschritte anzeigen lassen. Hierzu bei GitHub auf "Commits" drücken.

Die Präsentation besteht aus 2 Teilen: Dem [mp4-presenter](https://github.com/CinTheDev/mp4-presenter)
und den Animationen in diesem Repository.

Der Presenter ist ein in Rust geschriebenes Program basierend auf bevy, welches die mp4-Dateien
einliest und abspielt. Man kann die Animationen (ähnlich wie in PowerPoint) abspielen. Das Program
wurde von mir entwickelt, alles wurde aus Konvention in Englisch gehalten. (Das gleiche gilt für
die Skripte der Animationen.)

Die Animationen sind Python-Scripte, welche mit Manim Community arbeiten. Diese Scripte exportieren
die Animationen als mp4-Dateien, welche dann automatisch in einen gemeinsamen Ordner kopiert werden.

Es gibt 2 zusätliche Python-Scripte `build.py` und `render.py`, welche keine Animationen exportieren,
sondern die Animationsskripte ausführen. Grundsätzlich wird nur `build.py` von Hand ausgeführt,
`render.py` wird von diesem Skript automatisch ausgeführt.

Es sind noch einige (auf Linux begrenzte) Bash-Skripte vorhanden, die zur Bequemlichkeit bei der
Entwicklung dienen.

## Build-Prozess

Hier wird der Build-Prozess in Details erklärt. Man kann erwarten, dass der gesamte Prozess
ca. eine halbe Stunde dauern wird.

### Installation

Damit die Animationen exportiert werden können, wird Python und Manim Community benötigt.

Manim Community wird durch python mit `pip install` installiert.

Der mp4-presenter wird mit Rust und Cargo kompiliert.

Es ist auch wichtig sicherzustellen, dass in diesem Repository das Submodul `mp4-presenter`
initialisiert ist.

### build.py

Dieses Skript erstellt einen Ordner mit dem Presenter und allen Videos zusammen.

Anfänglichs wird der Presenter kompiliert und in diesen Ordner kopiert.

Das Skript besitzt eine Definition aller Szenen, die genutzt werden sollen. Bei Ausführung wird
diese Liste an `render.py` weitergegeben.

`render.py` exportiert die Animationen in einem seperaten Ordner zusammen mit sehr vielen
Cache-Dateien. Das Build-Skript kopiert dann alle relevanten Videos in den Zielordner

Am Ende gibt es einen Ordner "out", der bereit für Präsentation ist.

### render.py

`render.py` bekommt alle Szenen vom Build-Skript, und führt alle Animationsskripte mit Manim aus,
um die Animationen zu exportieren.

Das Render-Skript speichert zusätzlich Hash-Werte von allen Szenen, damit diese übersprungen werden
können falls die Szene sich nicht ändert. Dies ist wichtig in der Entwicklung, da sonst das Rendern
bei jeder kleinen Änderrung mehrere Minuten einnehmen wird.

Manim macht zwar etwas ähnliches und verwendet den Cache um Rendern der Segmente zu überspringen,
aber dies ist ziemlich langsam. Das Überspringen einer Szene kann trotzdem ca. eine Minute dauern.

## Recherche

Notizen über Recherche sind in RESEARCH.md geschrieben.

## Tatsächlich genutzte Quellen

Die Quellen, die zur Präsentation beigetragen haben. (Werden am Ende der Präsentation genannt.)

Anmerkung zu Wikipedia: Es wurde jeweils in Deutsch und in Englisch recherchiert, da
hierzu die Artikel jeweils unterschiedliche Informationen anbieten. Meistens bieten
die englischen Artikel mehr Informationen an.

- Schulbuch
- [Definition Funktionsschar](https://de.wikipedia.org/wiki/Kurvenschar)
- [Hüllfunktionen](https://de.wikipedia.org/wiki/Einh%C3%BCllende)
- [Wurfparabel](https://de.wikipedia.org/wiki/Wurfparabel)
- [Vereinfachung cos^2(tan^-1(x))](https://socratic.org/questions/how-do-you-simplify-cos-2-tan-1-x)
