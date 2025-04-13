# Légitársaság osztálya
class LegiTarsasag:
    def __init__(self):
        self._nev = ""
        self._jaratok = []

    @property
    def nev(self):
        return self.nev

    @nev.setter
    def nev(self, nev:str):
        if not isinstance(nev, str):
            raise TypeError("A névnek stringnek kell lennie")
        self._nev = nev

    @property
    def jaratok(self):
        return self._jaratok

    @jaratok.setter
    def jaratok(self, jaratok:list):
        self._jaratok = jaratok

    def add_jarat(self, jarat):
        self._jaratok.append(jarat)

    def jarat_torles(self, jarat):
        if jarat in self._jaratok:
            self._jaratok.remove(jarat)
        else:
            print("Járat nem található!")

    def list_jaratok(self):
        for jarat in self.jaratok:
            sorszam = self._jaratok.index(jarat) + 1
            print(f"{sorszam} -> {jarat.jarat_info}")