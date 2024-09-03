#Registrar usuario con nombre y contraseña
import stdiomask #Libreria para ocultar contraseña

nombre_usuario = input("Ingrese su nombre: ").lower()
email_usuario = input("Ingrese su email: ")
contraseña_usuario = stdiomask.getpass("Ingresa tu contraseña: ","*")

print("\nHas sido registrado exitosamente!")
#Mensaje de bienvenida al software
print("\n---------------------------------")
print(f"Bienvenido/a a Skyline Adventures, {nombre_usuario}.")
