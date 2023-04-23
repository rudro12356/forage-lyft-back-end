from abc import ABC, abstractmethod

class Servicing(ABC):
    @abstractmethod
    def service(self):
        pass