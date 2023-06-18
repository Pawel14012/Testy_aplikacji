import unittest
from main import ListaZakupow, ListaZakupowMemento, HistoriaListyZakupow

class TestIntegration(unittest.TestCase):

    def test_zapisz_stan_i_cofnij(self):
        lista_zakupow = ListaZakupow()
        historia = HistoriaListyZakupow(lista_zakupow)

        lista_zakupow.dodaj_produkt("Jabłka")
        historia.zapisz_stan()

        lista_zakupow.dodaj_produkt("Mleko")
        historia.zapisz_stan()

        lista_zakupow.usun_produkt("Mleko")
        historia.zapisz_stan()

        historia.cofnij()

        self.assertEqual(lista_zakupow._produkty, ["Jabłka", "Mleko"])

if __name__ == '__main__':
    unittest.main()
