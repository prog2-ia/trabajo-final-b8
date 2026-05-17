[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/09uckVan)
# Trabajo Final Programación II - Gestión de Autoescuela

Proyecto para la asignatura de Programación II del Grado en Inteligencia Artificial (Universidad de Alicante).

Hecho por: Alejandro Cerdá Fuentes.

---

## ¿De qué va el proyecto?
Es una aplicación por consola para gestionar el día a día de una autoescuela. Permite dar de alta alumnos, profesores, coches y motos, además de organizar las clases prácticas cruzando los datos de todos ellos. 

Hemos organizado el código separando las cosas por carpetas (Entidades, Persistencia, Servicios y la UI) para que quede todo limpio y bien estructurado.

---

## Requisitos de la práctica implementados

El sistema tiene 10 clases en total y cumple con todo lo que pide el enunciado:

* **Clases abstractas y herencia**: Usamos `Persona` como clase base abstracta para heredar en `Alumno` y `Profesor`. Lo mismo con `Vehiculo` para sacar las subclases `Coche` y `Moto`.
* **Encapsulamiento**: Usamos propiedades (`@property`) para proteger datos importantes como el DNI o la matrícula.
* **Métodos especiales**: Metidos los métodos `__str__` en las clases para pintar la información formateada por consola de forma fácil.
* **Sobrecarga de operadores**: Modificamos el operador `+` (`__add__`) en la clase `Autoescuela` para poder meter alumnos o coches a las listas sumándolos directamente.
* **Gestión de excepciones**: Controlamos los errores de lectura/escritura con bloques `try/except` y creamos la clase `AutoescuelaError` para los fallos personalizados.
* **Persistencia Binaria**: Guardamos y cargamos todo el estado de la aplicación usando archivos binarios con la librería `pickle`.
* **Archivos de texto**: El programa genera un archivo `.txt` real con el listado completo de los alumnos.

---

## Cómo ejecutarlo

Para arrancar el programa, abre la terminal en la carpeta raíz del proyecto y lanza el menú principal:

```bash
python3 UI/main.py