print("")
import subprocess #Poder dirigirse de un archivo python a otro
import time  # Importamos la librería time para hacer pausas

# Creamos una función para mostrar un menú con opciones personalizado al cliente
def menu_personalizado():
    print("\n -------- BIENVENIDO/A A TURISMO Y MAS --------")
    print("\n1. Crear Plan Personalizado")
    print("2. Suscribirse a Membresía")
    print("3. (Gratis) Pasar al módulo de hotel y destino por separado (incluye paquetes de oferta).")
    print("4. Salir")


# Función para crear el plan personalizado del cliente
def crear_plan_personalizado():
    print("\n ----- Plan Personalizado -----")

    # Preguntamos al cliente por su plan ideal
    punto_de_partida = input(" > ¿Desde dónde vas a viajar?: ")
    destino = input(" > ¿Cuál es tu destino ideal?: ")
    compañia = input(" > ¿Vas a viajar sol@ o acompañad@?: ")
    presupuesto = input(" > ¿Cuál es tu presupuesto aproximado para tu viaje?: ")
    duracion = input(" > ¿Cuántos días planeas viajar?: ")
    email = input(" > Ingrese su email: ")

    # Brindamos diferentes recomendaciones según las respuestas del cliente
    print(f"\n ¡Perfecto! Según tu destino: {destino}, hemos encontrado algunas opciones que pueden ser de tu interés: ")
    time.sleep(2)  # Esta función hace que el programa se detenga por 2 segundos
    print("1. Hotel La Esmeralda con Desayuno y Tours incluidos")
    print("2. Hotel El Diamante con Almuerzos y actividades de aventuras incluidas")
    print("3. Hotel Roman con todo incluido")
    while True:
        eleccion = input("> Elige tu opción de preferencia: ")
        if eleccion == "1" or eleccion == "2" or eleccion == 3:
            print(f"\n ¡Tu plan para {destino} está listo! Disfrutarás de {duracion} días de forma {compañia} con un presupuesto de {presupuesto}. \n")
            print(f" Su factura de pago e información sobre el viaje ha sido enviada a {email}.")
            time.sleep(1)
            print(" Gracias por utilizar nuestros servicios!")
            break
        else:
            print("Por favor, ingrese una opción disponible.\n")

    


# Función para adquirir la suscripción del cliente
def suscripciones():
    print("\n ----- SUSCRIPCIONES ----- ")
    print("> Ofrecemos diferentes planes de Membresías: ")
    print(" 1. Plan Básico (Descuentos en Hoteles)")
    print(" 2. Plan Premium (Descuentos y ofertas exclusivas)")
    print(" 3. VIP (Acceso total a eventos y promociones)")

    email = input("\n> Ingrese su email: ")
    while True:
        suscripcion = input("\n> Elige el plan de suscripción que desees: ")

        # Mensajes personalizados según la suscripción seleccionada
        if suscripcion == '1':
            print("\n¡Gracias por suscribirte al Plan Básico! Disfrutarás de descuentos en nuestros diferentes hoteles.")
            print(f"Su factura de pago e información sobre el Plan escogido ha sido enviado a {email}.")
            break
        elif suscripcion == '2':
            print("\n¡Gracias por suscribirte al Plan Premium! Disfrutarás de ofertas exclusivas y descuentos.")
            print(f"Su factura de pago e información sobre el Plan escogido ha sido enviado a {email}.")
            break
        elif suscripcion == '3':
            print("\n¡Gracias por suscribirte al Plan VIP! Tendrás acceso total a eventos y promociones.")
            print(f"Su factura de pago e información sobre el Plan escogido ha sido enviado a {email}.")
            break
        else:
            print("Opción no válida. Por favor, intenta nuevamente.")
        time.sleep(2)


# Función para controlar el programa en general
def main():
    while True:
        menu_personalizado()  # Aquí mostramos el menú principal
        opcion = input("> Selecciona una opción: ")

        # Según la opción que el usuario elija, se ejecuta la función correspondiente
        if opcion == '1':
            crear_plan_personalizado()
            break
        elif opcion == '2':
            suscripciones()
            break
        elif opcion == '3':
            print("------------------------------------------------------------------------")
            print("Redirigiendo al módulo de hotel y destino por separado...\n")
            time.sleep(2)
            subprocess.run(['python', 'reserva_hotel_vuelo.py'])
            break
        elif opcion == '4':
            time.sleep(1)
            print("------------------------------------------------------------------------")
            print("Gracias por utilizar nuestra agencia de viajes. ¡Hasta pronto! \n")
            
            break
        else:
            print("Opción incorrecta. Por favor, elige una opción correcta.")
            time.sleep(2)


# Ejecutamos el programa principal
if __name__ == "__main__":
    main()
