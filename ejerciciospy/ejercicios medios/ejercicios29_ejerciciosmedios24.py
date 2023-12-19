''' 24. Ejercicio:  Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10. '''

def tabla_de_multiplicar (n):
  tablita = []
  for i in range(1,11):
    resultado = n * i
    tablita.append(resultado)
  return tablita

numn = int(input('Introduce un número del 1 al 10: '))
print('La tabla de multiplicar del número que ha introducido es: ', tabla_de_multiplicar(numn))