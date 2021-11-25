class Polynomial:

    def __init__(self, *cof):
        # Uzytkownik podaje od najwiekszej potegi
        # Ale w implementacji jest od wyrazu wolnego...

        # Przykladowy input uzytkownika:
        # x^7 -5x +4 -> [1, 0, -5, 0, 0, 0, 0, 4]
        # w implementacji [4, ....., 1]

        k1 = []
        # DEEP COPY
        # Na "self.__k1" bedziemy operowac
        if isinstance(cof[0], list) and cof[0]:
            for i in range(len(cof[0][::-1])):
                k1.append(cof[0][::-1][i])
        # Gdy chcemy zrobic wielomian z wielomianu
        elif isinstance(cof[0], Polynomial):
            k1 = cof[0].__k1
        # Gdy inputem jest "None" albo "0"
        elif (not cof) or cof == 0:
            k1 = 0
        # Gdy jest to "lista" wpisana bez nawiasow [ ]
        else:
            for i in range(len(cof[::-1])):
                k1.append(cof[::-1][i])

        self.__k1 = k1

    # Robimy getter jako metode property
    @property
    def coefficients(self):
        coefficients = []
        for i in range(len(self.__k1)):
            coefficients.append(self.__k1[i])

        # Zeby nie dalo sie dopisac nic XD Tak sie robi immutable liste
        # az sie zdziwilem ze zadzialalo
        return list(tuple(self.__k1))

    def __add__(self, p2):
        # Ta metoda jest dobrze opisana, jest tu sporo komentarzy wyjasniajacych rzeczy
        # ktore moga byc niejasne w innych miejscach
        p3 = []
        if isinstance(self, Polynomial) and isinstance(p2, Polynomial):
            iteracja = 0

            while iteracja < (min(len(self.__k1), len(p2.__k1))):
                p3.append(self.__k1[iteracja]+p2.__k1[iteracja])
                iteracja += 1

            # ktora dluzsza
            if len(p2.__k1) - len(self.__k1) >= 0:
                # to p2 jest dluzsze
                ogon = p2.__k1[iteracja:max(len(self.__k1), len(p2.__k1))]

            else:
                ogon = self.__k1[iteracja:max(len(self.__k1), len(p2.__k1))]

            p3 = p3+ogon

            return Polynomial(p3[::-1])

        # Radzimy sobie z liczbami...
        # Ale skaldnia musi byc "Poly + liczba"
        # "liczba + Poly" nie dziala, bo np. INT nie ma takiej metody w swojej klasie... <- (*odsylacz*)
        # int.__add__(Polynomial(...)) - zeby dzialalo trzebaby zmienic wbudowane dodawanie...
        elif isinstance(self, Polynomial) ^ isinstance(p2, Polynomial):
            liczba, wielomian = p2, self
            [p3.append(i) for i in wielomian.__k1]
            p3[0] += liczba
            return Polynomial(p3[::-1])
        # else jest niepotrzebne, bo Zajrzyj do -> (*odsylacz*) w linijce 66
        # w pozostalych dzialaniach tez nie bedzie

    def __iadd__(self, p2):
        # to ma być " += "
        if isinstance(self, Polynomial) and isinstance(p2, Polynomial):
            iteracja = 0

            # ktora dluzsza
            if len(p2.__k1) - len(self.__k1) >= 0:
                # to p2.__k1 jest dluzsze
                while iteracja < (min(len(self.__k1), len(p2.__k1))):
                    self.__k1[iteracja] = self.__k1[iteracja] + p2.__k1[iteracja]
                    iteracja += 1

                ogon = p2.__k1[iteracja:max(len(self.__k1), len(p2.__k1))]

                self.__k1 = self.__k1 + ogon

                return self

            else:
                # self.__k1 jest dluzszy
                while iteracja < (min(len(self.__k1), len(p2.__k1))):
                    self.__k1[iteracja] = self.__k1[iteracja] + p2.__k1[iteracja]
                    iteracja += 1

                return self

        # Zeby dzialalo z liczbami
        elif isinstance(self, Polynomial) ^ isinstance(p2, Polynomial):
            self.__k1[0] += p2
            return self

    def __mul__(self, p2):

        if isinstance(self, Polynomial) and isinstance(p2, Polynomial):
            if len(self.__k1) - len(p2.__k1) >= 0:
                # self jest dluzszy
                dluzszy, krotszy = self.__k1, p2.__k1
                koszyk = []
            else:
                dluzszy, krotszy = p2.__k1, self.__k1
                koszyk = []

            for i in range(len(krotszy)):
                g = i * [0]
                koszyk.append(g)

            # Doklejamy zera na poczatku list
            for i in range(len(krotszy)):
                for j in range(len(dluzszy)):
                    koszyk[i].append(dluzszy[j] * krotszy[i])

            # Wyrownujemy listy
            # Doklejamy zera na koncu list, zeby listy mialy rowna dlugosc
            najwieksza = len(koszyk[-1])
            for lista in koszyk:
                roznica_dlugosci = najwieksza - len(lista)
                if roznica_dlugosci > 0:
                    lista = [lista.append(k) for k in (roznica_dlugosci * [0])]

            wynik = len(koszyk[-1]) * [0]

            for il_list in range(len(koszyk)):
                for k in range(len(koszyk[-1])):
                    wynik[k] += koszyk[il_list][k]

            return Polynomial(wynik[::-1])

        # Zeby dzialalo z liczbami
        elif isinstance(self, Polynomial) ^ isinstance(p2, Polynomial):
            liczba, wielomian = p2, self
            p3 = []
            [p3.append(i) for i in wielomian.__k1]  # gleboka kopia
            for i in range(len(p3)):
                p3[i] *= liczba

            return Polynomial(p3[::-1])

    def __imul__(self, p2):
        # to jest operacja *=
        if isinstance(self, Polynomial) and isinstance(p2, Polynomial):
            if len(self.__k1) - len(p2.__k1) >= 0:
                # self jest dluzszy
                dluzszy, krotszy = self.__k1, p2.__k1
                koszyk = []
            else:
                dluzszy, krotszy = p2.__k1, self.__k1
                koszyk = []

            for i in range(len(krotszy)):
                g = i * [0]
                koszyk.append(g)

            # Doklejamy zera na poczatku list
            for i in range(len(krotszy)):
                for j in range(len(dluzszy)):
                    koszyk[i].append(dluzszy[j] * krotszy[i])

            # Wyrownujemy listy
            # Doklejamy zera na koncu list, zeby listy mialy rowna dlugosc
            najwieksza = len(koszyk[-1]) #najdluzsza
            for lista in koszyk:
                roznica_dlugosci = najwieksza - len(lista)
                if roznica_dlugosci > 0:
                    lista = [lista.append(k) for k in (roznica_dlugosci * [0])]

            wynik = len(koszyk[-1]) * [0]

            for il_list in range(len(koszyk)):
                for k in range(len(koszyk[-1])):
                    wynik[k] += koszyk[il_list][k]

            self.__k1 = wynik

            return self

        # Zeby dzialalo z liczbami
        elif isinstance(self, Polynomial) ^ isinstance(p2, Polynomial):
            liczba, wielomian = p2, self
            for i in range(len(wielomian.__k1)):
                wielomian.__k1[i] *= liczba

            return self

    def __sub__(self, p2):

        p3 = []
        if isinstance(self, Polynomial) and isinstance(p2, Polynomial):
            iteracja = 0
            while iteracja < (min(len(self.__k1), len(p2.__k1))):
                p3.append(self.__k1[iteracja] - p2.__k1[iteracja])
                iteracja += 1

            # Ktora dluzsza
            if len(p2.__k1) - len(self.__k1) >= 0:
                # to p2 jest dluzsze
                ogon = p2.__k1[iteracja: max(len(self.__k1), len(p2.__k1)) ]
                ogon = [0-ogon[i] for i in range(len(ogon))]

            # p1 dluzsze
            else:
                ogon = self.__k1[iteracja:max(len(self.__k1), len(p2.__k1))]

            p3 = p3 + ogon
            return Polynomial(p3[::-1])

        # Zeby dzialalo z liczbami
        elif isinstance(self, Polynomial) ^ isinstance(p2, Polynomial):
            liczba, wielomian = p2, self
            [p3.append(i) for i in wielomian.__k1]
            p3[0] -= liczba
            return Polynomial(p3[::-1])

    def __isub__(self, p2):
        # to ma być " -= "

        if isinstance(self, Polynomial) and isinstance(p2, Polynomial):
            iteracja = 0
            p3 = []

            while iteracja < (min(len(self.__k1), len(p2.__k1))):
                p3.append(self.__k1[iteracja] - p2.__k1[iteracja])
                iteracja += 1

            # Ktora dluzsza
            if len(p2.__k1) - len(self.__k1) >= 0:
                # to p2 jest dluzsze
                ogon = p2.__k1[iteracja: max(len(self.__k1), len(p2.__k1)) ]
                ogon = [0-ogon[i] for i in range(len(ogon))]

            else:
                # p1 dluzsze
                ogon = self.__k1[iteracja:max(len(self.__k1), len(p2.__k1))]

            p3 = p3 + ogon
            self.__k1 = p3

            return self

        # Zeby dzialalo z liczbami
        elif isinstance(self, Polynomial) ^ isinstance(p2, Polynomial):
            self.__k1[0] -= p2
            return self

    def __str__(self):
        wynik = []

        for nr_wyraz in range(len(self.__k1)):

            wyraz = self.__k1[nr_wyraz]
            if wyraz < 0:
                znak = "-"
            elif wyraz == 0:
                znak = ""
                potega = ""
            else:
                znak = "+"

            # Potegi
            if nr_wyraz == 0:
                potega = ""
            elif nr_wyraz == 1:
                potega = "x "
            else:
                potega = f"x^{nr_wyraz} "

            # Wartosci
            wartosc = abs(self.__k1[nr_wyraz])

            if wartosc == 1 and potega != "":
                wartosc = ""
            elif wartosc == 0:
                potega = ""

            # Zeby nie pisalo plusa na poczatku
            if nr_wyraz == len(self.__k1)-1 and znak == "+":
                znak = ""
                wynik.append(f"{wartosc}{potega}")

            # W ogolnym przypadku
            if not znak == "":
                wynik.append(f"{znak} {wartosc}{potega}")

            nowa = list(range(len(wynik)))

            for j in range(len(wynik)):
                nowa[j] = wynik[-j-1]
            ######print(nowa)
            zapis_wielomianu = ""
            for elt in range(len(nowa)):
                if nowa[elt] == " 0 ":
                    continue
                else:
                    zapis_wielomianu += nowa[elt]

        return zapis_wielomianu


if __name__ == "__main__":
    jeden = Polynomial([1, 2, 3])
    dwa = Polynomial([5, 6])
    wywalajacy = Polynomial([5, 3, 2, 1])

    #print(jeden)
    #jeden.coefficients.append(7)
    #jeden += dwa
    #print(jeden)
    print("Witaj, klasa gotowa :D")
    print("Mozna operowac")

# Ma dodawac tez liczby
# Juz operuje rowniez na liczbach
# Prawie potrafi mnozyc Polynomial * String - ale to niezamierzona funkcjonalnosc

# wyslac na dgront@chem.uw.edu.pl
