#* se entrega una lista con las notas de los estudiantes de 4C para evaluar quienes tienen la mejor nota.
#* se guardaran las mejores notas en otra lista y cuando encuentre a alguien que tenga una nota mayor a 80 imprimira la nota y el indice con un mensaje de felicidades

notas = [35,86,45,99,67]
mejoresNotas=[]
for indice in range(len(notas)):
  if notas[indice] > 80 :
    mejoresNotas.append(notas[indice])
    print("Tu nota es: " + notas[indice] + " y estas en el puesto: " + indice)

