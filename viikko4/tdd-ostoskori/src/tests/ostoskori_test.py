import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def lisaa_maito(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        return maito

    def lisaa_maito_ja_leipa(self):
        maito = Tuote("Maito", 3)
        leipa = Tuote("Leipä", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)
        return maito, leipa

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.lisaa_maito()

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_oikein(self):
        self.lisaa_maito()

        self.assertEqual(self.kori.hinta(), 3)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        self.lisaa_maito()

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_yksi_ostos_sisaltaa_tuotteen_nimen_ja_lukumaaraan(self):
        self.lisaa_maito()

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.lisaa_maito_ja_leipa()

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        self.lisaa_maito_ja_leipa()

        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korin_hinta_oikein(self):
        self.lisaa_maito_ja_leipa()

        self.assertEqual(self.kori.hinta(), 5)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = self.lisaa_maito()
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        maito = self.lisaa_maito()
        self.kori.lisaa_tuote(maito)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kahden_saman_tuotteen_ostos_sisaltaa_nimen_ja_lukumaaraan_2(self):
        maito = self.lisaa_maito()
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_hinta_oikein(self):
        maito = self.lisaa_maito()
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 6)

    def test_kahden_saman_tuotteen_poistaminen_korista(self):
        maito = self.lisaa_maito()
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.assertEqual(self.kori.hinta(), 6)
        self.assertEqual(ostos.lukumaara(), 2)

        self.kori.poista_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.assertEqual(self.kori.hinta(), 3)
        self.assertEqual(ostos.lukumaara(), 1)

    def test_yhden_tuotteen_poistaminen_korista(self):
        maito = self.lisaa_maito()

        ostos = self.kori.ostokset()[0]

        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.assertEqual(self.kori.hinta(), 3)
        self.assertEqual(ostos.lukumaara(), 1)

        self.kori.poista_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)

    def test_metodi_tyhjenna_toimii(self):
        self.lisaa_maito_ja_leipa()

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.assertEqual(self.kori.hinta(), 5)
        self.assertEqual(len(self.kori.ostokset()), 2)

        self.kori.tyhjenna()

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)
