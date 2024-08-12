

def mostrarMenu():
    print("\nAgenda de contactos:")
    print("\n1. Agregar nuevo contacto")
    print("\n2. Eliminar contacto existente")
    print("\n3. Buscar contacto")
    print("\n4. Lista de contactos")
    print("\n5. Salir del programa")
    print("\n")
    
def agregarContacto(agenda):
    nombre = input("Por favor introduce el nombre completo del contacto: ")
    telefono = input("Por favor introduce el teléfono del contacto: ")
    email = input("Por favor introduce el email del contacto: ")
    agenda[nombre] = {"telefono": telefono, "email": email}
    print(f"¡Se ha agregado el contacto {nombre} exitosamente! \n")
    
def eliminarContacto(agenda):
    nombre = input("Ingrese el nombre de la agenda que desea eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto de {nombre} se ha eliminado correctamente!")
    else:
        print(f"No se a encontrado un contacto con el nombre {nombre}!")

def buscarContacto(agenda):
    nombre = input("Ingresa el nombre del contacto a buscar: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {agenda[nombre]['telefono']}")
        print(f"Email: {agenda[nombre]['email']}")
    else:
        print(f"El contacto {nombre} no ha sido encontrado en la agenda!")
        
def listarContactos(agenda):
    if agenda:
        print("\nLista de contactos")
        for nombre, info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info['telefono']}")
            print(f"Email: {info['email']}")
            print("-" * 20)
    else:
            print("La agenda aún está vacia!")
    
def agendaContactos():
    agenda = {}
    
    while True:
        mostrarMenu()
        opcion = input("Por favor elja un opción : ")
        print("\n")
        
        if opcion == "1":
            agregarContacto(agenda)
        elif opcion == "2":
            eliminarContacto(agenda)
        elif opcion == "3":
            buscarContacto(agenda)
        elif opcion == "4":
            listarContactos(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda de contactos.")
            break
        else:
            print("Por favor seleccione una opción válida (del 1 al 5)!")
            
agendaContactos()
        