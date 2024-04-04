# Importación de la función sleep
from time import sleep

# Variables globales
imprimir_menu = False
esta_abierta_tienda = False
es_primera_ejecucion = True
esta_ingresando_efectivo = True
# Arreglos de producto
codigo_productos = [1, 2, 3, 4]
nombres_productos = ["Azúcar", "Avena", "Trigo", "Maíz"]
precios_venta = [30, 25, 32, 20]
precios_compra = [25, 20, 30, 18]
# Arreglos de reportes
valor_compras = []
valor_ventas = []
# Variables para totales
total_efectivo_compras = 0
total_efectivo_ventas = 0
total_efectivo_caja = 0
precio_total = 0
# Variables para contador reportes
numero_ventas = 0
numero_compras = 0


# Función de ventas
def menu_ventas():
    # Declaro variables globales que se utilizarán.
    global imprimir_menu
    global nombres_productos
    global precios_venta
    global precio_total
    global codigo_productos
    global total_efectivo_ventas
    global numero_ventas
    global valor_ventas
    global total_efectivo_caja

    # Declara variables locales de la función.
    precio_total = 0
    imprimir_menu = False
    esta_abierto_venta = True

    # Imprime menú en pantalla.
    print("===== MENU VENTAS =====")
    print("1. Nueva venta")
    print("2. Regresar al menu principal")
    # Pedimos al usuario una opción.
    seleccion_usuario_ventas = input("Ingrese una opción: \n")

    # Bucle que verifica la opción del usuario.
    while esta_abierto_venta:
        if seleccion_usuario_ventas == "1":
            # .upper() es una función por defecto de Python que convierte un string a mayúscula.
            seleccion_tipo_cliente = input("Ingrese el tipo de cliente (B o C): \n").upper()
            seleccion_codigo_producto = int(input("Ingrese el código del producto (1 - 4): \n"))
            seleccion_cantidad = float(input("Ingrese la cantidad de kilogramos: \n"))

            # Función que valida el tipo de cliente
            if validar_venta(seleccion_tipo_cliente, seleccion_codigo_producto):
                # .index() función por defecto de Python que retorna el indice un arreglo en este caso codigo_productos.
                indice_producto = codigo_productos.index(seleccion_codigo_producto)
                # Basado en indice que nos retorna .index() igualamos el mismo indice para buscar el nombre y precio.
                nombre_producto = nombres_productos[indice_producto]
                precio_producto = precios_venta[indice_producto]

                # Calcula Subtotal y añade el subtotal a precio total.
                subtotal = precio_producto * seleccion_cantidad
                precio_total += subtotal

                # Imprime el producto, cantidad, precio unitario y subtotal.
                print(f"Producto: {nombre_producto}")
                print(f"Cantidad: {seleccion_cantidad}")
                print(f"Precio unitario: Lps.{precio_producto}")
                # .2f especifica el formato que en este caso es de 2 puntos decimales.
                print(f"Subtotal: Lps. {subtotal:.2f}")
                # Verifica si el usuario desea continuar o no, .lower() para el input a minúscula.
                ingresar_otro_producto = input("¿Quisiera agregar otro producto? (si/no): ").lower()
                if ingresar_otro_producto != "si":
                    # Detiene el bucle.
                    break
            elif not validar_venta(seleccion_tipo_cliente, seleccion_codigo_producto):
                print("ERROR: El cliente no puede comprar ese producto.")
                main()
            else:
                esta_abierto_venta = False
                print("ERROR: Ingrese una opción correcta.")
                main()

        else:
            print("ERROR: Ingrese una opción correcta.")
            main()

    # Calcula el descuento
    if precio_total >= 5000:
        descuento = 0.10
    elif precio_total >= 1000:
        descuento = 0.05
    else:
        descuento = 0

    # Calcula el total con descuento.
    total_con_descuento = precio_total * (1 - descuento)
    # Agrega el total con descuento al total de ventas.
    total_efectivo_ventas += total_con_descuento
    # Agrega el total de con descuento a caja.
    total_efectivo_caja += total_con_descuento
    # Incrementa 1 a la variable de numero de ventas para reportes.
    numero_ventas += 1
    # Añade el total de ventas al arreglo de valor_ventas para luego utilizarlo en reportes.
    valor_ventas.append(total_con_descuento)

    # Imprime el total de la compra y regresa al menu principal
    print(f"\nTotal a pagar (antes del descuento): Lps.{precio_total:.2f}")
    print(f"Descuento: {descuento * 100:.0f}%")
    print(f"Total a pagar (despues del descuento): Lps.{total_con_descuento:.2f}")
    main()


