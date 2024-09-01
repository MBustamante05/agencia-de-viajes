import time #Importar librería de espera
import random #Importar librería aleatoria

#DESTINO Y HOTEL POR SEPARADO
#Diccionario de vuelos y horarios
vuelos = {
    "Iberia": {
        "precio": 350000
    },
    "LATAM": {
        "precio": 420000
    },
    "Avianca": {
        "precio": 390000
    },
    "Emirates": {
        "precio": 460000
    }
}
#Diccionario con destinos y hoteles
destinos_hoteles = {
    "Habana": [
        ["Hotel Nacional", "Hotel Saratoga", "Hotel Meliá Cohiba"],
        [4000000, 2000000, 720000]
    ],
    "Quito": [
        ["Hotel Plaza Grande", "Hotel Casa Gangotena", "Swissotel Quito"],
        [1200000, 1400000, 1000000]
    ],
    "Paris": [
        ["Le Bristol Paris", "Shangri-La Hotel", "The Ritz Paris"],
        [7200000, 5800000, 9600000]
    ],
    "Tokio": [
        ["Park Hyatt Tokyo", "The Peninsula Tokyo", "Hotel New Otani"],
        [9400000, 12200000, 10600000]
    ],
    "Nueva York": [
        ["The Plaza Hotel", "Four Seasons Hotel", "The Ritz-Carlton New York"],
        [4000000, 3800000, 3400000]
    ],
    "Roma": [
        ["Hotel Eden", "Hotel Hassler", "Rome Cavalieri"],
        [5800000, 7800000, 6600000]
    ],
    "Londres": [
        ["The Savoy", "Claridge's", "The Ritz London"],
        [10800000, 12600000, 13000000]
    ],
    "Ciudad de Mexico": [
        ["Four Seasons Hotel", "St. Regis Mexico City", "Hotel Condesa DF"],
        [2000000, 1800000, 1200000]
    ],
    "Bangkok": [
        ["Mandarin Oriental Bangkok", "The Peninsula Bangkok", "Banyan Tree Bangkok"],
        [6600000, 7400000, 10000000]
    ],
    "Sidney": [
        ["Four Seasons Hotel Sydney", "Shangri-La Hotel Sydney", "Park Hyatt Sydney"],
        [4500000, 6800000, 8600000]
    ],
    "Dubai": [
        ["Burj Al Arab", "Atlantis The Palm", "The Ritz-Carlton Dubai"],
        [8000000, 9000000, 10600000]
    ],
    "Buenos Aires": [
        ["Alvear Palace Hotel", "Palacio Duhau - Park Hyatt", "Faena Hotel Buenos Aires"],
        [1600000, 1400000, 1200000]
    ],
    "Barcelona": [
        ["Hotel Arts Barcelona", "W Barcelona", "Majestic Hotel & Spa"],
        [2400000, 3200000, 2800000]
    ],
    "Miami": [
        ["Fontainebleau Miami Beach", "The Setai Miami Beach", "Eden Roc Miami Beach"],
        [3200000, 3000000, 2800000]
    ],
    "Los Angeles": [
        ["Beverly Wilshire", "The Ritz-Carlton Los Angeles", "Hotel Bel-Air"],
        [2800000, 2600000, 2400000]
    ],
    "Marrakech": [
        ["La Mamounia", "Royal Mansour Marrakech", "Mandarin Oriental Marrakech"],
        [1800000, 1600000, 1400000]
    ],
    "Estambul": [
        ["Four Seasons Hotel Istanbul", "Ciragan Palace Kempinski", "The Ritz-Carlton Istanbul"],
        [7200000, 6000000, 5800000]
    ],
    "Moscu": [
        ["Hotel Baltschug Kempinski", "Four Seasons Hotel Moscow", "The Ritz-Carlton Moscow"],
        [5400000, 7200000, 8000000]
    ],
    "Toronto": [
        ["The Ritz-Carlton Toronto", "Fairmont Royal York", "Shangri-La Hotel Toronto"],
        [2800000, 2400000, 2200000]
    ],
    "Lisboa": [
        ["Four Seasons Hotel Ritz Lisbon", "Altis Belém Hotel & Spa", "Pestana Palace Lisboa"],
        [4300000, 5800000, 3600000]
    ]
}

#Lógica Oscar
# Lista para almacenar los paquetes turísticos como diccionarios
paquetes = []

# Función para agregar un paquete turístico a la lista
def agregar_paquete(id_paquete, nombre, destino, duracion, duracion2, precio, descripcion):
        paquete = {
            'id_paquete': id_paquete,
            'nombre': nombre,
            'destino': destino,
            'duracion': duracion,  # Duración en días
            'duracion2': duracion2,  # Duración en noches
            'precio': precio,
            'descripcion': descripcion
        }
        paquetes.append(paquete)

