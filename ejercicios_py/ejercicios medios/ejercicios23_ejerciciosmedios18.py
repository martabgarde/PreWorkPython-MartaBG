''' 18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.'''

def penultimo_max (lista):
   n = 0
   segundo_maximo = 0
   for numero in lista:
    if numero > n:
      segundo_maximo = n
      n = numero
    elif numero > segundo_maximo:
      segundo_maximo = numero
   return segundo_maximo
    
lista_numeros = [int(x) for x in input('Introduce una lista de números separados por espacios: ').split()]
print('El segundo número más alto de su lista es: ', penultimo_max(lista_numeros))