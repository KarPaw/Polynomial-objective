import abc
# to beda energie
# Harmonic
# Repulsion
# Coulomb
# i na koniec sumuje energie


class Energy(abc):

    @abc.abstractmethod
    def energy(self):
        pass
