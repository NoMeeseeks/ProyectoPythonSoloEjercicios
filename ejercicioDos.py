print("Ejercicio numero 2")
print("Leer la siguiente lista que contiene numero y palabras, cuando encuentre un numero sumar el valor del numero y cuando sea una palabra sumara 1")
cosasGuardadas = ["Pelota de futbol",10,"Cargador de telefono",2000,"Avion de juguete",45968,56,True]
contadorPalabras=0
contadorNumeros=0
for i in cosasGuardadas:
    if type(i) == str:
        contadorPalabras += 1
    elif type(i) == int:
        contadorNumeros += i
print("Las palabras en la lista son: ", contadorPalabras)
print("Los numeros en la lista son: ", contadorNumeros)