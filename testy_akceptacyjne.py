import unittest
from main import ListaZakupow, ListaZakupowMemento, HistoriaListyZakupow

class TestAcceptance(unittest.TestCase):

    def test_aplikacja(self):
        lista_zakupow = ListaZakupow()
        historia = HistoriaListyZakupow(lista_zakupow)

        lista_zakupow.dodaj_produkt("Jabłka")
        lista_zakupow.dodaj_produkt("Mleko")
        self.assertEqual(lista_zakupow._produkty, ["Jabłka", "Mleko"])


        lista_zakupow.usun_produkt("Jabłka")
        self.assertEqual(lista_zakupow._produkty, ["Mleko"])

        historia.cofnij()
        self.assertEqual(lista_zakupow._produkty, [])

        lista_zakupow.dodaj_produkt("Chleb")
        historia.zapisz_stan()
        lista_zakupow.dodaj_produkt("Jogurt")
        historia.zapisz_stan()

        expected_output = "Historia listy zakupów:\n"
        expected_output += f"{historia._historia[0].pobierz_date()}: {historia._historia[0].pobierz_stan()}\n"
        expected_output += f"{historia._historia[1].pobierz_date()}: {historia._historia[1].pobierz_stan()}\n"

        self.assertEqual(expected_output, historia.wyswietl_historie())

if __name__ == '__main__':
    unittest.main()
