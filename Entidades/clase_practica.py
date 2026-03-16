# ClasePractica relaciona a un alumno, con un profesor y con su vehiculo,
class ClasePractica:
    def __init__(self, fecha, alumno, profesor, vehiculo):
        # La __ indica que son atributos protegidos, para que no se modifiquen por error fácilmente
        self.__fecha = fecha
        self.__alumno = alumno
        self.__profesor = profesor
        self.__vehiculo = vehiculo
        self.__precio = 30.0

    # Propiedad para consultar la fecha de la clase
    @property
    def fecha(self):
        return self.__fecha

    # Propiedad para acceder a los datos del alumno asignado
    @property
    def alumno(self):
        return self.__alumno

    # Metodo especial str para imprimir la información de la clase de forma legible
    def __str__(self):
        return f"Clase el {self.__fecha}: {self.__alumno.nombre} con el vehículo de matrícula {self.__vehiculo.matricula} y el profesor {self.__profesor.nombre}."

    # Metodo para validar si el vehiculo es apto para el carnet que busca el alumno
    def validar_compatibilidad(self):
        if self.__vehiculo.permiso_necesario() == self.__alumno.carnet_objetivo:
            return "El vehículo es correcto para el alumno."
        else:
            return "Aviso: El vehículo no coincide con el carnet objetivo del alumno."