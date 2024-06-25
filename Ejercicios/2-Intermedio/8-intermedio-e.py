# Considere la secuencia de números triangulares, cuyo nombre refleja su ley de formación
# Escriba un algoritmo en seudo-código que indique si un número natural t, ingresado por teclado, es triangular.
# Rúbrica: identificación de piso en operación (5 puntos), cálculo de usados (5 puntos), control de pisos construidos (5 puntos), validar s es triangular (5 puntos), algoritmo estructurado (5 puntos)
# http://blog.espol.edu.ec/ccpg1001/1eva_iiit2003_t2-numeros-triangulares/


pisos=5
resultado = (pisos * (pisos+1)) // 2
for i in range(resultado):
    if(i > 0 and i <= pisos):
        print(i*"*", " Este piso es el numero : ",i)
print(resultado)