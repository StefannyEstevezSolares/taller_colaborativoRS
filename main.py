from menu_visual import menu_visual
from funciones import agregar_producto, consultar_productos, actualizar_cantidad, eliminar_productos

def main_menu():

    while True:
        menu_visual()
        try:
            opc = int(input("""Ingrese una opción de MENÚ
                            """))
        except ValueError:
            print("Opción no válida. Por favor, ingrese un número.")

        if opc == 1:
            agregar_producto()
        
        elif opc == 2:
            consultar_productos()

        elif opc == 3:
            actualizar_cantidad()

        elif opc == 4:
            eliminar_productos()

        elif opc == 5:
            calcular_inventario_total()

        elif opc == 6:
            break

main_menu()