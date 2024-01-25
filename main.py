import os
import re

# Název souboru
soubor_info_naradi = r"c:\\MARTIN\\PROGRAMOVANI\\POKUS\\InfoNaradi.txt"

# Otevření souboru a čtení obsahu
with open(soubor_info_naradi, "r", encoding="utf-8") as soubor:
    obsah = soubor.read()

# Funkce pro vytvoření slovníku ze souboru
def slovnik(obsah):
    # vyřazení specialnich znaku
    pattern = re.compile(r"\s*(.*?):\s*(.*?)\n")

    # Hledání shod v textu
    shody = pattern.findall(obsah)

    #vytvoří slovník a odstraní mezery za a před každym klíčem a promenou
    result_dict = {}
    for key, value in shody:
        result_dict[key.strip()] = value.strip()
    return result_dict

# Funkce pro vytvoření složky na disku podle klíče "zakázka"
def vytvor_slozku_rok(slovnik_obsahu):

    #uloží pomocí klíče proměnou
    zakazka = slovnik_obsahu.get('Zakázka', '')

    if zakazka:
        # Získání prvních dvou čísel z hodnoty klíče "zakázka"
        rok_cisla = zakazka[:2]

        # Vytvoření cesty k nové složce
        nova_slozka_cesta = os.path.join("C:\\", f"Rok 20{rok_cisla}")

        # Vytvoření složky, pokud ještě neexistuje
        if not os.path.exists(nova_slozka_cesta):
            os.makedirs(nova_slozka_cesta)

        print(f"Složka vytvořena: {nova_slozka_cesta}")
    else:
        print("Klíč 'zakázka' není v slovníku nebo nemá hodnotu.")


slovnik_obsahu = slovnik(obsah)
print(slovnik_obsahu)
# Vytvoření složky rok na disku podle klíče "zakázka"
vytvor_slozku_rok(slovnik_obsahu)