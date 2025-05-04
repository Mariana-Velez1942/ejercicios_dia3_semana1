#Ejercicio 2 -  Agenda de Contactos
#Contexto:
#Vas a construir una agenda que guarda información de contactos personales.


#1. crear
# Lista global para guardar los contactos

agenda = {}

def agregar_contacto():
    nombre = input("Nombre: ")
    if nombre in agenda:
        print("Ya existe un contacto con ese nombre.\n")
        return

    telefono = input("Teléfono: ")
    email = input("Email: ")

    agenda[nombre] = {
        "teléfono": telefono,
        "email": email
    }
    print("Contacto agregado exitosamente.\n")

def listar_contactos():
    if not agenda:
        print("La agenda está vacía.\n")
        return

    for nombre, datos in agenda.items():
        print(f"Nombre: {nombre}")
        print(f"  Teléfono: {datos['teléfono']}")
        print(f"  Email: {datos['email']}\n")

def buscar_contacto():
    nombre = input("Ingrese el nombre a buscar: ").strip()
    if nombre in agenda:
        datos = agenda[nombre]
        print(f"Nombre: {nombre}")
        print(f"  Teléfono: {datos['teléfono']}")
        print(f"  Email: {datos['email']}\n")
    else:
        print("Contacto no encontrado.\n")

def actualizar_contacto():
    nombre = input("Nombre del contacto a actualizar: ").strip()
    if nombre in agenda:
        telefono = input("Nuevo teléfono (dejar en blanco para no cambiar): ").strip()
        email = input("Nuevo email (dejar en blanco para no cambiar): ").strip()

        if telefono:
            agenda[nombre]['teléfono'] = telefono
        if email:
            agenda[nombre]['email'] = email

        print("Contacto actualizado.\n")
    else:
        print("Contacto no encontrado.\n")

def eliminar_contacto():
    nombre = input("Nombre del contacto a eliminar: ").strip()
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto eliminado.\n")
    else:
        print("Contacto no encontrado.\n")

# Menú
while True:
    print("AGENDA DE CONTACTOS")
    print("1. Agregar contacto")
    print("2. Listar contactos")
    print("3. Buscar contacto")
    print("4. Actualizar contacto")
    print("5. Eliminar contacto")
    print("6. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        listar_contactos()
    elif opcion == "3":
        buscar_contacto()
    elif opcion == "4":
        actualizar_contacto()
    elif opcion == "5":
        eliminar_contacto()
    elif opcion == "6":
        print("¡Hasta pronto!")
        break
    else:
        print("Opción no válida.\n")
