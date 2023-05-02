#SUMA DE 1234 Y 532
numero1 = int(input("Escriba el primer número (1234 ó 532): "))
if int(numero1) == 1234 or int(numero1) == 532:
  #print(int(numero1)) 
  numero2 = int(input("Escriba el segundo número (1234 ó 532): "))
  if int(numero2) == 1234 or int(numero2) == 532:
    #print(int(numero2)) 
    if int(numero1) == int(numero2):
      #print(int(numero1), int(numero2))
      print("Los números son iguales")
    else:
      print("La suma es: ", int(numero1)+int(numero2))
  else:
    print("Debe escribir 1234 ó 532")  
else:
  print("Debe escribir 1234 ó 532")  