# Función de reportes
def menu_reportes():
    # Variables globales a utilizar.
    global imprimir_menu
    global total_efectivo_caja
    global numero_compras
    global numero_ventas
    global valor_ventas
    global valor_compras
    global total_efectivo_compras
    global total_efectivo_ventas

    # Variables locales
    imprimir_menu = False
    esta_abierto_reportes = True

    # Imprime Menú Reportes
    print("===== MENU Reportes =====")
    print("1. Cantidad actual en caja")
    print("2. Numero de compras y ventas")
    print("3. Volumen de compras y ventas")
    print("4. Valor medio de compra y venta")
    print("5. Venta y Compra mayor")
    print("6. Regresar al menu principal")
    seleccion_usuario_reportes = input("Ingrese una opción: \n")

    # Bucle que verifica la opción del usuario.
    while esta_abierto_reportes:
        if seleccion_usuario_reportes == "1":
            esta_abierto_reportes = False
            # Imprime el total de efectivo actualmente en caja
            print(f"Total actual en caja: {total_efectivo_caja}")
            main()
        elif seleccion_usuario_reportes == "2":
            esta_abierto_reportes = False
            # Imprime el número de ventas y compras del día
            print(f"El número de ventas hoy fue de: {numero_ventas}")
            print(f"El número de compras hoy fue de: {numero_compras}")
            main()
        elif seleccion_usuario_reportes == "3":
            esta_abierto_reportes = False
            # Calcula ganancias
            ganancias_reportes = total_efectivo_ventas - total_efectivo_compras

            # Imprime total compras, ventas y ganancias.
            print(f"El total de compras hoy es de: Lps. {total_efectivo_compras}")
            print(f"El total de ventas hoy es de: Lps. {total_efectivo_ventas}")
            print(f"Las ganancias hoy son de: {ganancias_reportes}")
            main()

        elif seleccion_usuario_reportes == "4":
            esta_abierto_reportes = False
            # Suma valores de compras y ventas
            suma_valor_ventas = sum(valor_ventas)
            suma_valor_compras = sum(valor_compras)
            # Retorna el tamaño de cada arreglo
            cantidad_valor_ventas = len(valor_ventas)
            cantidad_valor_compras = len(valor_compras)

            # Calcula el promedio de ventas y compras
            promedio_ventas = suma_valor_ventas / cantidad_valor_ventas
            promedio_compras = suma_valor_compras / cantidad_valor_compras

            # Imprime los valores
            print(f"El promedio de ventas es de: {promedio_ventas}")
            print(f"El promedio de compras es de: {promedio_compras}")
            main()

        elif seleccion_usuario_reportes == "5":
            esta_abierto_reportes = False
            # Inicializamos el valor del arreglo
            venta_mayor = valor_ventas[0]
            compra_mayor = valor_compras[0]

            # Bucle que verifica cual es el valor mayor
            for valor_venta in valor_ventas:
                if valor_venta > venta_mayor:
                    venta_mayor = valor_venta

            for valor_compra in valor_compras:
                if valor_compra > compra_mayor:
                    compra_mayor = valor_compra

            # Imprime los valores
            print(f"La venta mayor hoy fue de: Lps.{venta_mayor}")
            print(f"La compra mayor hoy fue de: Lps.{compra_mayor}")
            main()

        elif seleccion_usuario_reportes == "6":
            esta_abierto_reportes = False
            # Regresa al menu principal
            main()
        else:
            print("ERROR: Ingrese una opción correcta.")
            main()


