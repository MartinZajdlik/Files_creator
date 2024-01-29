import os
import re

# Název souboru
soubor_info_naradi = r"c:\\MARTIN\\PROGRAMOVANI\\POKUS\\InfoNaradi.txt"

# Otevření souboru a čtení obsahu
with open(soubor_info_naradi, "r", encoding="utf-8") as soubor:
    obsah = soubor.read()

# Funkce pro vytvoření slovníku ze souboru
def slovnik(obsah):
    pattern = re.compile(r"\s*(.*?):\s*(.*?)\n")
    shody = pattern.findall(obsah)
    result_dict = {}
    for key, value in shody:
        result_dict[key.strip()] = value.strip()
    return result_dict

# Funkce pro vytvoření složek na disku podle klíčů "Zakázka", "Zákazník", "Projekt", "Číslo dílce" a "Nářadí"
def vytvor_slozky(slovnik_obsahu):
    zakazka = slovnik_obsahu.get('Zakázka', '')

    if zakazka:
        # Vytvoření složky pro rok
        rok_cisla = zakazka[:2]
        nova_slozka_cesta_rok = os.path.join("C:\\", f"Rok 20{rok_cisla}")

        # Ověření jestli složka existuje
        if not os.path.exists(nova_slozka_cesta_rok):
            os.makedirs(nova_slozka_cesta_rok)
            print(f"Složka pro rok vytvořena: {nova_slozka_cesta_rok}")

        zakaznik = slovnik_obsahu.get('Zákazník', '')
        projekt = slovnik_obsahu.get('Projekt', '')

        # Vytvoření složky pro zákazníka a projekt
        nova_slozka_cesta_zakaznik = os.path.join(nova_slozka_cesta_rok, zakaznik)
        nova_slozka_cesta_projekt = os.path.join(nova_slozka_cesta_zakaznik, projekt)

         # Ověření jestli složka existuje
        if not os.path.exists(nova_slozka_cesta_zakaznik):
            os.makedirs(nova_slozka_cesta_zakaznik)
            print(f"Složka pro zákazníka vytvořena: {nova_slozka_cesta_zakaznik}")

         # Ověření jestli složka existuje
        if not os.path.exists(nova_slozka_cesta_projekt):
            os.makedirs(nova_slozka_cesta_projekt)
            print(f"Složka pro projekt vytvořena: {nova_slozka_cesta_projekt}")

        cislo_dilce = slovnik_obsahu.get('Číslo dílce', '')

        # Vytvoření složky pro číslo dílce a zakázku
        nova_slozka_cesta_cislo_dilce = os.path.join(nova_slozka_cesta_projekt, f"{cislo_dilce}_{zakazka}")

         # Ověření jestli složka existuje
        if not os.path.exists(nova_slozka_cesta_cislo_dilce):
            os.makedirs(nova_slozka_cesta_cislo_dilce)
            print(f"Složka pro číslo dílce a zakázku vytvořena: {nova_slozka_cesta_cislo_dilce}")

        naradi = slovnik_obsahu.get('Nářadí', '')

        if naradi:
            # Extracting the word between hyphens
            naradi_word = re.search(r'-(.*?)-', naradi)
            if naradi_word:
                naradi_word = naradi_word.group(1).strip()

                # Vytvoření složky pro 'Nářadí'
                nova_slozka_cesta_naradi = os.path.join(nova_slozka_cesta_cislo_dilce, naradi_word)

                 # Ověření jestli složka existuje
                if not os.path.exists(nova_slozka_cesta_naradi):
                    os.makedirs(nova_slozka_cesta_naradi)
                    print(f"Složka pro 'Nářadí' vytvořena: {nova_slozka_cesta_naradi}")
            else:
                print("Nářadí neobsahuje slovo mezi - -.")
        else:
            print("Klíč 'Nářadí' není v slovníku nebo nemá hodnotu.")

    else:
        print("Klíč 'Zakázka' není v slovníku nebo nemá hodnotu.")

# Vytvoření slovníku obsahu ze souboru
slovnik_obsahu = slovnik(obsah)

# Vytvoření složek na disku podle klíčů "Zakázka", "Zákazník", "Projekt", "Číslo dílce" a "Nářadí"
vytvor_slozky(slovnik_obsahu)