# Función para mostrar todos los paquetes turísticos
def mostrar_paquetes():
        print("--------------------------------------------------------------------------------")
        if paquetes:
            print("Elige el paquete que más se adapte a tus gustos y necesidades.")
            print("Estos son los paquetes turísticos disponibles:")
            print("--------------------------------------------------------------------------------")
            for i, paquete in enumerate(paquetes, 1):
                print(f"{i}. {paquete['nombre']} a {paquete['destino']} por {paquete['duracion']} días y {paquete['duracion2']} noches - Precio: ${paquete['precio']}")

#Función de factura del paquete (destino, hotel, vuelo, fecha_ida, fecha_regreso, precio_total)
def pago_paquete(precio_total):
    print("-----------------------------------------")
    print("Métodos de pago:")
    print("1. Tarjeta de Crédito/Débito.")
    print("2. PSE")
    print("-----------------------------------------")
    while True:
        opcion_pago = input("Ingrese el número de la opción con la cual desea continuar: ")
        if opcion_pago == "1":
            print("-----------------------------------------")
            nombre = input("Ingrese su nombre completo: ")
            tarjeta_num = input("Ingrese el número de la tarjeta de pago: ")
            factura_paquete(nombre,precio_total)
            break
        elif opcion_pago == "2":
            print("-----------------------------------------")
            banco_nombre = input("Escribir nombre del banco: ")
            nombre = input("Ingrese su nombre completo: ")
            correo_pago = input("Ingrese su correo: ")
            clave_dinamica = input("Ingrese su clave dinámica: ")
            factura_paquete(nombre,precio_total)
            break
        else:
            print("-----------------------------------------")
            print("Opción inválida. Vuelva a intentarlo.")


#Función para factura de paquete
def factura_paquete(nombre, precio_total):
    time.sleep(3)
    print("-----------------------------------------")
    print("Pago exitoso.\nGracias por utilizar nuestros servicios.\n")
    time.sleep(1)
    print("-----------------------------------------")
    print("1. Recibir factura.")
    print("2. Salir.")
    while True:
        opcion_factura = input("Ingrese el número de la opción con la cual desea continuar: ")
        if opcion_factura == "1":
            time.sleep(3)
            print("-----------------------------------------")
            print("---------------PAGO ACEPTADO-------------")
            print("----------paquete todo incluído----------")
            print(f"Cliente:         {nombre}")
            print(f"Total:           {precio_total}")
            print("-----------------------------------------")
            print(f"Pagado:         -${precio_total}")
            print("-----------------------------------------")

            break
        elif opcion_factura == "2":
            print("Gracias por utilizar nuestros servicios. Vuelve pronto!!")
            break
        else:
            print("Opción errada. Inténtelo de nuevo.")

# Función para que el usuario escoja un paquete y mostrarlo
def seccion_paquetes():
    mostrar_paquetes()
    print("--------------------------------------------------------------------------------")
    while True: 
        opcion = int(input("Introduce el número del paquete que deseas escoger: "))
        
        if opcion <= len(paquetes):
            paquete_seleccionado = paquetes[opcion - 1]
            print("\nHas seleccionado el siguiente paquete:")
            print(f"Nombre: {paquete_seleccionado['nombre']}")
            print(f"Destino: {paquete_seleccionado['destino']}")
            print(f"Duración: {paquete_seleccionado['duracion']} días y {paquete_seleccionado['duracion2']} noches")
            print(f"Precio: ${paquete_seleccionado['precio']}")
            print(f"Descripción: {paquete_seleccionado['descripcion']}")
            print("--------------------------------------------------------------------------------\n")
            while True:
                confirma_factura = input("Confirma las opciones de su paquete? (y-n): ")
                if confirma_factura == "y":
                    print("Redirigiendo...")
                    time.sleep(4)
                    pago_paquete(paquete_seleccionado['precio'])
                    break
                elif confirma_factura == "n":
                    seccion_paquetes()
                    break
                else:
                    print("Opción inválida. Por favor, ingrese 'y' o 'n'.")
            break
        else:
            print("Opción inválida. Por favor, selecciona un número de la lista.")

