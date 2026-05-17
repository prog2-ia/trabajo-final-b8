import pickle
import os

# Nombre del archivo binario donde se guardara ttodo el estado de la autoescuela
ARCHIVO_DATOS = "autoescuela_datos.bin"

def guardar_datos(autoescuela) -> None:
    """Guarda el objeto completo Autoescuela en un archivo binario."""
    try:
        with open(ARCHIVO_DATOS, "wb") as f:
            pickle.dump(autoescuela, f)
        print("Datos guardados correctamente en el archivo binario.")
    except Exception as e:
        print(f"Error crítico al guardar los datos en binario: {e}")

def cargar_datos(clase_autoescuela) -> object:
    """
    Carga el objeto Autoescuela desde el archivo binario.
    Si el archivo no existe o está corrupto, gestiona la excepción de forma segura.
    """
    # Excepción controlada: Si el archivo no existe en el disco duro
    if not os.path.exists(ARCHIVO_DATOS):
        print("No se encontró un archivo de datos previo. Inicializando sistema nuevo...")
        # Devolvemos una instancia limpia de la clase Autoescuela
        return clase_autoescuela("Autoescuela San Vicente")

    try:
        with open(ARCHIVO_DATOS, "rb") as f:
            datos = pickle.load(f)
            print("Datos cargados correctamente desde el archivo binario.")
            return datos
    except (pickle.PickleError, EOFError, AttributeError) as e:
        # Excepción controlada: Si el archivo se cortó a la mitad o está dañado
        print(f"Error: El archivo binario está corrupto ({e}). Creando sistema vacío de seguridad...")
        return clase_autoescuela("Autoescuela San Vicente")