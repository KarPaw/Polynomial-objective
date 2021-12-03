# tworzymy liste wyciagajac ze slownika potrzebne rzeczy
# w celu wylowienia parametrow potrzebnych do stworzenia
# obiektu Atom(...)

#
# slownik = {'id': ['id0', 'id1', 'id2', 'id3', 'id4', 'id7', 'id8', 'id10', 'id12', 'id15', 'id16'],
#            'x': ['x0', 'x1', 'x2', 'x3', 'x4', 'x7', 'x8', 'x10', 'x12', 'x15', 'x16'],
#            'y': ['y0', 'y1', 'y2', 'y3', 'y4', 'y7', 'y8', 'y10', 'y12', 'y15', 'y16'],
#            'r': ['r0', 'r1', 'r2', 'r3', 'r4', 'r7', 'r8', 'r10', 'r12', 'r15', 'r16'],
#            'm': ['m0', 'm1', 'm2', 'm3', 'm4', 'm7', 'm8', 'm10', 'm12', 'm15', 'm16']}

def slownik_atomow(plik):

    slownik = {"id": [],
               "x": [],
               "y": [],
               "r": [],
               "m": []}

    with open(plik) as f:
        i = 0
        for line in f:
            # slownik["id"][i] = None
            if not (line[0]) == "#":
                lista_wyrazow_w_linii = line.split()

                if len(lista_wyrazow_w_linii) != 5:
                    continue

                slownik["id"][i] = (lista_wyrazow_w_linii[0]) # tutaj sobie psuje....
                slownik["x"].append(lista_wyrazow_w_linii[1])
                slownik["y"].append(lista_wyrazow_w_linii[2])
                slownik["r"].append(lista_wyrazow_w_linii[3])
                slownik["m"].append(lista_wyrazow_w_linii[4])

                i += 1
        del i
    return slownik

print(
    slownik_atomow("drugi_przyklad")
)

def blabla(plik):

    with open(plik) as f:
        i = 0
        for line in f:
            if not (line[0]) == "#":
                lista_wyrazow_w_linii = line.split()

                if len(lista_wyrazow_w_linii) != 5:
                    continue