# Agregar los paquetes
agregar_paquete(1, "Aventura Urbana", "Nueva York", 7, 6, 5500000, "Incluye alojamiento en hotel céntrico y visitas guiadas a museos.")
agregar_paquete(2, "Escapada Romántica", "Paris", 6, 5, 6800000, "Incluye hotel cerca de la Torre Eiffel y cena en crucero por el Sena.")
agregar_paquete(3, "Exploración Cultural", "Ciudad de México", 5, 4, 4200000, "Incluye hotel en el centro histórico y tours gastronómicos.")
agregar_paquete(4, "Safari Urbano", "Tokio", 8, 7, 7200000, "Incluye alojamiento en hotel de lujo y paseos por la ciudad y alrededores.")
agregar_paquete(5, "Ruta Histórica", "Roma", 6, 5, 6500000, "Incluye hotel en el centro de Roma y visitas guiadas al Coliseo y Vaticano.")
agregar_paquete(6, "Aventura en el Desierto", "Dubai", 7, 6, 8200000, "Incluye hotel de lujo, safari por el desierto y crucero nocturno.")
agregar_paquete(7, "Exploración Asiática", "Bangkok", 6, 5, 5900000, "Incluye alojamiento y visitas a templos y mercados flotantes.")
agregar_paquete(8, "Cultura y Playa", "Barcelona", 5, 4, 5700000, "Incluye hotel cerca de la playa y visitas a museos y Sagrada Familia.")
agregar_paquete(9, "Naturaleza y Cultura", "Sidney", 8, 7, 9500000, "Incluye alojamiento, tours por la ciudad y visita a las Montañas Azules.")
agregar_paquete(10, "Escape al Caribe", "La Habana", 6, 5, 5100000, "Incluye hotel en el Malecón, visitas a sitios históricos y experiencia de salsa cubana.")



#Lógica María
def mostrar_detalle_factura(destino, hotel, vuelo, fecha_ida, fecha_regreso, precio_total):
    print(f"Destino:         {destino}")
    print(f"Hotel:           {hotel}")
    print(f"Vuelo:           {vuelo}")
    print(f"Fecha-ida:       {fecha_ida}")
    print(f"Fecha-regreso:   {fecha_regreso}")
    print("-----------------------------------------")
    print(f"Total:           ${precio_total}")

#Llamar a la función
    
#FUNCIÓN PARA PROCEDER CON LA FACTURA para no repetir todo un código dos veces
def funcion_para_factura(nombre, destino, hotel, vuelo, fecha_ida, fecha_regreso, precio_total):
    time.sleep(3)
    print("-----------------------------------------")
    print("Pago exitoso.\nGracias por utilizar nuestros servicios.\n")
    time.sleep(1)
    print("-----------------------------------------")
    print("1. Recibir factura.")
    print("2. Salir.")
    while True:
        opcion_factura = input("Ingrese el número de la opción con la cual desea continuar: ")
        if opcion_factura == "1":
            time.sleep(3)
            factura_usuario(nombre, destino, hotel, vuelo, fecha_ida, fecha_regreso, precio_total)
            break
        elif opcion_factura == "2":
            print("Gracias por utilizar nuestros servicios. Vuelve pronto!!")
            break
        else:
            print("Opción errada. Inténtelo de nuevo.")

#FUNCIÓN DE PAGO
def pago(destino, hotel, vuelo, fecha_ida, fecha_regreso, precio_total):
    print("-----------------------------------------")
    print("Métodos de pago:")
    print("1. Tarjeta de Crédito/Débito.")
    print("2. PSE")
    print("-----------------------------------------")
    while True:
        opcion_pago = input("Ingrese el número de la opción con la cual desea continuar: ")
        time.sleep(3)
        if opcion_pago == "1":
            print("-----------------------------------------")
            nombre = input("Ingrese su nombre completo: ")
            tarjeta_num = input("Ingrese el número de la tarjeta de pago: ")
            funcion_para_factura(nombre, destino, hotel, vuelo, fecha_ida, fecha_regreso, precio_total)
            break
        elif opcion_pago == "2":
            print("-----------------------------------------")
            banco_nombre = input("Escribir nombre del banco: ")
            nombre = input("Ingrese su nombre completo: ")
            correo_pago = input("Ingrese su correo: ")
            clave_dinamica = input("Ingrese su clave dinámica: ")
            funcion_para_factura(nombre, destino, hotel, vuelo, fecha_ida, fecha_regreso, precio_total)
            break
        else:
            print("-----------------------------------------")
            print("Opción inválida. Vuelva a intentarlo.")

        
#FUNCIÓN FACTURA
def factura_usuario(nombre, destino, hotel, vuelo, fecha_ida, fecha_regreso, precio_total):
    print("-----------------------------------------")
    print("---------------PAGO ACEPTADO-------------")
    print(f"Cliente:         {nombre}")
    mostrar_detalle_factura(destino, hotel, vuelo, fecha_ida, fecha_regreso, precio_total)
    print(f"Pagado:         -${precio_total}")
    print("-----------------------------------------")

