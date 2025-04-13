import legitarsasag_1_3 as LT
import tkinter as tk
from tkinter import messagebox
import time

from Jarat import Jarat
from LegiTarsasag import LegiTarsasag
from JegyFoglalas import JegyFoglalas


# JegyFoglalas osztály bővítése rögzítési idővel, JegyFoglalas osztály módosítása
class JegyFoglalas(JegyFoglalas):
    def __init__(self):
        super().__init__()  #hívja meg az ősosztály konstruktorát
        self.IDmax = 0

    def foglalas(self, jarat, utas_nev):
        foglalas_id = self.IDmax + 1
        foglalas_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.foglalasok.append({"id": foglalas_id, "jarat": jarat, "utas_nev": utas_nev, "foglalas_time": foglalas_time})
        self.IDmax += 1

# Rendszer feltöltése adatokkal
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

# GUI funkció
def start_gui():
    def repulo_lista():
        repulok_lista.delete(0, tk.END)
        for jarat in legi_tarsasag.jaratok:
            sorszam = legi_tarsasag.jaratok.index(jarat) + 1
            #repulok_lista.insert(tk.END, f"{sorszam} -> {jarat.get_jarat_info()}")
            repulok_lista.insert(tk.END, f"{sorszam} -> {jarat.jarat_info}")

    def jegy_foglalas():
        try:
            jarat_szama = int(repulo_bevitel.get()) - 1
            utas_nev = entry_passenger_name.get()
            if jarat_szama < 0 or jarat_szama >= len(legi_tarsasag.jaratok):
                messagebox.showerror("Hiba", "Érvénytelen járatszám!")
                return
            jarat = legi_tarsasag.jaratok[jarat_szama]
            foglalas_rendszer.foglalas(jarat, utas_nev)
            messagebox.showinfo("Siker", "Foglalás sikeres!")
        except ValueError:
            messagebox.showerror("Hiba", "Érvénytelen bemenet!")

    def jegy_torles():
        try:
            foglalas_id = int(entry_booking_id.get())
            foglalas_rendszer.lemondas(foglalas_id)
        except ValueError:
            messagebox.showerror("Hiba", "Érvénytelen foglalás ID!")

    def foglalas_lista():
        bookings_list.delete(0, tk.END)
        if not foglalas_rendszer.foglalasok:
            bookings_list.insert(tk.END, "Nincsenek foglalások.")
        for foglalas in foglalas_rendszer.foglalasok:
            sorszam = foglalas_rendszer.foglalasok.index(foglalas) + 1
            bookings_list.insert(tk.END, f"{sorszam} ... ID:{foglalas['id']}, Járat: {foglalas['jarat'].jaratszam}, Utas: {foglalas['utas_nev']},/"
                                         f"Ár: {foglalas['jarat'].jegyar} Ft, Foglalás idő: {foglalas['foglalas_time']}")

    def exit_program():
        gui.destroy()

    # Főablak létrehozása
    gui = tk.Tk()
    gui.title("GDE Aeroplane Járatkezelő - Készítette: Kiss Sándor O2WN7M")
    gui.rowconfigure(0, weight=1)
    gui.columnconfigure(0, weight=1)
    gui.geometry("600x800")

    # Keret létrehozása
    main_frame = tk.Frame(gui, padx=4, pady=4)
    main_frame.grid(sticky="nsew")
    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=1)
    main_frame.rowconfigure(2, weight=1)
    main_frame.rowconfigure(3, weight=1)
    main_frame.rowconfigure(4, weight=1)
    main_frame.columnconfigure(0, weight=1)

    # Járatok listája
    repulok_frame = tk.Frame(main_frame, relief="groove", borderwidth=2)
    repulok_frame.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)
    repulok_frame.rowconfigure(0, weight=1)
    repulok_frame.columnconfigure(0, weight=1)
    tk.Label(repulok_frame, text="Járatok:").grid(row=0, column=0, sticky="n")
    repulok_lista = tk.Listbox(repulok_frame)
    repulok_lista.grid(row=1, column=0, sticky="nsew")
    tk.Button(repulok_frame, text="Járatok listázása", command=repulo_lista, width=20, height=2).grid(row=2, column=0, sticky="ew")

    # Jegy foglalása
    foglal_frame = tk.Frame(main_frame, relief="groove", borderwidth=2)
    foglal_frame.grid(row=1, column=0, sticky="nsew", padx=4, pady=4)
    foglal_frame.rowconfigure(0, weight=1)
    foglal_frame.columnconfigure(0, weight=1)
    tk.Label(foglal_frame, text="Jegy foglalása:").grid(row=0, column=0, sticky="n")
    tk.Label(foglal_frame, text="Járatszám:").grid(row=1, column=0, sticky="w")
    repulo_bevitel = tk.Entry(foglal_frame)
    repulo_bevitel.grid(row=2, column=0, sticky="ew")
    tk.Label(foglal_frame, text="Utas neve:").grid(row=3, column=0, sticky="w")
    entry_passenger_name = tk.Entry(foglal_frame)
    entry_passenger_name.grid(row=4, column=0, sticky="ew")
    tk.Button(foglal_frame, text="Foglalás", command=jegy_foglalas, width=20, height=2).grid(row=5, column=0, sticky="ew")

    # Foglalás lemondása
    lemond_frame = tk.Frame(main_frame, relief="groove", borderwidth=2)
    lemond_frame.grid(row=2, column=0, sticky="nsew", padx=4, pady=4)
    lemond_frame.rowconfigure(0, weight=1)
    lemond_frame.columnconfigure(0, weight=1)
    tk.Label(lemond_frame, text="Foglalás lemondása:").grid(row=0, column=0, sticky="n")
    tk.Label(lemond_frame, text="Foglalás ID").grid(row=1, column=0, sticky="w")
    entry_booking_id = tk.Entry(lemond_frame)
    entry_booking_id.grid(row=2, column=0, sticky="ew")
    tk.Button(lemond_frame, text="Lemondás", command=jegy_torles, width=20, height=2).grid(row=3, column=0, sticky="ew")

    # Foglalások listája
    foglal_frame = tk.Frame(main_frame, relief="groove", borderwidth=2)
    foglal_frame.grid(row=3, column=0, sticky="nsew", padx=4, pady=4)
    foglal_frame.rowconfigure(0, weight=1)
    foglal_frame.columnconfigure(0, weight=1)
    tk.Label(foglal_frame, text="Foglalások:").grid(row=0, column=0, sticky="n")
    bookings_list = tk.Listbox(foglal_frame)
    bookings_list.grid(row=1, column=0, sticky="nsew")
    tk.Button(foglal_frame, text="Foglalások listázása", command=foglalas_lista, width=20, height=2).grid(row=2, column=0, sticky="ew")

    # Kilépés gomb
    exit_frame = tk.Frame(main_frame, relief="groove", borderwidth=2)
    exit_frame.grid(row=4, column=0, sticky="nsew", padx=4, pady=4)
    exit_frame.rowconfigure(0, weight=1)
    exit_frame.columnconfigure(0, weight=1)
    tk.Button(exit_frame, text="Kilépés", command=exit_program, width=20, height=2).grid(row=0, column=0, sticky="ew")

    gui.mainloop()

start_gui()