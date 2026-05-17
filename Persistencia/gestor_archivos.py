import pickle
import os

def guardar_datos(autoescuela):
    try:
        f = open("autoescuela_datos.bin", "wb")
        pickle.dump(autoescuela, f)
        f.close()
        print("Datos guardados en el archivo binario.")
    except Exception:
        print("Error al guardar los datos.")

def cargar_datos(clase_autoescuela):
    # Si el archivo no existe, devolvemos una autoescuela nueva en blanco
    if not os.path.exists("autoescuela_datos.bin"):
        print("No hay datos guardados. Creando nueva autoescuela...")
        return clase_autoescuela("Autoescuela San Vicente")

    try:
        f = open("autoescuela_datos.bin", "rb")
        datos = pickle.load(f)
        f.close()
        print("Datos cargados correctamente.")
        return datos
    except Exception:
        print("Error al cargar el archivo. Creando autoescuela vacía por seguridad.")
        return clase_autoescuela("Autoescuela San Vicente")