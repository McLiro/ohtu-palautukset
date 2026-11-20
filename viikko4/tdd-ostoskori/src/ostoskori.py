from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._maara = 0
        self._hinta = 0
        self._ostokset = []

    def tavaroita_korissa(self):
        return self._maara

    def hinta(self):
        return self._hinta

    def lisaa_tuote(self, lisattava: Tuote):
        self._maara += 1
        self._hinta += lisattava.hinta()
        for ostos in self._ostokset:
            if ostos.tuote == lisattava:
                ostos.muuta_lukumaaraa(1)
                return

        self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self._ostokset:
            if ostos.tuote == poistettava:
                if ostos.lukumaara() > 0:
                    ostos.muuta_lukumaaraa(-1)
                    self._maara -= 1
                    self._hinta -= poistettava.hinta()
                    if ostos.lukumaara() == 0:
                        self._ostokset.remove(ostos)
                return

    def tyhjenna(self):
        self._maara = 0
        self._hinta = 0
        self._ostokset.clear()

    def ostokset(self):
        return self._ostokset
