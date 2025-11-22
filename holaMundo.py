"""Ejercicio 1 hola mundo"""
print ("hola mundo")

"""Ejercicio 2 Saludo"""
nombre = input ("ingresa tu nombre:")
print(f"Hola {nombre}, ¡que tengas un buen día!")

"""
Ejercicio 3 Presentación
U.D.: ) Crear un programa que pida al usuario su nombre, apellido, edad 
y lugar de residencia e imprima por pantalla una oración con los datos ingresados. 
"""
nombre = input ("ingresa tu Nombre : ")
apellido = input ("ingresa tus apellidos:")
edad = input ("ingresa tu edad:") 
nacionalidad = input ("ingresa tu nacionalidad:")
print(f"soy {nombre} {apellido}, tengo {edad}Años y vivo en {nacionalidad}")

"""
Ejercicio 4 Circulo
Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
su perímetro.  
"""
radio = float (input("ingrese el valor del radio:"))
pi= 3.14
perimetro = 2 * radio * pi
print(f"el perimetro de la circunferencia es: {perimetro}")

"""
Ejercicio 5 Candidad de Segundos
Crear un programa que pida al usuario una cantidad de segundos e 
imprima por pantalla a cuántas horas equivale.
"""
segundos = int (input("ingresa un valor entero de segundos:"))
horas= segundos / 3600
print(f"los segundos consignados corresponde a : {horas}hs")

"""
Ejercicio 6 la table del....
Crear un programa que pida al usuario un número e imprima por 
pantalla la tabla de multiplicar de dicho número. 
"""
multiplo = float (input("ingresa un valor:"))
print(f"{multiplo} x 1 = {multiplo * 1}")
print(f"{multiplo} x 2 = {multiplo * 2}")
print(f"{multiplo} x 3 = {multiplo * 3}")
print(f"{multiplo} x 4 = {multiplo * 4}")
print(f"{multiplo} x 5 = {multiplo * 5}")
print(f"{multiplo} x 6 = {multiplo * 6}")
print(f"{multiplo} x 7 = {multiplo * 7}")
print(f"{multiplo} x 8 = {multiplo * 8}")
print(f"{multiplo} x 9 = {multiplo * 9}")
print(f"{multiplo} x 10 = {multiplo * 10}")

"""
Ejercicio 7 suma resta ,ultiplicacion y división
 Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 
"""
primer_numero = int (input("ingresa un valor entero distinto de cero:"))
segundo_numero = int (input("ingresa un valor entero distinto de cero:"))
suma = primer_numero + segundo_numero 
resta = primer_numero - segundo_numero 
multiplicacion = primer_numero * segundo_numero 
division = primer_numero / segundo_numero 
print(f"La suma de los valores ingresados es = {suma} ")
print(f"La resta de los valores ingresados es = {resta} ")
print(f"La multiplicación de los valores ingresados es = {multiplicacion} ")
print(f"La división de los valores ingresados es = {float (division)} ")

"""
Ejercicio 8 IMC
Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
de masa corporal.
"""
peso = float (input("ingresa tu peso en Kilos:"))
altura = float (input("ingresa tu altura en Metros:"))
imc = peso / (altura ** 2)
print(f"si indice de masa corporal es = {float(imc)}")

"""
Ejercicio 9 Celsius a Fahrenheit
 Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
"""
temp_celsius = float (input("ingresa la temperatura en ºC :"))
temp_fahrenheit = (9/5) * temp_celsius + 32
print(f"El equivalente es = {float(temp_fahrenheit )}ºF")

"""
Ejercicio 10 suma resta ,ultiplicacion y división
Crear un programa que pida al usuario  3 números e imprima por 
pantalla el promedio de dichos números.
"""
primer_numero = int (input("ingresa un valor entero distinto de cero:"))
segundo_numero = int (input("ingresa un valor entero distinto de cero:"))
tercer_numero = int (input("ingresa un valor entero distinto de cero:"))
promedio = (primer_numero + segundo_numero + tercer_numero) / 3
print(f"El promedio de los 3 valores ingresado es = {float (promedio)} ")