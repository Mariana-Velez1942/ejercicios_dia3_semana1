# Crear la biblioteca
biblioteca = { # se genero la creacion de la biblioteca  
    1: ("Divina comedia", "Dante Alighieri", 1321), # se crearon las tuplas donde va almacenada la info
    2: ("Orgullo y prejuicio", "Jane Austen", 1813),
    3: ("Cumbres borrascosas", "Emily Bronte", 1847),
    4: ("Madame Bovary", "Gustave Flaubert", 1857),
    5: ("Iliada", "Homero", 750)
}

# Mostrar todos los libros
print("Lista de libros:")
for id_libro, datos in biblioteca.items(): # se generaron dos variables donde id almacena el numero del libro, datos guarda la tupla con la info y biblioteca.items sirve para rrecorrer como para el valor del diccionario
    print(f"ID: {id_libro} - Título: {datos[0]} - Autor: {datos[1]} - Año: {datos[2]}") # se genera un bucle for y una f string para imprimir tanto el mensaje como la variable

# Buscar un libro por ID
buscar_id = int(input("¿ID del libro que quieres buscar?: ")) # se imprime el mensaje
if buscar_id in biblioteca: # con ambas variables se busca si el id del libro esta
    libro = biblioteca[buscar_id] # buscamos el id del libro
    print(f"Encontrado: {libro[0]} - {libro[1]} - {libro[2]}") # con f strin buscamos e imprimimos tanto el mensaje como la variable
else:
    print("Libro no encontrado.") # si no el libro no esta 

# Buscar un libro por Título
buscar_titulo = input("¿Título del libro que quieres buscar?: ") # se imprime la opcion de buscar el libro
encontrado = False # se usa el condicional false: investigar porque
for id_libro, datos in biblioteca.items():
    if datos[0].lower() == buscar_titulo.lower():
        print(f"Encontrado: ID {id_libro} - {datos[0]} - {datos[1]} - {datos[2]}")
        encontrado = True
        break # se usa para salir de un bucle de forma prematura
if not encontrado:
    print("Título no encontrado.")

# Actualizar un libro
actualizar_id = int(input("¿ID del libro que quieres actualizar?: "))
if actualizar_id in biblioteca:
    nuevo_autor = input("Nuevo autor: ")
    nuevo_anio = int(input("Nuevo año: "))
    titulo = biblioteca[actualizar_id][0]
    biblioteca[actualizar_id] = (titulo, nuevo_autor, nuevo_anio)
    print("Libro actualizado.")
else:
    print("ID no encontrado.")

# Eliminar un libro
eliminar_id = int(input("¿ID del libro que quieres eliminar?: "))
if eliminar_id in biblioteca:
    del biblioteca[eliminar_id] # del se utiliza para eliminar la referencia de un objeto
    print("Libro eliminado.")
else:
    print("ID no encontrado.")

# Mostrar libros actualizados
print("Lista actualizada de libros:")
for id_libro, datos in biblioteca.items():
    print(f"ID: {id_libro} - Título: {datos[0]} - Autor: {datos[1]} - Año: {datos[2]}")
