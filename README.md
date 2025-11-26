# Lista Zakupów - Program Python

Prosty program do zarządzania listą zakupów napisany w Pythonie.

## Opis

Program pozwala na:
- Dodawanie produktów do listy zakupów
- Usuwanie produktów z listy
- Automatyczne zapisywanie listy do pliku `zakupy.txt`
- Wczytywanie zapisanej listy przy starcie programu

## Wymagania

- Python 3.x

## Jak uruchomić

```bash
python cwiczenie3.py
```

## Jak używać

1. **Dodawanie produktów:**
   - Program poprosi Cię o wpisanie produktu
   - Wpisz nazwę produktu i naciśnij Enter
   - Aby zakończyć dodawanie, wpisz `end`

2. **Usuwanie produktów:**
   - Po wyświetleniu listy, program zapyta czy chcesz usunąć produkt
   - Wpisz `y` (yes) aby usunąć produkt
   - Wpisz nazwę produktu do usunięcia
   - Możesz kontynuować usuwanie kolejnych produktów

3. **Zapisywanie:**
   - Lista automatycznie zapisuje się do pliku `zakupy.txt`
   - Przy następnym uruchomieniu programu lista zostanie automatycznie wczytana

## Funkcje

- `zapisz_do_pliku()` - zapisuje listę do pliku tekstowego
- `wczytaj_z_pliku()` - wczytuje listę z pliku (jeśli istnieje)

## Przykład użycia

```
Add a product (or 'end'): chleb
Add a product (or 'end'): mleko
Add a product (or 'end'): jajka
Add a product (or 'end'): end

Twoja lista zakupów:
1. chleb
2. mleko
3. jajka

Do you want to remove a product? (y/n): y
Enter the product to remove: mleko
Usunięto: mleko
```

## Pliki

- `cwiczenie3.py` - główny plik programu
- `zakupy.txt` - plik z zapisaną listą zakupów (tworzony automatycznie)

## Nauka Pythona

Ten program demonstruje:
- Pętle (`while`, `for`)
- Listy i operacje na listach
- Funkcje (`def`)
- Pracę z plikami (`open`, `read`, `write`)
- Obsługę błędów (`try/except`)
- Warunki (`if/elif/else`)

