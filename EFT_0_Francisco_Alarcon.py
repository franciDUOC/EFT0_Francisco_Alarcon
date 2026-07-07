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
#Funcion devuelve bool
    return valor.strip() != ""

def leer_entero(mensaje):
#Funcion devuelve el numero
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("ERROR! Debe ingresar un numero entero.")

def leer_texto_no_vacio(mensaje):
#Funcion devuelve str
    while True:
        texto = input(mensaje)
        if validar_texto:
            return texto
        else:
            print("ERROR! Dato ingresado no puede estar vacio.")

def validar_precio(precio):
#Funcion devuelve bool
    return precio > 0

def validar_disponible(disponible):
#Funcion devuelve bool
    disponible = disponible.lower()
    return disponible == "s" or disponible == "n"

def validar_stock(stock):
#Funcion devuelve bool
    return stock >= 0

def validar_vendidos(vendidos):
#Funcion devuelve bool
    return vendidos >= 0

def validar_codigo_nuevo (codigo, productos, inventario):
#Funcion devuelve bool
    codigo = codigo.upper()
    return codigo != "" and codigo not in productos and codigo not in inventario

#---------------------------------------------------------------------------------

# Esqueleto de las opciones del menu

def stock_categoria(categoria, productos, inventario):
#Funcion print del stock
    total_stock = 0
    
    for codigo in productos:
        datos_producto = productos[codigo]
        producto_categoria = datos_producto[1]
        if producto_categoria.lower() == categoria.lower():
            if codigo in inventario:
                stock = inventario[codigo][0]
                total_stock += stock

    print("Stock total disponible:", total_stock)

def buscar_precio(precio_min, precio_max, productos, inventario):
#Funcion devuelve lista con productos (nombre -- codigo) en el rango precio minimo y maximo
    resultados = []
    for codigo in productos:
        precio = productos[codigo][2]
        stock = inventario[codigo][0]
        if precio >= precio_min and precio <= precio_max and stock != 0:
            nombre = productos[codigo][0]
            resultados.append(nombre + " -- " + codigo)
    resultados.sort()
    return resultados

def buscar_codigo(codigo, productos, inventario):
#Funcion devuelve bool si codigo se encuentra en productos e inventario
    codigo = codigo.upper()
    if codigo in productos and codigo in inventario:
        return True
    return False

def actualizar_precio(codigo, nuevo_precio, productos, inventario):
#Funcion devuelve bool que depende de si encuentra el codigo 
    codigo = codigo.upper()
    if buscar_codigo(codigo, productos, inventario):
        productos[codigo][2] = nuevo_precio
        return True
    return False

def agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario):
#Funcion devuelve bool que depende de si encuentra el codigo
    codigo = codigo.upper()
    nombre = nombre.capitalize()
    categoria = categoria.capitalize()
    
    if not validar_codigo_nuevo(codigo, productos, inventario):
        return False
    
    if disponible == "s":
        disponible_bool = True
    else:
        disponible_bool = False
    
    productos[codigo] = [nombre,categoria,precio,disponible_bool]
    inventario[codigo] = [stock,vendidos]
    return True

def eliminar_producto(codigo, productos, inventario):
#Funcion devuelve bool que depende de si encuentra el codigo 
    codigo = codigo.upper()
    
    if buscar_codigo(codigo, productos, inventario):
        del productos[codigo]
        del inventario[codigo]
        return True
    return False

#--------------------------------------------------------------------------------

#Funciones que incluyen los inputs

def ejecutar_stock_categoria(productos, inventario):
    categoria = leer_texto_no_vacio("Ingrese la categoria que desea consultar\n> ")
    stock_categoria(categoria, productos, inventario)

def ejecutar_busqueda_precio(productos, inventario):
    while True:
        precio_minimo = leer_entero("Ingrese el precio minimo\n> ")
        if precio_minimo >= 0:
            break
        else:
            print("ERROR! Debe ingresar un precio mayor o igual que 0.")

    while True:
        precio_maximo = leer_entero("Ingrese el precio maximo\n> ")
        if precio_maximo >= 0:
            break
    
    if precio_maximo < precio_minimo:
        print("ERROR! El precio maximo debe ser mayor que el precio minimo.")
        return
    resultados = buscar_precio(precio_minimo, precio_maximo, productos, inventario)
    if len(resultados) > 0:
        print("Lista de productos\n")
        for codigo in resultados:
            print(codigo)
    else:
        print("No existen productos en ese rango de precios.")

