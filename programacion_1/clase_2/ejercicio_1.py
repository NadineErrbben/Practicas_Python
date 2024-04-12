"""funcion que reciba un numero y determine si es par o no y devuelva en string el resultado
"""

def determinar_paridad(numero):
    if numero_ingresado % 2 == 0:
        mensaje = "numero par"
    else:
        mensaje = "numero no par"
    return mensaje

numero_ingresado = input("ingrese un numero: ")
numero_ingresado = int(numero_ingresado)
resultado = determinar_paridad(numero_ingresado)
print(resultado)

