#PROMEDIO DE TRES NUMEROS
print("Introduzca el primer número: ")
num1 = input()
print("Introduzca el segundo número: ")
num2 = input()
print("Introduzca el tercer número: ")
num3 = input()
prom= (float(num1), float(num2), float(num3))
mean= sum(prom)  / len(prom)
print("El promedio de los numeros es: ", mean)
