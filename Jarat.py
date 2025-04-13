# Járatok osztálya
class Jarat:
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @property
    def jarat_info(self):
        return f"Járat - adatai: {self.jaratszam}, Cél: {self.celallomas}, Ár: {self.jegyar} Ft"

    @jarat_info.setter
    def jarat_info(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar
