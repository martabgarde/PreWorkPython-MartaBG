''' 16. Ejercicio:  Define una función que tome una lista de números y retorne el número más grande de la lista '''

def maximo_lista (lista):
  for numero in lista:
    n = 0
    if numero > n:
      n = numero
  return numero

lista_numeros = [int(x) for x in input('Introduce una lista de números separados por espacios: ').split()]
print('El número más alto de su lista es: ', maximo_lista(lista_numeros))