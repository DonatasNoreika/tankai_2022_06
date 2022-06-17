
from tankas import Tankas

tankas = Tankas()

while True:
    tankas.info()
    pasirinkimas = input("Judėti į:\ns - šiaurę\np - pietūs\nv - vakarai\nr - rytai\nx - šūvis\ni - info\nb - išeiti iš žaidimo\n")
    if pasirinkimas == "s":
        tankas.siaure()
    if pasirinkimas == "p":
        tankas.pietus()
    if pasirinkimas == "v":
        tankas.vakarai()
    if pasirinkimas == "r":
        tankas.rytai()
    if pasirinkimas == "x":
        tankas.suvis()
    if pasirinkimas == "i":
        tankas.info()
    if pasirinkimas == "b":
        print("Viso gero")
        break