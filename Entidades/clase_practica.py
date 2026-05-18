# Importamos el error creado en el archivo de excepciones
from Entidades.excepciones import PermisoIncompatibleError

class ClasePractica:
    def __init__(self, fecha, alumno, profesor, vehiculo):
        self.__fecha = fecha
        self.__alumno = alumno
        self.__profesor = profesor
        self.__vehiculo = vehiculo
        self.__precio = 30.0

    @property
    def fecha(self):
        return self.__fecha

    @property
    def alumno(self):
        return self.__alumno

    def __str__(self):
        return f"Clase el {self.__fecha}: {self.__alumno._nombre} con el vehículo de matrícula {self.__vehiculo.matricula} y el profesor {self.__profesor._nombre}."

    # Manejo errores de compatiblidad requisito alumno y vehiculo elegido
    def validar_compatibilidad(self):
        if self.__vehiculo.permiso_necesario() != self.__alumno.carnet_objetivo:
            raise PermisoIncompatibleError(
                f"El alumno busca el carnet {self.__alumno.carnet_objetivo} "
                f"pero el vehículo requiere permiso {self.__vehiculo.permiso_necesario()}."
            )
        print("El vehículo es correcto para el alumno.")