# Función cierre caja
def menu_cierre_caja():
    # Variables Globales
    global total_efectivo_compras
    global total_efectivo_ventas
    global total_efectivo_caja
    global imprimir_menu
    global esta_abierta_tienda
    global numero_ventas
    global numero_compras
    global valor_compras
    global valor_ventas

    # Varaibles locales
    imprimir_menu = False
    esta_abierto_cierre = True

    # Imprime menú
    print("===== MENU CIERRE CAJA =====")
    print("1. Cerrar caja")
    print("2. Regresar al menu principal")
    seleccion_usuario_cierre = input("Ingrese una opción: \n")

    while esta_abierto_cierre:
        if seleccion_usuario_cierre == "1":
            esta_abierta_tienda = False
            esta_abierto_cierre = False
            # Calcula ganancias.
            ganancias = total_efectivo_ventas - total_efectivo_compras

            # Imprime ganancias
            print(f"Total ganancias de hoy: {ganancias}")
            # Regresamos todos los contadores y valores a 0 o vacío.
            numero_ventas = 0
            numero_compras = 0
            total_efectivo_compras = 0
            total_efectivo_ventas = 0
            valor_ventas = []
            valor_compras = []
            main()
        elif seleccion_usuario_cierre == "2":
            esta_abierto_cierre = False
            main()
        else:
            print("ERROR: Ingrese una opción correcta.")


# Menu compras
def menu_compras():
    # Variables Globales
    global imprimir_menu
    global nombres_productos
    global precios_compra
    global precio_total
    global codigo_productos
    global total_efectivo_compras
    global total_efectivo_caja
    global numero_compras
    global valor_compras

    # Variables locales
    precio_total = 0
    precio_compra_total = 0
    imprimir_menu = False
    esta_abierto_compra = True

    print("===== MENU COMPRAS =====")
    print("1. Nueva compra")
    print("2. Regresar al menu principal")
    seleccion_usuario_compras = input("Ingrese una opción: \n")

    while esta_abierto_compra:
        if seleccion_usuario_compras == "1":
            esta_abierto_compra = False
            seleccion_tipo_cliente = input("Ingrese el tipo de proveedor (A, B o C): \n").upper()
            seleccion_codigo_producto = int(input("Ingrese el código del producto (1 - 4): \n"))
            seleccion_cantidad = float(input("Ingrese la cantidad de kilogramos: \n"))

            if validar_compra(seleccion_tipo_cliente, seleccion_codigo_producto):
                indice_producto = codigo_productos.index(seleccion_codigo_producto)
                nombre_producto = nombres_productos[indice_producto]
                precio_producto = precios_compra[indice_producto]

                subtotal = precio_producto * seleccion_cantidad
                precio_compra_total += subtotal
                # Valida si tenemos suficiente efectivo para hacer la compra.
                if total_efectivo_caja >= subtotal:
                    print(f"Producto: {nombre_producto}")
                    print(f"Cantidad: {seleccion_cantidad}")
                    print(f"Precio unitario: Lps.{precio_producto}")
                    print(f"Total: Lps. {subtotal:.2f}")

                    print(f"\nTotal a pagar: Lps. {precio_compra_total:.2f}")
                    # Agregamos valores a las variables globales
                    total_efectivo_caja -= subtotal
                    total_efectivo_compras += precio_compra_total
                    numero_compras += 1
                    valor_compras.append(precio_compra_total)
                    main()
                else:
                    print("ERROR: No se puede se puede pagar la compra")
                    main()
            elif not validar_compra(seleccion_tipo_cliente, seleccion_codigo_producto):
                esta_abierto_compra = False
                print("ERROR: El proveedor no vende ese producto")
                main()
            else:
                esta_abierto_compra = False
                print("Error: Ingrese una opción correcta.")
                main()

        else:
            esta_abierto_compra = False
            print("ERROR: Ingrese una opción correcta")
            main()


# Definimos funcion de validación para ventas
def validar_venta(tipo_cliente, codigo_producto):
    if tipo_cliente == "B" and codigo_producto in [1, 2, 3]:
        return True
    elif tipo_cliente == "C" and codigo_producto == 4:
        return True
    else:
        return False


