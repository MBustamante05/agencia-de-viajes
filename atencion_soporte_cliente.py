# -*- coding: utf-8 -*-
"""Atencion_Y_soporte.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nCDVWcS91BG9uCY3TC6FCl8Cwv9N6Bvd
"""
#Lógica Juan
## Atención al cliente
def Atencion_cliente():
    print("\nHas elegido Atención al Cliente.")
    print("Opciones disponibles:")
    print("1. Consultar estado de un pedido")
    print("2. Preguntas sobre facturación")
    print("3. Devoluciones y reembolsos")
    print("4. Otra consulta")
    while True:
      # Captura la opción del usuario
      print("\n-----------------------------------------")
      opcion_cliente = input("Elige una opción (1, 2, 3 o 4): ")

      if opcion_cliente == '1':
          # Lógica para consultar el estado de un pedido
          numero_pedido = input("Por favor, ingresa tu número de pedido: ")
          # Supongamos que aquí se verifica el número de pedido en una base de datos
          print(f"El pedido con número {numero_pedido} está en proceso de envío.")
          break

      elif opcion_cliente == '2':
          # Lógica para preguntas sobre facturación
          print("\n-----------------------------------------")
          print("Preguntas frecuentes sobre facturación:")
          print("1. ¿Cómo veo mi factura?")
          print("2. ¿Cuándo se cobrará mi cuenta?")
          print("3. ¿Cómo puedo actualizar mi información de pago?")

          while True:
            opcion_facturacion = input("Elige una pregunta (1, 2 o 3): ")
            if opcion_facturacion == '1':
                print("Puedes ver tu factura en el área de clientes de nuestra página web, sección 'Facturas'.")
                break
            elif opcion_facturacion == '2':
                print("El cobro se realiza 48 horas después de que se haya confirmado tu pedido.")
                break
            elif opcion_facturacion == '3':
                print("Puedes actualizar tu información de pago en tu cuenta en línea, bajo la sección 'Métodos de Pago'.")
                break
            else:
                print("Opción no válida en Preguntas sobre Facturación.")
          break

      elif opcion_cliente == '3':
          # Lógica para devoluciones y reembolsos
          print("\n-----------------------------------------")
          print("Opciones de devoluciones y reembolsos:")
          print("1. Devolver un producto")
          print("2. Solicitar un reembolso")
          print("3. Ver el estado de una devolución")
          while True:
            opcion_devoluciones = input("Elige una opción (1, 2 o 3): ")

            if opcion_devoluciones == '1':
                producto = input("Por favor, ingresa el nombre del producto que deseas devolver: ")
                print(f"Se ha iniciado el proceso de devolución para {producto}. Pronto recibirás un correo con las instrucciones.")
                break
            elif opcion_devoluciones == '2':
                numero_pedido = input("Ingresa el número de pedido para solicitar el reembolso: ")
                print(f"Tu solicitud de reembolso para el pedido {numero_pedido} ha sido recibida. Se procesará en los próximos 5 días hábiles.")
                break
            elif opcion_devoluciones == '3':
                numero_devolucion = input("Ingresa el número de devolución: ")
                print(f"Tu devolución con número {numero_devolucion} está en proceso. Recibirás una confirmación cuando haya sido completada.")
                break
            else:
                print("Opción no válida en Devoluciones y Reembolsos.")
          break

      elif opcion_cliente == '4':
          # Permitir al usuario escribir una consulta personalizada
          consulta = input("Por favor, escribe tu consulta: ")
          print(f"Gracias por tu consulta: '{consulta}'. Un agente te responderá pronto.")
          break
          # Aquí podrías enviar la consulta a un sistema de atención al cliente
      else:
          print("Opción no válida en Atención al Cliente.")


