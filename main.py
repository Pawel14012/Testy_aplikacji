from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
import copy


class ListaZakupow:
    def __init__(self) -> None:
        self._produkty = []

    def dodaj_produkt(self, produkt: str) -> None:
        self._produkty.append(produkt)

    def usun_produkt(self, produkt: str) -> None:
        if produkt in self._produkty:
            self._produkty.remove(produkt)

    def wyswietl_liste(self) -> None:
        print("Lista zakupów:")
        for produkt in self._produkty:
            print(produkt)
        print()

    def utworz_memento(self) -> ListaZakupowMemento:
        return ListaZakupowMemento(copy.deepcopy(self._produkty))

    def przywroc(self, memento: ListaZakupowMemento) -> None:
        self._produkty = copy.deepcopy(memento.pobierz_stan())


class ListaZakupowMemento:
    def __init__(self, produkty: list[str]) -> None:
        self._produkty = produkty
        self._data = str(datetime.now())[:19]

    def pobierz_stan(self) -> list[str]:
        return self._produkty

    def pobierz_date(self) -> str:
        return self._data


class HistoriaListyZakupow:
    def __init__(self, lista_zakupow: ListaZakupow) -> None:
        self._historia = []
        self._lista_zakupow = lista_zakupow

    def zapisz_stan(self) -> None:
        memento = self._lista_zakupow.utworz_memento()
        self._historia.append(memento)

    def cofnij(self) -> None:
        if len(self._historia) > 1:
            self._historia.pop()
            memento = self._historia[-1]
            self._lista_zakupow.przywroc(memento)
        elif len(self._historia) == 1:
            self._historia.pop()
            self._lista_zakupow.przywroc(ListaZakupowMemento([]))

    def wyswietl_historie(self) -> None:
        print("Historia listy zakupów:")
        for memento in self._historia:
            data = memento.pobierz_date()
            stan = memento.pobierz_stan()
            print(f"{data}: {stan}")
        print()


if __name__ == "__main__":
    lista_zakupow = ListaZakupow()
    historia = HistoriaListyZakupow(lista_zakupow)

    while True:
        print("Co chcesz zrobić?")
        print("1. Dodaj produkt")
        print("2. Wyświetl listę zakupów")
        print("3. Usuń produkt")
        print("4. Cofnij zmianę")
        print("5. Wyświetl historię zmian")
        print("6. Wyjście")

        wybor = input("Wybierz opcję (1-6): ")

        if wybor == "1":
            produkt = input("Podaj nazwę produktu: ")
            lista_zakupow.dodaj_produkt(produkt)
            historia.zapisz_stan()
            print("Produkt dodany.")
            print()
        elif wybor == "2":
            lista_zakupow.wyswietl_liste()
        elif wybor == "3":
            produkt = input("Podaj nazwę produktu do usunięcia: ")
            lista_zakupow.usun_produkt(produkt)
            historia.zapisz_stan()
            print("Produkt usunięty.")
            print()
        elif wybor == "4":
            historia.cofnij()
            print("Zmiana cofnięta.")
            print()
        elif wybor == "5":
            historia.wyswietl_historie()
        elif wybor == "6":
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")
            print()
