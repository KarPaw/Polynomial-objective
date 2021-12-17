from abc import ABC, abstractmethod


class Energy(ABC):

    @abstractmethod
    def energy(self):
        pass
