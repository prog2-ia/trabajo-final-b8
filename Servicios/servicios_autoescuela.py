def generar_informe_alumnos(autoescuela, ruta_archivo="informe_alumnos.txt"):
    try:
        f = open(ruta_archivo, "w", encoding="utf-8")

        f.write("=========================================\n")
        f.write(f"  LISTADO DE ALUMNOS - {autoescuela.nombre}\n")
        f.write("=========================================\n\n")

        if len(autoescuela._lista_alumnos) == 0:
            f.write("No hay alumnos matriculados.\n")
        else:
            # Recorremos la lista usando el DNI que es seguro
            for alumno in autoescuela._lista_alumnos:
                f.write(f"- Alumno DNI: {alumno.dni} | Objetivo: {alumno.carnet_objetivo}\n")
                f.write("-----------------------------------------\n")

        f.close()
        print("Informe .txt creado correctamente en la raíz del proyecto.")

    except Exception as e:
        print(f"Error al intentar escribir en el archivo de texto: {e}")