def ejecutar_actualizar_precio(productos, inventario):
    codigo = leer_texto_no_vacio("Ingrese el codigo del producto que desea actualizar el precio\n> ").upper().strip()

    if codigo == "" or codigo not in productos or codigo not in inventario:
        print("ERROR! Codigo no existe")
        return

    while True:
        nuevo_precio = leer_entero("Ingrese el nuevo precio de su producto\n> ")
        if validar_precio(nuevo_precio):
            break
        else:
            print("El nuevo precio debe ser mayor que 0")
    actualizado = actualizar_precio(codigo, nuevo_precio, productos, inventario)
    if actualizado:
        print("Precio actualizado")
    else:
        print("ERROR! El codigo no existe.")

def ejecutar_agregar_producto(productos, inventario):
    codigo = leer_texto_no_vacio("Ingrese el codigo del nuevo producto\n> ").upper()
    
    if not validar_codigo_nuevo(codigo, productos, inventario):
        print("ERROR! El codigo ingresado ya existe.")
        return

    nombre = leer_texto_no_vacio("Ingrese el nombre del producto\n> ").capitalize()
    categoria = leer_texto_no_vacio("Ingrese la categoria del producto\n> ").capitalize()

    while True:
        precio = leer_entero("Ingrese el precio\n> ")
        if validar_precio(precio):
            break
        else:
            print("ERROR! El precio debe ser mayor que 0.")
    
    while True:
        disponible = leer_texto_no_vacio("Seleccione la disponibilidad del producto (s o n)\n> ").strip().lower()
        if validar_disponible(disponible):
            break
        else:
            print("ERROR! Debe ingresar una opcion entre 's' o 'n'.")

    while True:
        stock = leer_entero("Ingrese el stock del producto\n> ")
        if validar_stock(stock):
            break
        else:
            print("ERROR! El stock debe ser mayor o igual que 0.")
    
    while True:
        vendidos = leer_entero("Ingrese la cantidad vendida\n> ")
        if validar_vendidos(vendidos):
            break
        else:
            print("ERROR! La cantidad debe ser mayor o igual que 0")
    agregado = agregar_producto(
        codigo,
        nombre,
        categoria,
        precio,
        disponible,
        stock,
        vendidos,
        productos,
        inventario
        )
    if agregado:
        print("Producto agregado!")
    else:
        print("ERROR! Codigo ya existe.")

def ejecutar_eliminar_producto(productos, inventario):
    codigo = leer_texto_no_vacio("Ingrese el codigo del producto a eliminar\n> ").upper()
    if eliminar_producto(codigo, productos, inventario):
        print("Producto eliminado")
    else:
        print("ERROR! El codigo no existe")

def mostrar_productos(productos, inventario):
    if len(productos) > 0 and len(inventario) > 0:
        for codigo in productos:
            print("Lista de productos")
            print(f"Codigo: {codigo}")
            print("-"*20)
            print(f"Nombre: {productos[codigo][0]}")
            print(f"Categoria: {productos[codigo][1]}")
            print(f"Precio: ${productos[codigo][2]}")
            if productos[codigo][3] == "s":
                print("Disponible: Si")
            else:
                print("Disponible: No")
            print(f"Stock: {inventario[codigo][0]}")
            print(f"Vendidos: {inventario[codigo][1]}")
            print(f"="*20)
    else:
        print("No hay productos registrados")

#-----------------------------------------------------------------------------------------

#Programa final

def main():
    #Productos codigo Key, contiene Nombre, Categoria, Precio y Disponibilidad
    productos = {
        "P101": ["Cuaderno", "Papeleria", 2490, True],
        "P102": ["Lapiz", "Papeleria", 590, True ],
        "P103": ["Botella", "Accesorios", 6990, False],
        "P104": ["Mochila", "Accesorios", 24990, True]
    }
    #Inventario codigo key, lista 0 stock y 1 vendidos
    inventario = {
        "P101": [30,15],
        "P102": [120,50],
        "P103": [0,10],
        "P104": [8,25]
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
