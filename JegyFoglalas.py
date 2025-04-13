# Jegyek foglalásához szükséges osztály
class JegyFoglalas:
    def __init__(self):
        self._foglalasok = []
        self.IDmax = 0

    @property
    def foglalasok(self):
        return self._foglalasok

    @foglalasok.setter
    def foglalasok(self, foglalasok):
        if not isinstance(foglalasok, list):
            raise TypeError("A foglalásoknak listának kell lennie")
        self._foglalasok = foglalasok

    def add_foglalas(self, jarat):
        self._foglalasok.append(jarat)

    def foglalas(self, jarat, utas_nev):
        foglalas_id = self.IDmax + 1
        self.foglalasok.append({"id": foglalas_id, "jarat": jarat, "utas_nev": utas_nev})
        print(f"Foglalás sikeres! Foglalás ID: {foglalas_id}, Ár: {jarat.jegyar} Ft")
        self.IDmax += 1

    def lemondas(self, foglalas_id):
        for foglalas in self.foglalasok:
            if foglalas["id"] == foglalas_id:
                self.foglalasok.remove(foglalas)
                print(f"Foglalás lemondva: {foglalas_id}")
                return
        print("Érvénytelen foglalás ID!")

    def list_foglalasok(self):
        if not self.foglalasok:
            print("Nincsenek foglalások.")
        for foglalas in self.foglalasok:
            print(f"ID: {foglalas['id']}, Járat: {foglalas['jarat'].jaratszam}, Utas: {foglalas['utas_nev']}")