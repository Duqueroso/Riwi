#Variables Globales
titulo_libros = []
autor = []
genero =[]
year = []
total_libros = []
costo = []

def menu():
    print("="*30)
    print("GESTION DE LIBROS")
    print("="*30)
    print("OPCIONES DISPONIBLES")
    print("="*30)
    print("1. Registrar nuevos libros")
    print("2. Buscar libros")
    print("3. Actualizar información")
    print("4. Eliminar libros obsoletos")
    print("5. Generar reportes")
    print("="*30)
    opcion = int(input("QUE DESEAS REALIZAR: "))
    match opcion:
        case 1:
            uno()
        case 2:
            dos()
        case 3:
            tres()
        case 4:
            cuatro()
        case 5:
            cinco()
        case _:
            print("OPCION NO VALIDA")
            menu()
    
def uno():
    print("="*30)
    print("REGISTRAR LIBRO")
    print("="*30)
    titulo_libros.append(input("Ingresa el titulo: "))
    autor.append(input("ingresa el autor: "))
    genero.append(input("Ingresa el genero del libro: "))
    year.append(input("Ingresa el año de publicación: "))
    total_libros.append(int(input("Ingresa la cantidad de libros: ")))
    costo.append(int(input("Costo de reposicion: ")))
    print("="*30)
    opcion = input("Quieres ingresar otro libro (S/N): ")
    opcionf = opcion.upper()
    if opcionf == "S":
        uno()
    elif opcionf == "N":
        salida = input("Quieres salir del sistema (S/N): ")
        salidaf = salida.upper()
        if salidaf == "S":
            print("Saliste del sistema, chao")
        elif salidaf == "N":
            menu()
        else:
            print("OPCION INVALIDA")
    else:
        print("OPCION INVALIDA")

menu()
