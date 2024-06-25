# Ingrese una palabra imprimala n cantidad de veces que usted quiera pero al imprimir la palabra tiene que mostrar el numero de la palabra que se esta imprimiendo y en los multiplos de 5 cambie la palabra por cualquier otra palabra
# ej: 1 hola 2 hola 3 hola 4 hola

palabra=input('Ingrese alguna palabra: ')
for i in range(1,100):
  print(palabra + " " + i)
  if i %5==0:
    print('Es multiplo de 5')