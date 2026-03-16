from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, matricula: str, marca: str, modelo: str):
        # Usamos _ para indicar que son atributos protegidos
        self._matricula = matricula
        self._marca = marca
        self._modelo = modelo

    # La "Propiedad" permite leer la matrícula pero no cambiarla fácilmente
    @property
    def matricula(self):
        return self._matricula

    @abstractmethod
    def permiso_necesario(self): # De esta manera, nos aseguramos que sus hijas no puedan ser creadas sin un permiso
        pass

class Coche(Vehiculo):
    def __init__(self, matricula: str, marca: str, modelo: str, es_automatico: bool):
        # Aprovechamos el constructor de la madre
        super().__init__(matricula, marca, modelo)
        self.es_automatico = es_automatico

    def permiso_necesario(self):
        return "B"

class Moto(Vehiculo):
    def __init__(self, matricula: str, marca: str, modelo: str, cilindrada: int):
        super().__init__(matricula, marca, modelo)
        self.cilindrada = cilindrada

    def permiso_necesario(self):
        return "A2"