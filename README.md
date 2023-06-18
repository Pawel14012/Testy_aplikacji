# Testy_aplikacji



## Dokumentacja projektowa – testów aplikacji
## Paweł Jakubaszek 14012
### Struktura aplikacji
Aplikacja wykorzystuje wzorzec architektoniczny Model-Widok-Kontroler (MVC), który podziela kod na trzy główne komponenty:
1. Model:
*	(`ListaZakupow`): Reprezentuje model listy zakupów. Zarządza stanem listy zakupów, udostępnia metody do modyfikacji listy oraz tworzenia memento do przechowywania i przywracania stanu.
2. Widok:
*	Interfejs użytkownika (CLI): Główna część kodu obsługuje interakcje użytkownika za pomocą interfejsu wiersza poleceń (CLI). Wyświetla opcje menu i prosi użytkownika o wprowadzenie danych. Pokazuje również listę zakupów oraz historię zmian na żądanie.
3. Kontroler:
*	(`HistoriaListyZakupow`): Pełni rolę kontrolera w wzorcu MVC. Zarządza historią listy zakupów, zapisuje stany, cofa zmiany oraz wyświetla historię.
*	Kontroler współdziała zarówno z modelem (`ListaZakupow`), jak i z widokiem (CLI), aby koordynować działania i dostarczać odpowiednią funkcjonalność.
### Podział struktury:
- Klasa „ListaZakupow” reprezentuje model. Zawiera listę zakupów i udostępnia metody do dodawania i usuwania produktów, wyświetlania listy, tworzenia memento oraz przywracania stanu z memento.
- Klasa 'ListaZakupowMemento' reprezentuje obiekt memento. Przechwytuje stan listy zakupów w określonym punkcie czasowym. Zawiera listę produktów oraz datę utworzenia memento.
- Klasa 'HistoriaListyZakupow' pełni rolę kontrolera. Zarządza historią listy zakupów i współdziała zarówno z modelem, jak i z widokiem. Udostępnia metody do zapisywania stanu, cofania zmian oraz wyświetlania historii.
- Menu użytkownika: pobiera dane wejściowe i wywołuje odpowiednie metody kontrolera i modelu na podstawie wybranej opcji. Wyświetla również listę zakupów oraz historię na żądanie.


### Scenariusze testów
A.Jednostkowe:
1.	Test dodający produkty:
*	Nowa lista produktów
*	Dodajemy produkty za pomocą metody dodaj_produkt
2.	Test usuwający produkty:
*	Tworzymy nową listę produktów
*	Dodajemy produkty za pomocą metody dodaj_produkt
*	Usuwamy jeden z produktow
3.	Test cofający zmiany w liscie zakupów
*	Nowa lista produktów
*	Dodajemy produkty za pomocą metody dodaj_produkt
*	Wyswietlamy liste 
*	Usuwamy produkt
*	Sprawdzamy liste zakupów
*	Cofamy zmiane przy uzyciu cofnij_zmiane
*	Sprawdzamy czy usunięty produkt został przywrócony

B.Integracyjne:
1.	Dodawanie produktu i wyswietlanie listy:
*	Z menu wybieramy dodawanie produktu
*	Wpisujemy nazwe produktu
*	Ponownie dodajemy produkt
*	Usuwamy produkt
*	Cofamy zmiany

C.Akceptacyjne:
1.	Dodawanie produktu, usuwanie go , cofnięcie zmian i wyjście z programu
*	Wybieramy dodawanie produktu z listy 
*	Wpisujemy nazwe produktu
*	Dodajemy kolejny produkt
*	Wybieramy usuwanie produktu 
*	Wpisujemy nazwe produktu do usuniecia
*	Cofamy zmiany w menu
*	Dodajemy kolejne 2 produkty
*	Sprawdzamy czy wyświetlana jest odpowiednia historia zakupów

### Wykorzystane narzędzia i biblioteki:
1.	Język programowania Python:Za jego pomocą została napisana ta aplikacja
2.	Moduły:
*	Datetime: do pobierania aktualnej daty i czasu 
*	Unittest: do tworzenia testów jednostkowych, integracyjnych i akceptacyjnych aplikacji
*	StringIO: dostarcza mozliwosc tworenia obiektów strumieniowych, które działaja jak pliki przechowujace dane w pamięci(przechwytywał dane wyjsciowe i porównywał z tymi oczekiwanymi w testach)

### Ewentualne problemy i ich rozwiązania
1.	W aplikacji mogą wystąpić błedy logiczne, które mogą prowadzić do złych wyników lub dziwnego działania programu, aby temu zapobiec trzeba przeglądać kod regularnie i testować aplikacje 
2.	Błedne testy – żeby testy były prawidłowo wykonane musi je wykonać osoba zajmująca się testami profesjonalnie, ponieważ będzie ona miała inne spojrzenie na naszą aplikację i zastosuje testy, o których my możemy nie pomysleć
3.	Aplikacja może działać różnie w różnych środowiskach dlatego trzeba zadbać o odpowiednie dokumentowanie kodu, czytelność  jak i również modularność kodu.
4.	Niedostateczne pokrycie testowe: Istnieje ryzyko, że nie wszystkie scenariusze i gałęzie kodu zostaną pokryte przez testy, co może prowadzić do niedostrzeżenia błędów i nieodkrycia ważnych defektów







