#AREA Y VOLUMEN DEL CILINDRO
#v= (pi*(radio**2))*altura
#a= (2*pi(radio))*altura+(2*pi)*(radio**2) ó 2*pi(radio)(altura+radio)
print("Calulemos juntos el área y el volúmen de un cilindro")
radio = input("Ingrese el valor del radio del cilindro: ")
altura = input("Ingrese el valor de la altura del cilindro: ")
pi= float(3.14159265358979323846)
volumen = (float(pi)* (float(radio)**2))*float(altura)
area = (2*float(pi))*float(radio)*(float(radio)+float(altura))
print("El volúmen del cilindro es: " + str(volumen))
print("El área del cilindro es: " + str(area))
