# Clase Persona
class Persona:
    def __init__(self, dni: str, nombre: str, apellido: str, telefono: str):
        self.dni: str = dni
        self.nombre: str = nombre
        self.apellido: str = apellido
        self.telefono: str = telefono

# Clase Alumno hereda de Persona
class Alumno(Persona):
    def __init__(self, dni: str, nombre: str, apellido: str, telefono: str, carnet_objetivo: str):
        super().__init__(dni, nombre, apellido, telefono)
        self.carnet_objetivo: str = carnet_objetivo
        self.clases_restantes: int = 0

# Clase Profesor hereda de Persona
class Profesor(Persona):
    def __init__(self, dni: str, nombre: str, apellido: str, telefono: str, especialidad: str):
        super().__init__(dni, nombre, apellido, telefono)
        self.especialidad: str = especialidad
        self.esta_de_baja: bool = False