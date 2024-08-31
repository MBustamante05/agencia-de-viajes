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
#Agregar función Oscar
#

#Lógica
def hoteles_destinos_separados():
    print("\n-- Estos son los destinos disponibles: --\n")
    #Mostrar vuelos disponibles
    for destino in destinos_hoteles.keys():
        print(destino)

    #Escoger destino
    print("-----------------------------------------")
    destino_usuario = input("Ingrese su destino: ").lower()

    #Mostrar hoteles disponibles
    def hotel_destino(destino):
        cuenta = 0
        for lugar in destinos_hoteles.keys():
            if destino == lugar.lower():
                print("Hoteles disponibles: \n")
                for hotel in destinos_hoteles[lugar][0]:
                    cuenta += 1
                    print(f"{cuenta}. {hotel}.")
        return "Destino no encontrado"

    hotel_destino(destino_usuario)
    print("-----------------------------------------")
    #Evitar colocar un index fuera del rango
    while True:
        hotel_usuario = int(input("Ingrese el número del hotel en el cual desea hospedarse: "))
        if hotel_usuario == 1 or hotel_usuario == 2 or hotel_usuario == 3:
            break
        else:
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
    #Mostrar factura antes de aceptar
    def confirma_factura():
        print(f"Destino:         {destino_primera_mayus}")
        print(f"Hotel:           {hotel_escogido_nombre}")
        print(f"Vuelo:           {vuelo}")
        print(f"Fecha-ida:       {fecha_ida}")
        print(f"Fecha-regreso:   {fecha_regreso}")
        print("-----------------------------------------")
        print(f"Total:           ${precio_hotel_mas_destino + vuelo_precio}")
    #Llamar a la función
    confirma_factura()
    #FUNCIÓN PARA PROCEDER CON LA FACTURA para no repetir todo un código dos veces
    def funcion_para_factura(nombre):
        time.sleep(3)
        print("-----------------------------------------")
        print("Pago exitoso.\nGracias por utilizar nuestros servicios.\n")
        time.sleep(1)
        print("-----------------------------------------")
        print("1. Recibir factura.")
        print("2. Salir.")
        opcion_factura = int(input("Ingrese el número de la opción con la cual desea continuar: "))
        while True:
            if opcion_factura == 1:
                time.sleep(3)
                factura_usuario(nombre)
                break
            elif opcion_factura == 2:
                break
            else:
                print("Opción errada. Inténtelo de nuevo.")
    #FUNCIÓN DE PAGO
    def pago():
        print("-----------------------------------------")
        print("Métodos de pago:")
        print("1. Tarjeta de Crédito/Débito.")
        print("2. PSE")
        print("-----------------------------------------")
        opcion_pago = int(input("Ingrese el número de la opción con la cual desea continuar: "))
        time.sleep(3)
        while True:
            if opcion_pago == 1:
                print("-----------------------------------------")
                nombre = input("Ingrese su nombre completo: ")
                tarjeta_num = input("Ingrese el número de la tarjeta de pago: ")
                funcion_para_factura(nombre)
                break
            elif opcion_pago == 2:
                print("-----------------------------------------")
                banco_nombre = input("Escribir nombre del banco: ")
                nombre = input("Ingrese su nombre completo: ")
                correo_pago = input("Ingrese su correo: ")
                clave_dinamica = input("Ingrese su clave dinámica: ")
                funcion_para_factura(nombre)
                break
            else:
                print("-----------------------------------------")
                print("Opción inválida. Vuelva a intentarlo.")
          
    #FUNCIÓN FACTURA
    def factura_usuario(nombre):
        print("-----------------------------------------")
        print("---------------PAGO ACEPTADO-------------")
        print(f"Cliente:         {nombre}")
        confirma_factura()
        print(f"Pagado:         -${precio_hotel_mas_destino + vuelo_precio}")
        print("-----------------------------------------")
    #Opción de aceptar o nó
    while True:
        confirma = input("Confirma las opciones de su factura? (y-n): ").lower()
        if confirma == "y":
            print("Espere unos segundos mientras se redirige a la página de pago...\n")
            time.sleep(5)
            pago()
            break 
        elif confirma == "n":
            print("-----------------------------------------")
            print("1. Terminar proceso.")
            print("2. Cambiar opciones de vuelo.")
            while True:  # Bucle para salir o cambiar
                try: #Maneja errores de conversión a la hora de entrar el número
                    salir_o_cambiar = int(input("Ingrese el número de la opción con la cual desea continuar (1-2): "))
                    if salir_o_cambiar == 1:
                        print("Gracias por acceder a nuestros servicios.")
                        break 
                    elif salir_o_cambiar == 2:
                        hoteles_destinos_separados()
                        break  
                    else:
                        print("Opción errada.")
                except ValueError:
                    print("Por favor, ingrese un número válido (1 o 2).")
            break  
        else:
            print("Opción errada. Ingrese una opción válida (y-n).")


#Opciones entre servicio normal de la agencia o paquetes de oferta
print("--------------BIENVENIDO/A---------------")
print("1. Escoger destino y hotel por separado.")
print("2. Escoger paquetes en oferta.")
print("3. Salir.")
print("-----------------------------------------")
while True: #Evitar una opción fuera del rango
  opcion = int(input("Ingrese el número de la opción con la cual desea continuar: "))
  if opcion == 1:
    print("Redirigiendo...")
    time.sleep(4)
    hoteles_destinos_separados()
    break
  elif opcion == 2:
    print("Redirigiendo...")
    time.sleep(4)
    print("Sección de paquetes") #Cambiar línea a nombre función de Oscar.
    break
  elif opcion == 3:
    print("Gracias por acceder a nuestros servicios.")
    break
  else:
    print("Opción inválida.\n")