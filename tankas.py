from random import randint
import pickle

class Tankas:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kryptis = "Š"
        self.suviai = [0, 0, 0, 0]
        self.priesas_x = 0
        self.priesas_y = 0
        self.priesai = 0
        self.taskai = 100


    def gauti_rekorda(self):
        try:
            with open('rekordas.pkl', 'rb') as file:
                rekordas = pickle.load(file)
        except:
            print("Nėra tokio failo")
            with open("rekordas.pkl", 'wb') as failas:
                rekordas = {"vardas": "demo", "taskai": 0}
                pickle.dump(rekordas, failas)
        return rekordas

    def siaure(self):
        self.y += 1
        self.kryptis = "Š"
        self.taskai -= 10

    def pietus(self):
        self.y -= 1
        self.kryptis = "P"
        self.taskai -= 10

    def vakarai(self):
        self.x -= 1
        self.kryptis = "V"
        self.taskai -= 10

    def rytai(self):
        self.x += 1
        self.kryptis = "R"
        self.taskai -= 10

    def _tikrinti_pataikyma(self):
        if self.x == self.priesas_x and self.kryptis == "Š" and self.y < self.priesas_y:
            return True
        if self.x == self.priesas_x and self.kryptis == "P" and self.y > self.priesas_y:
            return True
        if self.y == self.priesas_y and self.kryptis == "V" and self.x > self.priesas_x:
            return True
        if self.y == self.priesas_y and self.kryptis == "R" and self.x < self.priesas_x:
            return True
        return False

    def generuoti_priesa(self):
        self.priesas_x = randint(-10, 10)
        self.priesas_y = randint(-10, 10)

    def suvis(self):
        if self.kryptis == "Š":
            self.suviai[0] += 1
        if self.kryptis == "P":
            self.suviai[1] += 1
        if self.kryptis == "V":
            self.suviai[2] += 1
        if self.kryptis == "R":
            self.suviai[3] += 1
        if self._tikrinti_pataikyma():
            print("PATAIKEI!")
            self.priesai += 1
            self.generuoti_priesa()
            self.taskai += 50

    def irasyti_rekorda(self):
        vardas = input("Įrašykite savo vardą")
        rekordas = {"vardas": vardas, "taskai": self.priesai}
        try:
            with open("rekordas.pkl", 'wb') as failas:
                pickle.dump(rekordas, failas)
        except:
            print("Nepavyko įrašyti rekordų failo")

    def ar_pabaiga(self):
        if self.taskai <= 0:
            if self.gauti_rekorda()['taskai'] < self.priesai:
                print(f"Naujas rekordas: {self.priesai}")
                self.irasyti_rekorda()
            return True
        return False

    def info(self):
        print(f"Koordinatės: X: {self.x}, Y: {self.y}")
        print(f"Priešas: X: {self.priesas_x}, Y: {self.priesas_y}")
        print(f"Kryptis: {self.kryptis}")
        print(f"Taškai: {self.taskai}")
        print("--------------------------")
        print(f"Šūviai: {self.suviai}")
        print(f"Nušauti tankai: {self.priesai}")
