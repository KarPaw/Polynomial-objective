from Energy import Energy
from HarmonicMaker import HarmonicMaker
from CoulombMaker import CoulombMaker
from RepulsionMaker import RepulsionMaker
from Coords import Coords


class Total_Energy(Energy):

    def __init__(self, crd: Coords):
        self.__makers = {"HARMONIC": HarmonicMaker(),
                         "COULOMB": CoulombMaker(),
                         "REPULSION": RepulsionMaker()
                         }

        self.__ene_lista = []   # Lista obiektow typu Rep/Har/Coul


        self.__crd = crd    # Plytka kopia Coords.

    def from_file(self, fname:str):

        crd = self.__crd
        en_list = self.__ene_lista
        with open(fname) as f:
            for line in f:
                if line[0] != "#":
                    lista_wyrazow_w_linii = line.split()
                    lwl = lista_wyrazow_w_linii

                energy_type = lwl[0]
                maker = self.__makers[energy_type]

                # type(maker) -> Rep..Maker / Har...Maker / Col..Maker
                ene_obj = maker

                if energy_type == "HARMONIC":
                    i, j, d0, k = map(float, lwl[1:5])

                    do_przekazania = (i, j, d0, k)
                    en = ene_obj.make(crd, *do_przekazania)
                    en_list.append(en)

                elif energy_type == "COULOMB" or "REPULSION":
                    c = float(lwl[1])
                    do_przekazania = c
                    en = ene_obj.make(crd, do_przekazania)
                    en_list.append(en)

                else:
                    raise NotImplementedError

        return en_list

    def energy(self):
        total = 0
        lst_ene = self.__ene_lista
        tete = iter(lst_ene)

        for obj in tete:
            energy_val = obj.energy()
            total += energy_val

        return total

if __name__ == "__main__":

    c1 = Coords("testy\sim2d-system.txt")

    factory = Total_Energy(c1)
    print(factory.energy())     # 0
    # wrzucamy dane potrzebne do policzenia energii
    factory.from_file("testy\sim2d-energy.txt")
    print(factory.energy())     # 246