## Soporte al usuario
def Soporte_usuario():
    print("\nHas elegido Soporte al Usuario.")
    print("Opciones disponibles:")
    print("1. Problemas de acceso")
    print("2. Asistencia técnica con software")
    print("3. Configuración de dispositivos")
    print("4. Otra consulta")
    while True:
      # Captura la opción del usuario
      opcion_soporte = input("Elige una opción (1, 2, 3 o 4): ")

      if opcion_soporte == '1':
          # Lógica para resolver problemas de acceso
          print("Problemas de acceso:")
          print("1. Restablecer contraseña")
          print("2. Recuperar nombre de usuario")
          print("3. Error de inicio de sesión")
          while True:
            problema_acceso = input("Elige una opción (1, 2 o 3): ")

            if problema_acceso == '1':
                email = input("Por favor, ingresa tu correo electrónico para restablecer la contraseña: ")
                print(f"Se ha enviado un enlace de restablecimiento de contraseña a {email}.")
                break
            elif problema_acceso == '2':
                email = input("Por favor, ingresa tu correo electrónico para recuperar tu nombre de usuario: ")
                print(f"Tu nombre de usuario ha sido enviado a {email}.")
                break
            elif problema_acceso == '3':
                print("Verifica que tu conexión a internet esté activa.")
                print("Asegúrate de que las credenciales de inicio de sesión sean correctas.")
                break
            else:
                print("Opción no válida en Problemas de acceso.")
          break
      elif opcion_soporte == '2':
          # Lógica para asistencia técnica con software
          print("Asistencia técnica con software:")
          print("1. Problema de instalación")
          print("2. Error de ejecución")
          print("3. Software no responde")
          while True:
            problema_software = input("Elige una opción (1, 2 o 3): ")

            if problema_software == '1':
                print("Solución: Asegúrate de tener suficiente espacio en disco e intenta ejecutar el instalador como administrador.")
                break
            elif problema_software == '2':
                print("Solución: Verifica si hay actualizaciones disponibles o reinstala el software.")
                break
            elif problema_software == '3':
                print("Solución: Cierra el programa y reinicia tu dispositivo. Si el problema persiste, reinstala el software.")
                break
            else:
                print("Opción no válida en Asistencia técnica con software.")
          break
      elif opcion_soporte == '3':
          # Lógica para asistencia con configuración de dispositivos
          print("Configuración de dispositivos:")
          print("1. Conectar a internet")
          print("2. Configurar impresora")
          print("3. Conectar dispositivo Bluetooth")
          while True:
            configuracion_dispositivo = input("Elige una opción (1, 2 o 3): ")

            if configuracion_dispositivo == '1':
                print("Guía: Verifica que el router esté encendido y sigue las instrucciones del dispositivo para conectarte a la red.")
                break
            elif configuracion_dispositivo == '2':
                print("Guía: Asegúrate de que los controladores de la impresora estén instalados correctamente y la impresora esté conectada.")
                break
            elif configuracion_dispositivo == '3':
                print("Guía: Activa el Bluetooth en tu dispositivo y asegúrate de que el dispositivo que deseas conectar esté en modo de emparejamiento.")
                break
            else:
                print("Opción no válida en Configuración de dispositivos.")
          break

      elif opcion_soporte == '4':
          # Permitir al usuario escribir una consulta personalizada
          consulta = input("Por favor, escribe tu consulta: ")
          print(f"Gracias por tu consulta: '{consulta}'. Un agente te responderá pronto.")
          break
          # Aquí podrías enviar la consulta a un sistema de soporte
      else:
          print("Opción no válida en Soporte al Usuario.")


# Llamada principal para ejecutar las funciones
def main():
    print("Elige un servicio:")
    print("1. Atención al Cliente")
    print("2. Soporte al Usuario")

    while True:
      opcion = input("Escribe 1 o 2 según tu elección: ")
      if opcion == '1':
          Atencion_cliente()
          break
      elif opcion == '2':
          Soporte_usuario()
          break
      else:
          print("Opción no válida. Por favor, elige 1 o 2.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()