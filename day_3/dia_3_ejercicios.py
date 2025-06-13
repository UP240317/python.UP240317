#ejericio 1
edad = 25                
#ejercicio 2
altura = 1.75            
#ejercicio 3
numero_complejo = 3 + 4j # variable de número complejo
#ejercicio 4
print("vamos a calcular el area de un triangulo")
base = float(input("introduzca la base del triangulo: "))
altura=float(input("introduzca altura del triangulo: "))
area= base*altura

print("el area del triangulo es: ",area)
#ejercicio 5
print("vamos a calcular el perimetro de un triangulo")
lado_a= float(input("introduzca el lado a: "))
lado_b=float(input("introduzca el lado b: "))
lado_c=float(input("introduzca el lado c: "))
perimetro=lado_a+lado_b+lado_c

print("el perimetro de tu triangulo es: ", perimetro)
#ejercicio 6
print("vamos a calcular el area y elperimetro de un rectangulo")
longitud = float(input("Introduce la longitud del rectángulo: "))
ancho = float(input("Introduce el ancho del rectángulo: "))

area_2 = longitud*ancho
perimetro_2 = 2 * (longitud + ancho)

print("El área del rectángulo es:", area_2)
print("El perímetro del rectángulo es:", perimetro_2)
#ejercicio 7
pi=3.14
print("vamos a calcular el area y circunferencia de un circulo")
radio=float(input("introduce la radio del circulo"))
area_circulo=pi*radio**2
circunferencia=2*pi*radio

print("el area de tu circulo es: ", area_circulo)
print("la circunferencia de tu circulo es: ",circunferencia)
#ejercicio 8
print("vamos a calcular el punto de intercepcion de los ejes x and y")
x1=2
z2=-2
intercepcion_x=(0-z2)/x1
intercepcion_y=z2
print("pendiente",x1)
print("Interseccion con eje x: (", intercepcion_x, ", 0 )")
print("Interseccion con eje y: ( 0 ,", intercepcion_y, ")")

#ejercicio 9
import math
x1, y1 = 2, 2
x2, y2 = 6, 10
m2 = (y2 - y1) / (x2 - x1)
distancia= math.sqrt((x2 - x1)*2 + (y2 - y1)**2)

print("\n=== Entre puntos (2,2) y (6,10) ===")
print("Pendiente entre puntos:", m2)
print("Distancia Euclidiana:",distancia)

#ejercicio 10
print("=== Ejercicio 8 ===")
x1 = 2        # This is the slope (m)
z2 = -2       # This is the y-intercept (b)

m1 = x1
b1 = z2

print(f"Pendiente (m1): {m1}")
print(f"Intersección con eje y (b1): {b1}")

print("\n=== Ejercicio 9 ===")
x2_1, y2_1 = 2, 2
x2_2, y2_2 = 6, 10

m2 = (y2_2 - y2_1) / (x2_2 - x2_1)

b2 = y2_1 - m2 * x2_1

print(f"Pendiente (m2): {m2}")
print(f"Intersección con eje y (b2): {b2}")

print("\n=== Comparación ===")

if m1 == m2 and b1 == b2:
    print("Las rectas son IGUALES.")
elif m1 == m2:
    print("Las rectas son PARALELAS.")
else:
    print("Las rectas son DIFERENTES (ni iguales ni paralelas).")

#ejercicio 11

def quadratic(x):
    return x**2 + 6*x + 9

print("x\t y")
for x in range(-10, 5):
    y = quadratic(x)
    print(f"{x}\t {y}")

x_zero = -3
y_zero = quadratic(x_zero)
print(f"\nCuando x = {x_zero}, y = {y_zero} (-> y = 0)")

# ejercicio 12

palabra1 = "python"
palabra2 = "dragon"

largo1 = len(palabra1)
largo2 = len(palabra2)

print("Length of 'python':", largo1)
print("Length of 'dragon':", largo2)

print("Is 'python' longer than 'dragon'? ->", largo1 > largo2)  

#ejercicio 13
palabra1 = "python"
palabra2 = "dragon"

resultado = ('on' in palabra1) and ('on' in palabra2)

print("¿'on' está en ambas palabras 'python' y 'dragon'? ->", resultado)

#ejercicio 14
oracion = "Espero que este curso no esté lleno de jargon"
print("1. ¿La palabra 'jargon' está en la oración?:", "jargon" in oracion)

#ejercicio 15
print("2. ¿'on' está en 'python' y en 'dragon'?:", ("on" in "python") and ("on" in "dragon"))

#ejercicio 16
longitud = len("python")
como_flotante = float(longitud)
como_cadena = str(como_flotante)
print("3. Longitud de 'python' como cadena flotante:", como_cadena)

#ejercicio 17
numero = 12
es_par = numero % 2 == 0
print("4. ¿El número", numero, "es par?:", es_par)

#ejercicio 18
resultado = (7 // 3 == int(2.7))
print("5. ¿7 // 3 es igual a int(2.7)?:", resultado)

#ejercicio 19
tipos_iguales = (type('10') == type(10))
print("6. ¿El tipo de '10' es igual al tipo de 10?:", tipos_iguales)

#ejercicio 20
try:
    comparacion = int('9.8') == 10
except ValueError:
    comparacion = "Error: no se puede convertir '9.8' directamente a entero"
print("7.", comparacion)

#ejercicio 21
horas = float(input("8. Introduce las horas trabajadas: "))
tarifa = float(input("Introduce la tarifa por hora: "))
pago = horas * tarifa
print("Tu ganancia semanal es:", pago)

#ejercicio 22
anios = int(input("9. Introduce cuántos años has vivido: "))
segundos = anios * 365 * 24 * 60 * 60
print("Has vivido aproximadamente", segundos, "segundos.")

#ejercicio 23
print("10. Tabla:")
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
