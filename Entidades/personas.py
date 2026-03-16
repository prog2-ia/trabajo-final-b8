from abc import ABC, abstractmethod

# Clase base
class Persona(ABC):
    def __init__(self, dni, nombre, apellido, telefono):
        # Atributos protegidos
        self._dni = dni
        self._nombre = nombre
        self._apellido = apellido
        self.telefono = telefono

    # Propiedad para acceder al DNI de forma segura (solo lectura), para no modificarlo fácilmente
    @property
    def dni(self):
        return self._dni

    # Creación metodo obligatorio que todas sus clases hijas heredarán
    @abstractmethod
    def mostrar_responsabilidad(self):
        pass

# Clase alumno hereda de persona
class Alumno(Persona):
    def __init__(self, dni, nombre, apellido, telefono, carnet_objetivo):
        super().__init__(dni, nombre, apellido, telefono)
        self.carnet_objetivo = carnet_objetivo
        self.clases_restantes = 0

    def mostrar_responsabilidad(self):
        return f"Alumno preparándose para el carnet {self.carnet_objetivo}"

# Clase profesor hereda de persona
class Profesor(Persona):
    def __init__(self, dni, nombre, apellido, telefono, especialidad):
        super().__init__(dni, nombre, apellido, telefono)
        self.especialidad = especialidad

    def mostrar_responsabilidad(self):
        return f"Profesor instructor de {self.especialidad}"