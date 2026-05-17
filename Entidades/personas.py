from abc import ABC, abstractmethod

# Clase base
class Persona(ABC):
    _dni: str
    _nombre: str
    _apellido: str
    telefono: str

    def __init__(self, dni: str, nombre: str, apellido: str, telefono: str) -> None:
        # Atributos protegidos
        self._dni = dni
        self._nombre = nombre
        self._apellido = apellido
        self.telefono = telefono

    # Propiedad para acceder al DNI de forma segura (solo lectura), para no modificarlo fácilmente
    @property
    def dni(self) -> str:
        return self._dni

    # Creación metodo obligatorio que todas sus clases hijas heredarán
    @abstractmethod
    def mostrar_responsabilidad(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{self._nombre} {self._apellido} (DNI: {self._dni})"

# Clase alumno hereda de persona
class Alumno(Persona):
    carnet_objetivo: str
    clases_restantes: int

    def __init__(self, dni: str, nombre: str, apellido: str, telefono: str, carnet_objetivo: str) -> None:
        super().__init__(dni, nombre, apellido, telefono)
        self.carnet_objetivo = carnet_objetivo
        self.clases_restantes = 0

    def mostrar_responsabilidad(self) -> str:
        return f"Alumno preparándose para el carnet {self.carnet_objetivo}"

    def __str__(self) -> str:
        return f"[Alumno] {super().__str__()} - Objetivo: {self.carnet_objetivo}"

# Clase profesor hereda de persona
class Profesor(Persona):
    especialidad: str

    def __init__(self, dni: str, nombre: str, apellido: str, telefono: str, especialidad: str) -> None:
        super().__init__(dni, nombre, apellido, telefono)
        self.especialidad = especialidad

    def mostrar_responsabilidad(self) -> str:
        return f"Profesor instructor de {self.especialidad}"

    def __str__(self) -> str:
        return f"[Profesor] {super().__str__()} - Especialidad: {self.especialidad}"