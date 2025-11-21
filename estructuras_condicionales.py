"""
Ejercicio 1 Mayor de edad
Escribir un programa que solicite la edad del usuario. 
Si el usuario es mayor de 18 años, deberá mostrar un 
mensaje en pantalla que diga “Es mayor de edad”
"""
edad = int (input("ingrese su edad:"))
if edad >= 18:
    print("Es mayo de edad")

"""
Ejercicio 2 "Resultado parcial"
Escribir un programa que solicite su nota al usuario. 
Si la nota es mayor o igual a 6, deberá mostrar por pantalla 
un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
mensaje “Desaprobado”.
"""
nota = float (input("ingrese la nota del parcial:"))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

"""
Ejercicio 3 "Es un numero Par"
Escribir un programa que permita ingresar solo números pares.
Si el usuario ingresa un número par, imprimir por en 
pantalla el mensaje "Ha ingresado un número par"; en caso 
contrario, imprimir por pantalla "Por favor, ingrese un número par".
Nota: investigar el uso del operador de módulo (%) en Python 
para evaluar si un número es par o impar. 
"""
numero = int (input("ingrese un numero par:"))
if numero % 2 ==0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un número par")

"""
Ejercicio 4 "Etapas del desarroyo humano"
Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
siguientes categorías pertenece:  
• Niño/a: menor de 12 años.  
• Adolescente: mayor o igual que 12 años y menor que 18 años.  
• Adulto/a joven: mayor o igual que 18 años y menor que 30 años.  
• Adulto/a: mayor o igual que 30 años.  
"""
edad = int (input("ingrese su edad:"))
if edad < 12:
    print("Es un niño/a")
elif edad >= 12 and edad < 18:
    print("Es un Adolescente")
elif edad >= 18 and edad < 30:
    print("Es adulto/a o joven")
elif edad >= 30:
    print("Es adulto/a")

"""
Ejercicio 5 "Contraseñas"
Escribir un programa que permita introducir contraseñas 
de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario 
ingresa una contraseña de longitud adecuada, imprimir por en 
pantalla el mensaje "Ha ingresado una contraseña correcta";
en caso contrario, imprimir por pantalla "Por favor, 
ingrese una contraseña de entre 8 y 14 caracteres". 
"""
password = len(input("ingrese su contraseña:"))
if password >= 8 and password <= 14:
    print("Ha ingresado una contraseña correcta")
else: 
    print("Por favor,ingrese una contraseña de entre 8 y 14 caracteres")

"""
Ejercicio 6 "Consumo energetico"
Escribir un programa que solicite al usuario el consumo 
mensual de energía eléctrica en kilovatios (kWh) e indique 
la categoría del consumo según el siguiente criterio: 
    • Menor que 150 kWh: “Consumo bajo”. 
    • Entre 150 y 300 kWh (inclusive): “Consumo medio”. 
    • Mayor que 300 kWh: “Consumo alto”. 
Además, si el consumo supera los 500 kWh, mostrar un mensaje adicional que diga: 
    “Considere medidas de ahorro energético”. 
"""
consumo = int(input("ingrese su el consumo mensual " \
                     "de energía eléctrica en kilovatios (kWh)"))
if consumo < 150:
    print("Consumo bajo")
elif consumo >= 150 and consumo <= 300:
    print("Consumo medio")
elif consumo > 300:
    print("Consumo alto")
    if consumo >= 500:
        print ("“Considere medidas de ahorro energético”")

"""
Ejercicio 7 "palabras"
Escribir un programa que solicite una frase o palabra 
al usuario. Si el string ingresado termina con vocal, 
añadir un signo de exclamación al final e imprimir 
el string resultante por pantalla; en caso contrario, 
dejar el string tal cual lo ingresó el usuario e 
imprimirlo por pantalla.  
"""
frase = input("ingrese palabra o frase :")
simbolo = "!"
if frase.endswith(("a", "e", "i", "o", "u")):
    print(f"{frase}!")
else:
    print(frase)


"""
Ejercicio 8 "Nombre con Opciones"
Escribir un programa que solicite al usuario que ingrese 
su nombre y el número 1, 2 o 3 
dependiendo de la opción que desee:  
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.  
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.  
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.  
El programa debe transformar el nombre ingresado de acuerdo 
con la opción seleccionada por el usuario e imprimir el resultado 
por pantalla. 

"""
nombre = input("ingrese su nombre: ")
opcion = int(input(
    "Si quiere su nombre en mayúsculas ingrese 1 \n" 
    "Si quiere su nombre en minúsculas ingrese 2 \n"
    "Si quiere su nombre con la primera letra mayúscula \n"  
    "Indique su opcion: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

"""
Ejercicio 9 "Terremoto"
Escribir un programa que pida al usuario la magnitud de un terremoto, 
clasifique la magnitud en una de las siguientes categorías según 
la escala de Richter e imprima el resultado por pantalla:  
• Menor que 3: "Muy leve" (imperceptible).  
• Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).  
• Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).  
• Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).  
• Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).  
• Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).   
"""
magnitud_terremoto = int(input("la magnitud de un terremoto (entre 0 y 7) : "))
if magnitud_terremoto < 3:
    print("Muy leve (imperceptible)")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud_terremoto >= 7 :
    print("Extremo (puede causar graves daños a gran escala)")

"""
Ejercicio 10 "Estaciones del año"
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
si el usuario se encuentra en otoño, invierno, primavera o verano. 
"""
hemisferio= (input("Ingrese el emisferio donde vive (S,N) : "))
mes= int((input("Ingrese el mes actual (numero) : ")))
dia= int((input("Ingrese el dia actual (numero) : ")))

if hemisferio.upper() == "S":
    if mes == 1 or  mes == 2 or ((mes == 12) and (dia >= 21)) or((mes == 3) and (dia <21)):
        print("Verano")
    elif mes == 4 or  mes == 5 or ((mes == 3) and (dia >= 21)) or ((mes == 6) and (dia < 21)):
        print("Otoño")
    elif mes == 7 or  mes == 8 or ((mes == 6) and (dia >= 21)) or ((mes == 9) and (dia < 21)):
        print("Invierno")
    elif mes == 10 or  mes == 11 or ((mes == 9) and (dia >= 21)) or ((mes == 12) and (dia < 21)):
        print("Primavera")
elif hemisferio.upper()  == "N":
    if mes == 1 or  mes == 2 or ((mes == 12) and (dia >= 21)) or((mes == 3) and (dia <21)):
        print("Invierno")
    elif mes == 4 or  mes == 5 or ((mes == 3) and (dia >= 21)) or ((mes == 6) and (dia < 21)):
        print("Primavera")
    elif mes == 7 or  mes == 8 or ((mes == 6) and (dia >= 21)) or ((mes == 9) and (dia < 21)):
        print("Verano")
    elif mes == 10 or  mes == 11 or ((mes == 9) and (dia >= 21)) or ((mes == 12) and (dia < 21)):
        print("Otoño")
else:
    print ("ingrese S o N")