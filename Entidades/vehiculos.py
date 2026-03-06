# Clase vehiculo
class Vehiculo:
    def __init__(self, matricula: str, modelo: str, marca: str, es_electrico: bool, es_hibrido: bool):

        self.matricula: str = matricula
        self.modelo: str = modelo
        self.marca: str = marca
        self.disponible: bool = True
        self.es_electrico: bool = es_electrico
        self.es_hibrido: bool = es_hibrido

# Clase coche, hereda de vehiculo
class Coche(Vehiculo):
    def __init__(self, matricula: str, modelo: str, marca: str, es_electrico: bool, es_hibrido: bool, cv: int):

        super().__init__(matricula, modelo, marca, es_electrico, es_hibrido)
        self.cv: int = cv

# Clase moto, hereda de vehiculo
class Moto(Vehiculo):
    def __init__(self, matricula: str, modelo: str, marca: str, es_electrico: bool, es_hibrido: bool, cilindrada: int):

        super().__init__(matricula, modelo, marca, es_electrico, es_hibrido)
        self.cilindrada: int = cilindrada










