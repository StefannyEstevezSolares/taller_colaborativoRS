from json import dumps, load, JSONDecodeError

archivo_productos = "productos.json"


def leer_json(archivito):
    respuesta = {}
    try:
        with open(archivito, "r")as archivo:
            respuesta = load(archivo)
            return respuesta
    except FileNotFoundError:
        print("Archivo no encontrado, se creará uno nuevo al guardar el primer producto.")
        return respuesta
    except JSONDecodeError:
        print("Archivo vacío o con formato incorrecto, se creará uno nuevo al guardar el primer producto.")
        return respuesta
    
def escribir_json(archivito, contenido):
    with open(archivito, "w")as archivo:
        guardar = dumps(contenido, indent=4)
        archivo.write(guardar)


def valor_total_inventario():
    productos = leer_json(archivo_productos)

    total = sum(datos["Precio"] * datos["Cantidad"] for datos in productos.values())

    print(f"El valor total del inventario es: Q {total:,.2f}")


def eliminar_producto():
    productos = leer_json(archivo_productos)
    eliminar_producto = input("Ingrese el nombre del producto: ").strip().title()

    if eliminar_producto not in productos: 
        print("Producto no existe")
        return
    
    else: 
        print(productos[eliminar_producto])

    while True:
            opc = int (input("""Desea eliminar el producto del inventario
                             
                             1. Si
                             2. Volver
    
Ingrese un número válido: """))
            

            if opc == 1:
                del productos[eliminar_producto]
                escribir_json(archivo_productos, productos)
                print("Producto eliminado correctamente")
                break
            
            elif opc == 2:
                break
            
            else:
                print("Opción no válida, intente de nuevo")


def agregar_producto():
    
    while True:

        datos = leer_json(archivo_productos)
        nombre_producto = input("Ingrese el nombre del producto: ").strip().title()

        if nombre_producto == "":
            print("Ingrese un nombre de producto válido")
            continue

        if nombre_producto in datos:
            print("El producto ya existe en el inventario")
            continue
        
        while True:
            try:
                precio = int(input("Ingrese el precio por unidad del producto: "))
                cantidad = int(input("Ingrese la cantidad de productos en stock: "))
                break
            except:
                print("Ingrese una cantidad valida")
                continue
                

        datos [nombre_producto] = {

            "Precio" : precio,
            "Cantidad": cantidad,
        }

        escribir_json(archivo_productos, datos)
        break

def actualizar_cantidad():
    productos = leer_json(archivo_productos)

    if not productos:
        print("No hay productos en el inventario para actualizar.")
        return
    
    agregar_producto = input("Ingrese el nombre del producto: ").strip().title()

    if agregar_producto not in productos: 
        print("Producto no existe")
        return
    
    else: 
        print(productos[agregar_producto])

    while True:
        try:
            opc = int (input("""Desea agregar una cantidad al inventario
                             
                             1. Si
                             2. Volver
    
Ingrese un número válido: """))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
            

        if opc == 1:
            agregar = int(input("Ingrese la cantidad de unidades: "))

            if agregar < 0:
                print("Ingrese una cantidad válida")
                break

            productos[agregar_producto]["Cantidad"] = agregar
            escribir_json(archivo_productos, productos)
            print("Cantidad agregada correctamente")
            break
        elif opc == 2:
            break

        else:
            print("Opción no válida, intente de nuevo")


def consultar_productos():

    datos = leer_json(archivo_productos)

    opc = 0
    while True:
        try:
          opc = int(input(""" Presione "1" para consultar productos o "2" para volver:"""))
        except ValueError:
            print("Por favor, ingrese un número válido.")

        if opc == 1:
            nombre = input("Ingrese el nombre del producto").strip().title()
            for clave, valores in datos.items():
                if nombre == clave:
                    print(f" Datos del producto: {nombre} - {valores}")

        elif opc == 2: 
            break