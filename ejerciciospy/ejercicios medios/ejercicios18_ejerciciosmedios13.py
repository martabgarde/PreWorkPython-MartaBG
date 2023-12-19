''' 13. Ejercicio:  Define una función que tome una lista y retorne la lista ordenada en orden ascendente. '''

def lista_ascendente (lista):
  lista_ordenada = sorted(lista)
  return lista_ordenada

lista_dada = input('Introduce una lista de números: ')
print ('Su lista ordenada es: ', lista_ascendente(lista_dada))
