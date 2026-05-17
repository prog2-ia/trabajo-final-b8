# Rsta clasegestiona todas las demas entidades del sistema
class Autoescuela:
    def __init__(self, nombre):
        self._nombre = nombre
        # Listas para almacenar los objetos
        self._lista_alumnos = []
        self._lista_profesores = []
        self._lista_vehiculos = []
        self._lista_clases = []

    # Propiedad para leer el nombre de la autoescuela
    @property
    def nombre(self):
        return self._nombre

    # Metodo para añadir alumnos
    def añadir_alumno(self, alumno):
        self._lista_alumnos.append(alumno)
        print(f"Alumno {alumno.dni} registrado correctamente.")

    # Metodo para añadir vehiculos
    def añadir_vehiculo(self, vehiculo):
        self._lista_vehiculos.append(vehiculo)
        print(f"Vehiculo con matricula {vehiculo.matricula} añadido al sistema.")

    # Metodo especial para ver un resumen rapido de la empresa
    def __str__(self):
        return f"Autoescuela: {self._nombre} | Alumnos: {len(self._lista_alumnos)} | Vehiculos: {len(self._lista_vehiculos)}"

    # Metodo especial para sobrecargar el operador + y asi permitir añadir elementos directamente en cualquier entidad
    def __add__(self, otro):
        # Comprobamos el nombre de la clase por el tipo para evitar problemas de importación circular
        tipo_objeto = type(otro).__name__

        if tipo_objeto == "Alumno":
            self._lista_alumnos.append(otro)
            print(f"Alumno {otro.dni} registrado mediante operador +.")
        elif tipo_objeto == "Profesor":
            self._lista_profesores.append(otro)
            print(f"Profesor {otro.dni} registrado mediante operador +.")
        elif tipo_objeto in ["Vehiculo", "Coche", "Moto"]:  # Añade aquí las subclases de vehiculo que tengas
            self._lista_vehiculos.append(otro)
            print(f"Vehículo registrado mediante operador +.")
        else:
            print("Tipo de objeto no soportado para la suma.")
        return self