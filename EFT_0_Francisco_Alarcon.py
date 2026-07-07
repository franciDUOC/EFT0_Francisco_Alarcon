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
            print("ERROR! Debe ingresar un numero entero.")

#Validaciones

def validar_texto(valor):
    return valor.strip() != ""

def leer_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("ERROR! Debe ingresar un numero entero.")

def leer_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje)
        if validar_texto:
            return texto
        else:
            print("ERROR! Dato ingresado no puede estar vacio.")

def validar_precio(precio):
    return precio >= 0

def validar_disponible(disponible):
    disponible = disponible.lower()
    return disponible == "s" or disponible == "n"

def validar_stock(stock):
    return stock >= 0

def validar_vendidos(vendidos):
    return vendidos >= 0

def validar_codigo_nuevo (codigo, productos, inventario):
    codigo = codigo.lower()
    return codigo != "" and codigo not in productos and codigo not in inventario

#---------------------------------------------------------------------------------

def stock_categoria(categoria, productos, inventario):
    pass

def buscar_precio(precio_min, precio_max, productos, inventario):
    pass

def buscar_codigo(codigo, productos, inventario):
    pass

def actualizar_precio(codigo, nuevo_precio, productos, inventario):
    pass

def agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario):
    pass

def eliminar_producto(codigo, productos, inventario):
    pass

def ejecutar_stock_categoria(productos, inventario):
    pass
def ejecutar_busqueda_precio(productos, inventario):
    pass

def ejecutar_actualizar_precio(productos, inventario):
    pass

def ejecutar_agregar_producto(productos, inventario):
    pass

def ejecutar_eliminar_producto(productos, inventario):
    pass

def mostrar_productos(productos, inventario):
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
            ejecutar_stock_categoria(productos, inventario)
        elif opcion == 2:
            ejecutar_busqueda_precio(productos, inventario)
        elif opcion == 3:
            ejecutar_actualizar_precio(productos, inventario)
        elif opcion == 4:
            ejecutar_agregar_producto(productos, inventario)
        elif opcion == 5:
            ejecutar_eliminar_producto(productos, inventario)
        elif opcion == 6:
            mostrar_productos(productos, inventario)
        else:
            print("Saliendo del programa")
            break

#Inicio programa
main()