# Definimos funcion de validación para compras
def validar_compra(tipo_proveedor, codigo_producto):
    if tipo_proveedor == "A" and codigo_producto in [1, 4]:
        return True
    elif tipo_proveedor == "B" and codigo_producto in [2, 3]:
        return True
    elif tipo_proveedor == "C" and codigo_producto == 2:
        return True
    else:
        return False


# Función Abrir Caja
def menu_abrir_caja():
    # Variables Globales
    global es_primera_ejecucion
    global imprimir_menu
    global esta_abierta_tienda
    global esta_ingresando_efectivo
    global total_efectivo_caja

    # Cambia valor de Variables Globales
    esta_ingresando_efectivo = True
    imprimir_menu = False

    # Verifica si es primera ejecución
    if es_primera_ejecucion:
        es_primera_ejecucion = False
        esta_abierta_tienda = True
        print("===SE HA ABIERTO CAJA===")

        while esta_ingresando_efectivo:
            esta_ingresando_efectivo = False
            efectivo_ingresado = input("Ingrese la cantidad de efectivo que desee:\n")
            if efectivo_ingresado == '':
                es_primera_ejecucion = True
                esta_abierta_tienda = False
                print("ERROR: Ingrese una cantidad de efectivo para abrir el sistema.")
                main()
            elif efectivo_ingresado.isdigit():
                cantidad_ingresada = int(efectivo_ingresado)
                total_efectivo_caja += cantidad_ingresada
                print(f"Se ha ingresado la cantidad de: Lps.{cantidad_ingresada}")
                main()
            else:
                es_primera_ejecucion = True
                esta_abierta_tienda = False
                print("Favor ingrese un número válido")
                main()

    else:
        print("===== MENU ABRIR CAJA =====")
        print("1. Ingresar Efectivo")
        print("2. Regresar al menu principal")
        seleccion_usuario_caja = input("Ingrese una opción \n")

        while esta_ingresando_efectivo:
            if seleccion_usuario_caja == "1":
                esta_ingresando_efectivo = False
                esta_abierta_tienda = True

                while True:
                    efectivo_ingresado = input("Ingrese la cantidad de efectivo que desee\n")
                    if efectivo_ingresado == '':
                        main()
                    elif efectivo_ingresado.isdigit():

                        cantidad_ingresada = int(efectivo_ingresado)
                        total_efectivo_caja += cantidad_ingresada
                        print(f"Se ha ingresado la cantidad de: Lps.{cantidad_ingresada}")
                        main()
                    else:
                        print("Favor ingrese un número válido")
                        main()

            elif seleccion_usuario_caja == "2":
                esta_ingresando_efectivo = False
                main()
            else:
                esta_ingresando_efectivo = False
                print("ERROR: Ingrese una opción correcta.")
                menu_abrir_caja()


# Imprime menu principal
def imprimir_principal():
    global esta_abierta_tienda

    print("==== Bienvenido a la Tienda Python =====")
    print("1. Abrir Caja")
    # Valida si la tienda esta abierta
    if esta_abierta_tienda:
        print("2. Ventas")
        print("3. Compras")
        print("4. Reportes")
        print("5. Cierre Caja")
    print("6. Salir del sistema")


# Cierra sistema
def cerrar_sistema():
    print("==CERRANDO SISTEMA==")
    # Retrasa un segundo
    sleep(1)
    print("Hasta luego...")
    sleep(1)
    exit()


# Función principal
def main():
    global imprimir_menu
    imprimir_menu = True
    # Valida opciones del usuario
    while imprimir_menu:
        imprimir_principal()
        seleccion_usuario = input("Ingrese una opción: \n")

        if seleccion_usuario == "1":
            menu_abrir_caja()
        elif seleccion_usuario == "2" and esta_abierta_tienda:
            menu_ventas()
        elif seleccion_usuario == "3" and esta_abierta_tienda:
            menu_compras()
        elif seleccion_usuario == "4" and esta_abierta_tienda:
            menu_reportes()
        elif seleccion_usuario == "5" and esta_abierta_tienda:
            menu_cierre_caja()
        elif seleccion_usuario == "6":
            cerrar_sistema()
        else:
            print("Por favor ingrese una opción válida o abra caja: ")


# Ejecuta la función main()
if __name__ == "__main__":
    main()
