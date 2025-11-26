"""
NOWE ĆWICZENIE: Lista zakupów z pętlą
======================================

Zadanie:
Napisz program, który:
1. Tworzy pustą listę zakupów
2. W pętli pyta użytkownika o produkty do dodania
3. Użytkownik może dodawać produkty, aż wpisze "koniec"
4. Po zakończeniu wyświetla całą listę zakupów z numeracją
5. Pyta czy chce usunąć jakiś produkt (opcjonalnie)

Nowe elementy Pythona:
- LISTY: lista = []  (pusta lista)
- DODAWANIE: lista.append(element)
- PĘTLA WHILE: while warunek:
- PĘTLA FOR: for element in lista:
- SPRAWDZANIE: if element in lista:
- USUWANIE: lista.remove(element) lub del lista[indeks]
- LEN: len(lista) - długość listy
- ENUMERATE: for i, element in enumerate(lista) - numeracja

Przykład działania:
Dodaj produkt (lub 'koniec'): chleb
Dodaj produkt (lub 'koniec'): mleko
Dodaj produkt (lub 'koniec'): jajka
Dodaj produkt (lub 'koniec'): koniec

Twoja lista zakupów:
1. chleb
2. mleko
3. jajka
"""

# TODO: Napisz tutaj swój kod!

# Krok 1: Utwórz pustą listę: zakupy = []
# Krok 2: Użyj pętli while True: do dodawania produktów
# Krok 3: W pętli: pobierz produkt, sprawdź czy to "koniec", jeśli nie to dodaj do listy
# Krok 4: Po wyjściu z pętli wyświetl listę z numeracją (użyj enumerate lub range)
# Krok 5: (Opcjonalnie) Zapytaj czy chce usunąć produkt i usuń go

# ============================================
# NOWE: PRACA Z PLIKAMI
# ============================================
# Funkcja do zapisywania listy do pliku
def zapisz_do_pliku(lista, nazwa_pliku="zakupy.txt"):
    """Zapisuje listę do pliku - jeden produkt na linię"""
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        for produkt in lista:
            plik.write(produkt + "\n")
    print(f"Lista zapisana do pliku {nazwa_pliku}")

# Funkcja do odczytywania listy z pliku
def wczytaj_z_pliku(nazwa_pliku="zakupy.txt"):
    """Wczytuje listę z pliku"""
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            lista = [linia.strip() for linia in plik.readlines()]
        return lista
    except FileNotFoundError:
        # Jeśli plik nie istnieje, zwróć pustą listę
        return []

# ============================================
# GŁÓWNY PROGRAM
# ============================================

# Krok 1: Wczytaj istniejącą listę (jeśli istnieje)
zakupy = wczytaj_z_pliku()
if zakupy:
    print("Wczytano istniejącą listę zakupów:")
    for i, product in enumerate(zakupy):
        print(f"{i+1}. {product}")
    print()

# Krok 2: Dodawanie nowych produktów
while True:
    product = input("Add a product (or 'end'): ")
    if product == "end":
        break
    zakupy.append(product)

# Krok 3: Wyświetl całą listę
print("\nTwoja lista zakupów:")
for i, product in enumerate(zakupy):
    print(f"{i+1}. {product}")

# Krok 4: Usuwanie 
while True:
    if input("\nDo you want to remove a product? (y/n): ") == "y":
        product_to_remove = input("Enter the product to remove: ")
        if product_to_remove in zakupy:
            zakupy.remove(product_to_remove)
            print(f"Usunięto: {product_to_remove}")
        else:
            print(f"Produkt '{product_to_remove}' nie znajduje się na liście")
    odpowiedz = input("\nDo you want to remove another product? (y/n): ")
    if odpowiedz == "n":
        break
    elif odpowiedz == "y":
        print("Dalej usuwamy produkty")
        remove_else = input("What product else do yout want to remove?")
        if remove_else in zakupy:
            zakupy.remove(remove_else)
            print(f"Usunięto: {remove_else}")
            continue
        else:
            print(f"Produkt '{remove_else}' nie znajduje się na liście")
    else:
        print("Nieprawidłowa odpowiedź. Wpisz 'y' lub 'n'")
# Krok 5: ZAPISZ LISTĘ DO PLIKU
zapisz_do_pliku(zakupy)
print("\nLista została zapisana! Możesz zamknąć program.")