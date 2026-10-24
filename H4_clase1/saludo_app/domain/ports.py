from abc import ABC, abstractmethod

class SaludarInputPort(ABC):
    @abstractmethod
    def ejecutar(self, nombre: str) -> str:
        pass