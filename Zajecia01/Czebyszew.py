from Polynomial import Polynomial

def czebyszew(n):
    n += 1
    kolejne_t = [Polynomial(1), Polynomial(1, 0)]

    for i in range(1, n):
        nowy = Polynomial(2, 0)*kolejne_t[i] - kolejne_t[i-1]
        kolejne_t.append(nowy)

    return kolejne_t[n-1]

print(czebyszew(11))


