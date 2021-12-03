from Energy import Energy

class Total_Energy(Energy):

    def add_energy(e: Energy):
        pass


    # Rozne argumenty, i ich ilosc bedzie ogarnieta przez maker / konstruktor
    # podane na zajeciach
    def energy(self):
        total = 0
        for en_i in self.ene_list:
            total += en_i._energy()
