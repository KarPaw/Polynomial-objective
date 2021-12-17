from Coords import Coords
from Energy import Energy


# powinna przechowywac plytkie kopie atomu
# zeby moc zmieniac energie przy zmianie polozenia atomu

class Harmonic(Energy):

    def __init__(self, coords_object, d0, k, i, j):
        # d0 - odległość równowagowa
        # k - stała sprężystości

        self.__d0 = d0
        self.__k = k

        if isinstance(coords_object, Coords):
            self.__coords_object = coords_object
        else:
            raise Exception("parameter is not a Coords_Object")

        self.i = i
        self.j = j

    @property
    def get_d0(self):
        return self.__d0

    @property
    def get_k(self):
        return self.__k

    # Obliczamy enegie Harmoniczna
    def energy(self):

        k = self.get_k
        d0 = self.get_d0

        coords_object = self.__coords_object

        c = coords_object
        c_i = c[int(self.i)]
        c_j = c[int(self.j)]

        d_ij = c_i.distance_to(c_j)

        total_energy = k * (d0 - d_ij)**2

        return total_energy


if __name__ == "__main__":
    c1 = Coords("texts/drugi_przyklad")

    h1 = Harmonic(c1, 0.0, 1, 4, 5)

    print(
        h1.energy()
    )
