from abc import ABC,abstractmethod

class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        
    def __str__(self):
        return f"{self._marca} {self._modelo}"

    @abstractmethod
    def ligar(self):
        pass
