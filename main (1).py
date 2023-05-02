
menu= int(input("Ingrese la opcíon a ejecutar: "))
if menu == 1:
  print('Ejecutando Ejercicio 1 "Calcule el área de un triángulo"')
  print('')
  exec(open("1_area_triangulo.py").read())
if menu == 2:
  print('Ejecutando Ejercicio 2 "Introducir dos números por teclado y sumarlos"')
  print('')
  exec(open("2_Suma.py").read())
if menu == 3:
  print('Ejecutando Ejercicio 3 "introducir un número por teclado y visualizar el número elevado al cuadrado"')
  print('')
  exec(open("3_elevado_al_cuadrado.py").read())
if menu == 4:
  print('Ejecutando Ejercicio 4 "Imprima por pantalla la suma de 1234 y 532"')
  print('')
  exec(open("4_Suma_de.py").read())
if menu == 5:
  print('Ejecutando Ejercicio 5 "Imprima por pantalla la resta de 1234 y 532"')
  print('')
  exec(open("5_Resta_de.py").read())
if menu == 6:
  print('Ejecutando Ejercicio 6 "Imprima por pantalla la multiplicación de 1234 y 532"')
  print('')
  exec(open("6_Multiplicacion_de.py").read())
if menu == 7:
  print('Ejecutando Ejercicio 7 "Imprima por pantalla la división de 1234 entre 532"')
  print('')
  exec(open("7_Division_de.py").read())
if menu == 8:
  print('Ejecutando Ejercicio 8 "Imprima por pantalla el módulo de 1234 entre 532"')
  print('')
  exec(open("8_Modulo_de.py").read())
if menu == 9:
  print('Ejecutando Ejercicio 9 "Convierta de euros a dólares"')
  print('')
  exec(open("9_Conversor_euros.py").read())
if menu == 10:
  print('Ejecutando Ejercicio 10 "Calcule el área de un rectángulo"')
  print('')
  exec(open("10_area_rectangulo.py").read())
if menu == 11:
  print('Ejecutando Ejercicio 11 "Pida el lado de un cuadrado y muestre el valor del área y del perímetro."')
  print('')
  exec(open("11_area_y_perimetro_cuadrado.py").read())
if menu == 12:
  print('Ejecutando Ejercicio 12 "Algoritmo que determine el área y el volumen de un cilindro"')
  print('')
  exec(open("12_area_y_volumen_cilindro.py").read())
if menu == 13:
  print('Ejecutando Ejercicio 13 "Algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma, y el área (Pi*R) ^2 del círculo inscrito"')
  print('')
  exec(open("13_area_y_longitud_circunferencia.py").read())
if menu == 14:
  print('Ejecutando Ejercicio 14 "Calcular el promedio de tres números introducidos por teclado"')
  print('')
  exec(open("14_Promedio_numeros.py").read())

if menu < 1 or menu > 14:
  print('Opción de menú no válido')