import sys
import os

# Añadimos la raíz del proyecto al path para que Python encuentre las carpetas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importaciones varias
from Entidades.autoescuela import Autoescuela
from Entidades.excepciones import PermisoIncompatibleError
from Entidades.personas import Alumno, Profesor
from Entidades.vehiculos import Coche, Moto
from Entidades.clase_practica import ClasePractica
from Persistencia.gestor_archivos import guardar_datos, cargar_datos
from Servicios.servicios_autoescuela import generar_informe_alumnos


def mostrar_menu():
    print("\n=========================================")
    print("      SISTEMA DE GESTIÓN AUTOESCUELA     ")
    print("=========================================")
    print("1. Alta de Alumno")
    print("2. Alta de Profesor")
    print("3. Alta de Coche")
    print("4. Alta de Moto")
    print("5. Programar Clase Práctica")
    print("6. Ver Estado General (Resumen)")
    print("7. Generar Informe de Alumnos (.txt)")
    print("8. Guardar y Salir")
    print("=========================================")


def main():
    # Cargamos el archivo
    mi_autoescuela = cargar_datos(Autoescuela)

    salir = False
    while not salir:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- ALTA DE ALUMNO ---")
            dni = input("DNI: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            telefono = input("Teléfono: ")
            carnet = input("Carnet objetivo (A2 / B): ").upper()

            nuevo_alumno = Alumno(dni, nombre, apellido, telefono, carnet)
            mi_autoescuela = mi_autoescuela + nuevo_alumno

        elif opcion == "2":
            print("\n---- ALTA DE PROFESOR ---")
            dni = input("DNI: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            telefono = input("Telefono: ")
            especialidad = input("Especialidad: ")

            nuevo_profesor = Profesor(dni, nombre, apellido, telefono, especialidad)
            mi_autoescuela = mi_autoescuela + nuevo_profesor

        elif opcion == "3":
            print("\n--- ALTA DE COCHE ---")
            matricula = input("Matrícula: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            automatico_in = input("¿Es automático? (si/no): ").lower()
            es_automatico = True if automatico_in == "si" else False

            nuevo_coche = Coche(matricula, marca, modelo, es_automatico)
            mi_autoescuela = mi_autoescuela + nuevo_coche

        elif opcion == "4":
            print("\n--- ALTA DE MOTO ---")
            matricula = input("Matrícula: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            cilindrada = input("Cilindrada (ej: 250cc): ")

            nueva_moto = Moto(matricula, marca, modelo, cilindrada)
            mi_autoescuela = mi_autoescuela + nueva_moto


        elif opcion == "5":

            print("\n--- PROGRAMAR CLASE PRÁCTICA ---")

            if not mi_autoescuela._lista_alumnos or not mi_autoescuela._lista_profesores or not mi_autoescuela._lista_vehiculos:
                print("Error: Necesitas registrar mínimo 1 Alumno, 1 Profesor y 1 Vehículo para agendar clases.")

                continue

            fecha = input("Fecha y hora de la clase (ej: 25/05 a las 10:00): ")

            print("\nAlumnos disponibles:")

            for i, al in enumerate(mi_autoescuela._lista_alumnos):
                print(f"  [{i}] {al._nombre} {al._apellido} (Objetivo: {al.carnet_objetivo})")

            idx_al = int(input("Seleccione el número del alumno: "))

            print("\nProfesores disponibles:")

            for i, pr in enumerate(mi_autoescuela._lista_profesores):
                print(f"  [{i}] {pr._nombre} {pr._apellido}")

            idx_pr = int(input("Seleccione el número del profesor: "))

            print("\nVehículos disponibles:")

            for i, ve in enumerate(mi_autoescuela._lista_vehiculos):
                print(
                    f"  [{i}] {ve._marca} {ve._modelo} [Matrícula: {ve.matricula}] (Permiso: {ve.permiso_necesario()})")

            idx_ve = int(input("Seleccione el número del vehículo: "))

            alumno_sel = mi_autoescuela._lista_alumnos[idx_al]

            profesor_sel = mi_autoescuela._lista_profesores[idx_pr]

            vehiculo_sel = mi_autoescuela._lista_vehiculos[idx_ve]

            # Captura de excepcion propia

            try:

                nueva_clase = ClasePractica(fecha, alumno_sel, profesor_sel, vehiculo_sel)

                # Si esto falla, saltará directamente al except sin añadir la clase

                nueva_clase.validar_compatibilidad()

                mi_autoescuela._lista_clases.append(nueva_clase)

                print("Clase agendada correctamente.")


            except PermisoIncompatibleError as e:

                print(f"\n[ERROR DE VALIDACIÓN] No se pudo agendar: {e}")


        elif opcion == "6":

            print("\n--- ESTADO GENERAL DE LA EMPRESA ---")

            print(mi_autoescuela)

            print(f"\nProfesores totales ({len(mi_autoescuela._lista_profesores)}):")

            for pr in mi_autoescuela._lista_profesores:
                print(f"  - DNI: {pr.dni} | Especialidad: {getattr(pr, 'especialidad', 'No asignada')}")

            print(f"\nVehículos totales ({len(mi_autoescuela._lista_vehiculos)}):")

            for ve in mi_autoescuela._lista_vehiculos:
                print(f"  - {ve._marca} {ve._modelo} ({ve.matricula})")

            print(f"\nClases agendadas ({len(mi_autoescuela._lista_clases)}):")

            for cl in mi_autoescuela._lista_clases:

                try:

                    # Usamos fecha y alumno de la ClasePractica

                    print(f"  - Clase el {cl.fecha} | Alumno DNI: {cl.alumno.dni}")

                except Exception:

                    print("  - [Error al leer datos de una clase práctica]")

        elif opcion == "7":
            # Esto genera el archivo informe_alumnos.txt en la raíz
            generar_informe_alumnos(mi_autoescuela)

        elif opcion == "8":
            # Guardado y salida del programa
            print("\nGuardando datos en 'autoescuela_datos.bin'...")
            guardar_datos(mi_autoescuela)
            print("¡Cierre completado con éxito!")
            salir = True
        else:
            print("Opción no válida. Inténtelo de nuevo.")


if __name__ == "__main__":
    main()