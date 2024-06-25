# usuario ingresar una serie de números enteros positivos. El programa debe continuar solicitando números hasta que el usuario ingrese un número negativo. 
# Al final, el programa debe mostrar lo siguiente:

# La cantidad total de números ingresados (excluyendo el número negativo).
# La suma de todos los números ingresados. Una cadena de texto que contenga todos los números ingresados, separados por comas.

numero = 1
contador = 0
acumuladorPalabras = ''
acumulador = 0

while numero > 0:
  numero = int(input('ingrese numero'))
  contador +=1
  acumuladorPalabras += str(numero) + ','
  acumulador += numero

print("La cantidad total de numeros ingresados es: ",contador )
print("La suma de todos los numeros ingresados es: ",acumulador)
print("Los numeros ingresados fueron: ",acumuladorPalabras)