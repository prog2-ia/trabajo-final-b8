from abc import ABC, abstractmethod

# Clase base
class Vehiculo(ABC):
    def __init__(self, matricula, marca, modelo):
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

# Clase hija coche hereda de vehiculo
class Coche(Vehiculo):
    def __init__(self, matricula, marca, modelo, es_automatico):
        # Aprovechamos el constructor de la madre
        super().__init__(matricula, marca, modelo)
        self.es_automatico = es_automatico

    def permiso_necesario(self):
        return "B"

# Clase hija moto hereda de vehiculo
class Moto(Vehiculo):
    def __init__(self, matricula, marca, modelo, cilindrada):
        super().__init__(matricula, marca, modelo)
        self.cilindrada = cilindrada

    def permiso_necesario(self):
        return "A2"