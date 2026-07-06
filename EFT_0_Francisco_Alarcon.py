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
    disponible = disponible.strip().lower()
    if disponible == 's':
        return True
    elif disponible == 'n':
        return False
    else:
        return -1

#Validaciones diccionario de inventario

def validar_stock(stock):
    return stock >= 0

def validar_vendidos(vendidos):
    return vendidos >= 0

def stock_categoria(categoria, productos, inventario):
    total = 0
    for codigo in productos:
        if productos[codigo][1].lower() == categoria.lower():
            total += inventario[codigo][0]
    else:
        if total == 0:
            print("No hay stock")
        else:
            print(f"Stock disponible de {categoria.lower().capitalize()} = {total}")

def buscar_precio(precio_min, productos, inventario):
    pass

def buscar_codigo(codigo, productos):
    #retorna True/False
    pass

def actualizar_precio(codigo, nuevo_precio, productos):
    #retorna True/False
    pass

def agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario):
    #retorna True si fue agregado, False si el codigo existe
    pass

def eliminar_producto(codigo, productos, invetario):
    #retorna True/false
    pass

def mostrar_productos(productos, inventario):
    #print
    pass

def main():
    #Productos codigo Key, contiene Nombre, Categoria, Precio y Disponibilidad
    productos = {
        "P101": ["Cuaderno", "Papeleria", 2490, True],
        "P102": ["Lapiz", "Papeleria", 590, False ],
        "P103": ["Vodka", "Alcohol", 5000, True]
    }
    #Inventario codigo key, lista 0 stock y 1 vendidos
    inventario = {
        "P101": [8,15],
        "P102": [4,50],
        "P103": [1,40]
    }
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        if opcion == 1:
            categoria = input("Ingrese la categoria que desea verificar\n> ")
            if not validar_categoria(categoria):
                print("La categoria no puede quedar vacia")
            else:
                stock_categoria(categoria, productos, inventario)

#Inicio programa
main()
