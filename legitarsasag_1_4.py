
from Jarat import Jarat
from LegiTarsasag import LegiTarsasag
from JegyFoglalas import JegyFoglalas


# Légitársaság foglalási konzol rendszer
#run csak önálló futtatáskor
if __name__ == "__main__":
    # Rendszer feltöltése adatokkal
    #legi_tarsasag = LegiTarsasag("GDE-Travel")
    legi_tarsasag = LegiTarsasag()
    legi_tarsasag.nev = "GDE-Travel"

    legi_tarsasag.add_jarat(Jarat("BELFÖLD-1", "Budapest", 10000))
    legi_tarsasag.add_jarat(Jarat("BELFÖLD-2", "Debrecen", 8000))
    legi_tarsasag.add_jarat(Jarat("NEMZETKÖZI-1", "London", 50000))
    legi_tarsasag.add_jarat(Jarat("NEMZETKÖZI-2", "Naples", 40000))
    legi_tarsasag.add_jarat(Jarat("NEMZETKÖZI-3", "St Helena Island", 400000))

    foglalas_rendszer = JegyFoglalas()
    foglalas_rendszer.foglalas(legi_tarsasag.jaratok[0], "Kiss János")
    foglalas_rendszer.foglalas(legi_tarsasag.jaratok[1], "Nagy Anna")
    foglalas_rendszer.foglalas(legi_tarsasag.jaratok[2], "Tóth Péter")
    foglalas_rendszer.foglalas(legi_tarsasag.jaratok[3], "Edebede Bá")
    foglalas_rendszer.foglalas(legi_tarsasag.jaratok[4], "Apu Fortyogó Epéje")
    foglalas_rendszer.foglalas(legi_tarsasag.jaratok[4], "Tayler Durden")

    # Felhasználói felület terminál használata esetén
    while True:
        print("\n GDE-Travel - Készítette: Kiss Sándor O2WN7M \n1. Járatok listázása\n2. Jegy foglalása\n3. Foglalás lemondása\n4. Foglalások listázása\n5. Kilépés")
        valasztas = input("Válasszon egy lehetőséget: ")

        if valasztas == "1":
            legi_tarsasag.list_jaratok()

        elif valasztas == "2":
            # Járat megadása járatlista sorszám alapján
            jarat_szama = int(input("Adja meg a járat sorszámát: ")) - 1
            utas_nev = input("Adja meg az utas nevét: ")
            # Ellenőrzés, hogy a megadott sorszám érvényes-e
            if jarat_szama < 0 or jarat_szama >= len(legi_tarsasag.jaratok):
                print("Érvénytelen járatszám!")
                continue
            jarat = legi_tarsasag.jaratok[jarat_szama]

            if jarat:
                foglalas_rendszer.foglalas(jarat, utas_nev)
            else:
                print("Érvénytelen járatszám!")

        elif valasztas == "3":
            foglalas_id = int(input("Adja meg a foglalás ID-t: "))
            foglalas_rendszer.lemondas(foglalas_id)

        elif valasztas == "4":
            foglalas_rendszer.list_foglalasok()

        elif valasztas == "5":
            break
        else:
            print("Érvénytelen választás!")