def confirmar_y_pagar(destino, hotel, vuelo, fecha_ida, fecha_regreso, precio_total):
    mostrar_detalle_factura(destino, hotel, vuelo, fecha_ida, fecha_regreso, precio_total)
    while True:
        confirma = input("Confirma las opciones de su factura? (y-n): ").lower()
        if confirma == "y":
            print("Espere unos segundos mientras se redirige a la página de pago...\n")
            time.sleep(5)
            pago(destino, hotel, vuelo, fecha_ida, fecha_regreso, precio_total)
            break 
        elif confirma == "n":
            print("-----------------------------------------")
            print("1. Terminar proceso.")
            print("2. Cambiar opciones de vuelo.")
            while True:
                try:
                    salir_o_cambiar = int(input("Ingrese el número de la opción con la cual desea continuar (1-2): "))
                    if salir_o_cambiar == 1:
                        print("Gracias por acceder a nuestros servicios.")
                        return  
                    elif salir_o_cambiar == 2:
                        hoteles_destinos_separados()
                        return 
                    else:
                        print("Opción errada.")
                except ValueError:
                    print("Por favor, ingrese un número válido (1 o 2).")
        else:
            print("Opción errada. Ingrese una opción válida (y-n).")


def hoteles_destinos_separados():
    while True:
        time.sleep(3)
        print("\n-- Estos son los destinos disponibles: --\n")
        # Mostrar destinos disponibles
        for destino in destinos_hoteles.keys():
            print(destino)

        # Escoger destino
        print("-----------------------------------------")
        destino_usuario = input("Ingrese su destino: ").lower()

        #mostrar hoteles disponibles
        cuenta = 0
        destino_encontrado = False  # mostrar si el destino existe
        for lugar in destinos_hoteles.keys():
            if destino_usuario == lugar.lower():
                destino_encontrado = True
                print("Hoteles disponibles: \n")
                for hotel in destinos_hoteles[lugar][0]:
                    cuenta += 1
                    print(f"{cuenta}. {hotel}.")

        if destino_encontrado:
            break 
        else:
            print("Destino no encontrado. Por favor, intente de nuevo.")

    print("-----------------------------------------")
    #Evitar colocar un index fuera del rango
    while True:
        try:
            hotel_usuario = int(input("Ingrese el número del hotel en el cual desea hospedarse: "))
            if hotel_usuario == 1 or hotel_usuario == 2 or hotel_usuario == 3:
                break
            else:
                print("Opción inválida.\n")
        except ValueError:
            print("Opción inválida.\n")

    #CALENDARIO
    fecha_ida = input("Ingrese la fecha de ida (Ex: 12-05-2024): ")
    fecha_regreso = input("Ingrese la fecha de regreso (Ex: 12-05-2024): ")  


    print("\n\n-----------------------------------------")
    print("-----------CONFIRMAR FACTURA-------------")
    #Escoger vuelo aleatorio disponible
    vuelo = random.choice(list(vuelos.keys()))
    vuelo_precio = vuelos[vuelo]["precio"] #Sacar solamente el precio del vuelo

    #CONFIRMAR HOTEL Y DESTINO
    #Colocar primera letra en mayuscula
    destino_primera_mayus = destino_usuario.title()
    
    #Sacar el nombre del hotel para colocarlo en la factura
    hotel_escogido_nombre = destinos_hoteles[destino_primera_mayus][0][hotel_usuario - 1]
    precio_hotel_mas_destino = destinos_hoteles[destino_primera_mayus][1][hotel_usuario - 1]
    
    #Llamar a las otras funciones
    precio_total = precio_hotel_mas_destino + vuelo_precio
    confirmar_y_pagar(destino_primera_mayus, hotel_escogido_nombre, vuelo, fecha_ida, fecha_regreso, precio_total)

#Opciones entre servicio normal de la agencia o paquetes de oferta
print("--------------BIENVENIDO/A---------------")
print("1. Escoger destino y hotel por separado.")
print("2. Escoger paquetes en oferta.")
print("3. Salir.")
print("-----------------------------------------")
while True: #Evitar una opción fuera del rango
  opcion = input("Ingrese el número de la opción con la cual desea continuar: ")
  if opcion == "1":
    print("Redirigiendo...")
    time.sleep(1)
    hoteles_destinos_separados()
    break
  elif opcion == "2":
    print("Redirigiendo...")
    time.sleep(4)
    seccion_paquetes()
    break
  elif opcion == "3":
    print("Gracias por acceder a nuestros servicios.")
    break
  else:
    print("Opción inválida.\n")