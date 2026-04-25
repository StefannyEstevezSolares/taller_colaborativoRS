from json import dumps, load

archivo_productos = "productos.json"


def leer_json(archivito):
    respuesta = {}
    with open(archivito, "r")as archivo:
        respuesta = load(archivo)
        return respuesta
    
def escribir_json(archivito, contenido):
    with open(archivito, "w")as archivo:
        guardar = dumps(contenido, indent=4)
        archivo.write(guardar)


def valor_total_inventario():
    productos = leer_json(archivo_productos)

    total = sum(datos["Precio"] * datos["Cantidad"] for datos in productos.values())

    print(f"El valor total del inventario es: Q {total:,.2f}")