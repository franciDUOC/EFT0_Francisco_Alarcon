import os
os.system("cls")

def mostrar_menu():
    print("""
==== MENU PRINCIPAL ====

1. Stock por categoria
2. Buscar productos por rango de precio
3. Actualizar precio
4. Agregar producto
5. Eliminar Producto
6. Mostrar productos
7. Salir
        """)

def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una de las opciones\n> "))
            if opcion not in range(1,8):
                print("Opcion seleccionada no se encuentra en el menu...")
            else:
                return opcion
        except ValueError:
            print("Opcion seleccionada debe ser un numero entero")

#Validaciones diccionario de productos
def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_categoria(categoria):
    return categoria.strip() != ""

def validar_precio(precio):
    return precio > 0

def validar_disponible(disponible):
    return disponible.lower() in ('s','n')

#Validaciones diccionario de inventario

def validar_stock(stock):
    return stock >= 0

def validar_vendidos(vendidos):
    return vendidos >= 0

