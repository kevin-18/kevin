nombre=input("¿como te llamas? ")
apellido=input("¿cual es tu apéllido? ")
edad=input("¿que edad tienes? ")
direccion=input("¿donde estas ahora? ")
space=" "
print("Hola soy"+space+nombre+space+apellido+space+"tengo"+space+edad+space+"años"+space+"y ahora estoy en"+space+direccion)
if edad>"18":
	print("eres mayor de edad")
else:
    print("eres menor de edad")
