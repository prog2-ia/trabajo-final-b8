""" CHEKEAR ENTERA """
# Clase 10: Es la clase maestra que gestiona todas las demas entidades del sistema
class Autoescuela:
    def __init__(self, nombre):
        self._nombre = nombre
        # Listas para almacenar los objetos y cumplir con los requisitos de listados
        self._lista_alumnos = []
        self._lista_profesores = []
        self._lista_vehiculos = []
        self._lista_clases = []

    # Propiedad para leer el nombre de la autoescuela
    @property
    def nombre(self):
        return self._nombre

    # Metodo para añadir alumnos (Relaciona la clase Autoescuela con Alumno)
    def añadir_alumno(self, alumno):
        self._lista_alumnos.append(alumno)
        print(f"Alumno {alumno.nombre} registrado correctamente.")

    # Metodo para añadir vehiculos
    def añadir_vehiculo(self, vehiculo):
        self._lista_vehiculos.append(vehiculo)
        print(f"Vehiculo con matricula {vehiculo.matricula} añadido al sistema.")

    # Metodo especial para ver un resumen rapido de la empresa
    def __str__(self):
        return f"Autoescuela: {self._nombre} | Alumnos: {len(self._lista_alumnos)} | Vehiculos: {len(self._lista_vehiculos)}"