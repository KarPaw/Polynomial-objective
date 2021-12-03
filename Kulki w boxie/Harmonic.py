from Coords import Coords
from Energy import Energy

# powinna przechowywac plytkie kopie atomu
# zeby moc zmieniac energie przy zmianie polozenia atomu

class Harmonic(Energy):

    def __init__(self, d0, k):
        # zrob sprezynke
        # d0 - odległość równowagowa
        # k - stała sprężystości

        self.__d0 = d0
        self.__k = k

    @property
    def get_d0(self):
        return self.__d0

    @property
    def get_k(self):
        return self.__k

    def energy(self):

        k = self.get_k
        d0 = self.get_d0
        # trzeba zrobic __get_item__ w Coords
        d_ij = Coords[i].distance_to(Coords[j])


        E = k*(d0 - d_ij)

        return E
