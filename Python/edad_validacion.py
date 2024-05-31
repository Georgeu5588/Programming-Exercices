#Ejercicio 1: Validación de Edad
#Un equipo de desarrollo necesita una función para validar si un usuario es mayor de edad (18 años o más). Si es mayor de edad, se le debe permitir el acceso, de lo contrario, se debe denegar.

edad = input('Ingrese su edad: ')
edad = int(edad)

def validarEdad():
    if edad >= 18:
        print('Acceso permitido.')
    else:
        print('Acceso denegado.')

validarEdad()
