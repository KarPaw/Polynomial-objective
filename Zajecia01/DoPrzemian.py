
def zrob_cos():

    def mnozenieee(pierwszy = [1,2,3,4,5,6,7], drugi = [7, 0, 9]):

        if len(pierwszy) - len(drugi) >= 0:
            # dluzszy jest dluzszy
            dluzszy, krotszy = pierwszy, drugi
            koszyk = []
        else:
            dluzszy, krotszy = drugi, pierwszy
            koszyk = []

        for i in range(len(krotszy)):
            g = i * [0]
            koszyk.append(g)

        print(koszyk)

        # Doklejamy zera na poczatku list
        for i in range(len(krotszy)):
            for j in range(len(dluzszy)):
                koszyk[i].append(dluzszy[j] * krotszy[i])

        print(koszyk)

        # Wyrownujemy listy
        # Doklejamy zera na koncu list, zeby listy mialy rowna dlugosc

        najwieksza = len(koszyk[-1]) #najdluzsza
        for lista in koszyk:
            roznica_dlugosci = najwieksza - len(lista)
            if roznica_dlugosci > 0:
                lista = [lista.append(k) for k in (roznica_dlugosci * [0])]

        print(koszyk)

        wynik = len(koszyk[-1]) * [0]

        for il_list in range(len(koszyk)):
            for k in range(len(koszyk[-1])):
                wynik[k] += koszyk[il_list][k]

        print(wynik)


    print(mnozenieee())

zrob_cos()
