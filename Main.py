import sqlite3

def agregarAlumno():

    agregar='Y'
    while (agregar=='Y'):
        nom=input("Por favor digita un nombre a agregar: ")
        ape=input("Por favor digita el apellido a agregar: ")
        agregar=(input('Si desea agregar un nuevo alumno,'
                       'por favor presione Y, de lo contrario presione'
                       'cualquier tecla ')).upper()
        query= f"insert into alumnos(nombre, apellido) values('{nom}','{ape}')"
        rows= cursor.execute(query)


def buscarTodo():
    query=f"select * from Alumnos"
    rows=cursor.execute(query)
    for row in rows:
        print(row)

def mostrarAlumno(nom):
    query=f"select * from Alumnos where nombre='{nom}'"
    rows=cursor.execute(query)
    for row in rows:
        print(row)

def seleccionaOpcion(opcion):
    if opcion==1:
        agregarAlumno()
        conn.commit()
    elif opcion==2:
        buscarTodo()

    elif opcion==3:
        alumno=input("Escribe el nombre del alumnno que deseas buscar: ")
        mostrarAlumno(alumno)
    else:
        return "No has seleccionado una opción correcta"
conn=sqlite3.connect('Alumnos.db')
cursor=conn.cursor()
seleccion=int(input("Por favor ingresa la opcion de la acción que deseas realizar"
                 "con los numeros del 1 al 3"))

seleccionaOpcion(seleccion)
cursor.close()
conn.close()

