''' 3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.'''
def elementos_unicos(lista):
  unicos_elementos = set()
  for repeticion in lista:
      unicos_elementos.add(repeticion)
  return unicos_elementos
    
listn = input('Introduce una lista de números separado por comas: ')
mi_lista = [int(x) for x in listn.split(',')]
resultado = elementos_unicos(mi_lista)
print('Los elementos únicos de tu lista son: ', resultado)


def unicos(lista):     
  return list(set(lista))  

print(unicos([1, 2, 2, 3, 4, 4])) 