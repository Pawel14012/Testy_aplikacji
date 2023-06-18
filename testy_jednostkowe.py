import unittest
from io import StringIO
from unittest.mock import patch
from datetime import datetime
from main import ListaZakupow, HistoriaListyZakupow

class ListaZakupowTest(unittest.TestCase):

    def setUp(self):
        self.lista_zakupow = ListaZakupow()
        self.historia = HistoriaListyZakupow(self.lista_zakupow)

    def test_dodaj_produkt(self):
        self.lista_zakupow.dodaj_produkt("Jabłka")
        self.assertIn("Jabłka", self.lista_zakupow._produkty)

    def test_usun_produkt(self):
        self.lista_zakupow.dodaj_produkt("Jabłka")
        self.lista_zakupow.usun_produkt("Jabłka")
        self.assertNotIn("Jabłka", self.lista_zakupow._produkty)

    def test_cofnij(self):
        self.lista_zakupow.dodaj_produkt("Jabłka")
        self.historia.zapisz_stan()
        self.lista_zakupow.usun_produkt("Jabłka")
        self.historia.zapisz_stan()
        self.historia.cofnij()
        self.assertEqual(self.lista_zakupow._produkty, ["Jabłka"])

    


if __name__ == '__main__':
    unittest.main()
