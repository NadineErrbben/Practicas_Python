"""UTN Technologies, una reconocida software factory se encuentra en la búsqueda de ideas para su próximo desarrollo en Python, que promete revolucionar el mercado.

Las posibles aplicaciones son las siguientes:
Inteligencia artificial (IA),:
Realidad virtual/aumentada (RV/RA),
Internet de las cosas (IOT)

Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.

A) Los datos a ingresar por cada empleado encuestado son:
nombre del empleado
edad (no menor a 18)
género (Masculino - Femenino - Otro)
tecnologia (IA, RV/RA, IOT)  
B) Cargar por terminal 10 encuestas.
C) Determinar:
1) Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
2) Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
3) Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.
"""

contador_m = 0
contador_no_ia_no_f_33_40 = 0
edad_maxima = 0

for i in range(4):
    nombre = input("ingrese su nombre: ")
    edad = input("ingrese su edad: ")
    edad = int(edad)
    while edad < 18:
        edad = input("ingrese su edad +18: ")
        edad = int(edad)
        
    genero = input("ingrese su genero m, f, nb")
    while genero != "m" and genero != "f" and genero != "nb":
        genero = input("ingrese un genero valido m, f, nb: ")

    tecnologia = input("ingrese su tecnologia IA - RV - IOT: ")
    while tecnologia != "ia" and tecnologia != "rv" and tecnologia != "iot":
        tecnologia = input("ingrese una tecnologia valida: IA - RV - IOT")

    match genero:
        case "m":
            if (tecnologia == "ia" or tecnologia == "iot") and (edad > 25 and edad < 50):
                contador_m += 1
            if edad > edad_maxima:
                edad_maxima = edad
                nombre_m_maxima_edad = nombre
                tecnologia_m_maxima_edad = tecnologia
    
    if tecnologia != "ia" and genero != "f" and (edad > 33 and edad < 40):
        contador_no_ia_no_f_33_40 += 1

    
porcentaje_no_ia_no_f_33_40 = (contador_no_ia_no_f_33_40 * 100) / 10

print(f"cantidad de empleados m que votaron IOT o IA entre 25 y 50: {contador_m}/n")
print(f"porcentaje de empleados no IA no F: {porcentaje_no_ia_no_f_33_40}/n")
print(f"nombre del masc con mayor edad: {nombre_m_maxima_edad}, tecnologia: {tecnologia_m_maxima_edad}")





            



