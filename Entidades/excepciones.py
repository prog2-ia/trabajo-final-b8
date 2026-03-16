# En este archivo estrán agrupados todos los posbiles errores del proyecto, con el objetivo de lanzar un mensaje comprensible para los usuarios en caso de error
# Error base
class AutoescuelaError(Exception): # Al poner (Exception) indicamos a python que no es una clase normal y que debe comportarde como un error del sistema
    pass


# Error 1. Error para cuando los carnets no coinciden
class PermisoIncompatibleError(AutoescuelaError):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        # Usamos super para pasarle el texto a la clase Exception de Python
        super().__init__(self.mensaje)

    def __str__(self):
        return f"ERROR DE PERMISO: {self.mensaje}"