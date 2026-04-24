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
        