#Tenemos dos listas una con estudiantes y otra con su deudas el estudiante que tenga una deuda mayor a 500 tendra que pagar un valor adicional del 25% de su deuda. 
#Imprimir por pantalla el nombre de la persona y la deuda mas lo que deberia pagar con los intereses

estudiantes=['xavier','Carlos','Luis']
deuda = [950,200,670]

for i in range(len(deuda)):
  a=0
  if deuda[i] > 500 :
    a=deuda[i]+(deuda[i]*0.25)
    print(estudiantes[i],'debera pagar',a)
