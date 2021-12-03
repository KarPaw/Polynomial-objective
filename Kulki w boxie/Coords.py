from Atom import Atom


class Coords:

    def __init__(self, file):
        # To powinien byc loop wywolujacy kilka razy konstruktor
        # klasy ATOM

        slownik_wszystkich_atomow = self.slownik_atomow(file)
        # print(slownik_wszystkich_atomow)

        # atomy = list(len(slownik_wszystkich_atomow['id']) * [None])
        atomy = list(len(slownik_wszystkich_atomow['id']) * [None])
        # print(atomy)
        # print(len(atomy))
        for i in range(len(slownik_wszystkich_atomow['id'])):
            potrzebne_do_stworzenia_atomu = (slownik_wszystkich_atomow["id"][i],
                                             slownik_wszystkich_atomow["x"][i],
                                             slownik_wszystkich_atomow["y"][i],
                                             slownik_wszystkich_atomow["r"][i],
                                             slownik_wszystkich_atomow["m"][i])

            # Tu tworzymy atomy z konstruktora
            # atomy[i] = Atom(*potrzebne_do_stworzenia_atomu)

            atomy[i] = Atom(*potrzebne_do_stworzenia_atomu)
        # print(atomy)

        # print(atomy)
        # print(atomy[0].get_position)
        # atomy[0] = Atom(*(None, None, None, None, None))
        # print(atomy[0].get_position)

        # self.atomy = atomy
        self.__atomy = atomy

    @staticmethod
    def slownik_atomow(plik):

        slownik = {"id": [],
                   "x": [],
                   "y": [],
                   "r": [],
                   "m": []}

        with open(plik) as f:
            line = iter(f)
            next(line)  # pomijamy pierwsza linijke pliku, czyli naglowek
            for line in f:
                if line[0] == "#":
                    [slownik[klucz].append(None) for klucz in slownik.keys()]

                else:
                    lista_wyrazow_w_linii = line.split()

                    if len(lista_wyrazow_w_linii) != 5:
                        # zamiast wadliwych wynijek dajemy None
                        [slownik[klucz].append(None) for klucz in slownik.keys()]

                    # slownik["id"].append(lista_wyrazow_w_linii[0])
                    # slownik["x"].append(lista_wyrazow_w_linii[1])
                    # slownik["y"].append(lista_wyrazow_w_linii[2])
                    # slownik["r"].append(lista_wyrazow_w_linii[3])
                    # slownik["m"].append(lista_wyrazow_w_linii[4])

                    [slownik[list(slownik.keys())[krotka[0]]].append(krotka[1]) for krotka in enumerate(lista_wyrazow_w_linii)]

        return slownik

    @property
    def get_list_of_atoms(self):
        return self.__atomy

    def __getitem__(self, key):
        return self.__atomy[key]

    def __str__(self):
        return f"{self.get_list_of_atoms}"

    def get_position(self):
        pass

    # do zrobienia
    def __iter__(self):
        lista_atomow = self.get_list_of_atoms
        return iter(lista_atomow)


if __name__ == "__main__":

    c1 = Coords("drugi_przyklad")

    print(c1)
    # print(
    # Coords("drugi_przyklad").get_list_of_atoms
    # )
    #
    # print("siema")
    # print(c1[0], c1[-1])
    #
    # atom0 = c1[0]
    # atom_ostatni = c1[-1]
    # atom0 = c1[0]

    for i in c1:
        print(i)
