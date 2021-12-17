from Atom import Atom


class Coords:

    def __init__(self, file):
        # loop wywolujacy kilka razy konstruktor klasy ATOM
        slownik_wszystkich_atomow = self.dict_of_atoms(file)

        atomy = list(len(slownik_wszystkich_atomow['id']) * [None])

        for var in range(len(slownik_wszystkich_atomow['id'])):
            # for i in tatata:
            potrzebne_do_stworzenia_atomu = (slownik_wszystkich_atomow["id"][var],
                                             slownik_wszystkich_atomow["x"][var],
                                             slownik_wszystkich_atomow["y"][var],
                                             slownik_wszystkich_atomow["r"][var],
                                             # slownik_wszystkich_atomow["m"][i],
                                             slownik_wszystkich_atomow["q"][var])
            # Tu tworzymy atomy z konstruktora
            atomy[var] = Atom(*potrzebne_do_stworzenia_atomu)

        self.__atomy = atomy
        # zeby iterator nam nie przestrzelil za liste
        self.n_atoms = len(atomy)   # publiczne - dla klasy MonteCarlo


    @staticmethod
    def dict_of_atoms(file):

        slownik = {"id": [],
                   "x": [],
                   "y": [],
                   "r": [],
                   # "m": []}
                   "q": []}

        with open(file) as f:
            # next(line)  # pomijamy pierwsza linijke pliku, czyli naglowek
            for line in f:
                if line[0] == "#":
                    [slownik[klucz].append(None) for klucz in slownik.keys()]

                else:
                    lista_wyrazow_w_linii = line.split()

                    # if len(lista_wyrazow_w_linii) != 5:
                    #     # zamiast wadliwych linijek dajemy None
                    #     [slownik[klucz].append(None) for klucz in slownik.keys()]

                    # slownik["id"].append(lista_wyrazow_w_linii[0])
                    # slownik["x"].append(lista_wyrazow_w_linii[1])
                    # slownik["y"].append(lista_wyrazow_w_linii[2])
                    # slownik["r"].append(lista_wyrazow_w_linii[3])
                    # slownik["m"].append(lista_wyrazow_w_linii[4])

                    [slownik[list(slownik.keys())[krotka[0]]].append(krotka[1]) for krotka in
                     enumerate(lista_wyrazow_w_linii)]

        return slownik

    @property
    def get_list_of_atoms(self):
        return self.__atomy

    def __getitem__(self, key):
        return self.__atomy[key]

    def __str__(self):

        return f"{self.get_list_of_atoms}"

    def __iter__(self):
        self.__num = 0
        return self

    def __next__(self):

        if self.__num < self.n_atoms:
            xxx = self.__num
            self.__num += 1

            return self.__atomy[xxx]
        else:
            raise StopIteration


if __name__ == "__main__":

    c1 = Coords("texts/drugi_przyklad")
    d = iter(c1)

    print(d)

    for i in d:
        print(i)

