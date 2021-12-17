from math import sqrt

class Atom:

    # x, y, m, r
    # def __init__(self, id, x, y, m=1, r=1):
    #
    #     # id atomu
    #
    #     self.__id = id
    #
    #     # polozenie atomu
    #     self.__x = x
    #     self.__y = y
    #
    #     # masa
    #     self.m = m
    #     # promien
    #     self.r = r

    # Do testow # id x  y   r   q
    def __init__(self, id, x, y, r=1, q=0):

        # id atomu
        self.__id = id

        # polozenie atomu
        # self.__x = x
        # self.__y = y

        self.x = x  # Na potrzeby klasy MonteCarlo
        self.y = y  # Musi miec dostep. Przez getter upierdliwe

        # ladunek
        self.q = q
        # promien
        self.r = r

        # jesli informacje niepelne to Tworzymy atom zerowy z indeksem -1
        if None in [id, x, y, r, q]:
            self.__id = -1
            # self.__x, self.__y = 0, 0
            self.x, self.y = 0, 0
            self.q, self.r = 0, 0

    def set(self, x, y):
        # umozliwia zmiane wspolrzednych X oraz Y
        # self.__x = x
        # self.__y = y
        self.x = x
        self.y = y


    @property
    def get_position(self):
        # return self.__x, self.__y
        return self.x, self.y

    def distance_to(self, atom2):

        assert isinstance(atom2, Atom)

        # x1, y1 = self.get_position
        # x2, y2 = atom2.get_position

        # x1, y1 = float(self.__x), float(self.__y)
        # x2, y2 = float(atom2.__x), float(atom2.__y)

        x1, y1 = float(self.x), float(self.y)
        x2, y2 = float(atom2.x), float(atom2.y)

        d = sqrt((x1 - x2)**2 + (y1 - y2)**2)

        return d

    def __str__(self):
        # return f"Atom ID:{self.__id} (X:{self.__x}, Y:{self.__y})"
        return f"Atom ID:{self.__id} (X:{self.x}, Y:{self.y})"


if __name__ == "__main__":
    a1 = Atom(2, 4, 1, 1)
    a2 = Atom(5, 7, 2, 1)

    a3 = Atom(*(None, None, None, None, None))

    print(a1.get_position)
    a1.set(0, 0)
    print(a1.get_position)

    print(a3.get_position)

    print(
        a1.distance_to(a2)
    )


