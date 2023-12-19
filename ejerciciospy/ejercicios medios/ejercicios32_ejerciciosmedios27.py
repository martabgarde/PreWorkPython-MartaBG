''' 27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados'''

def lista_sin_duplicados (list1):
  resultado = []
  for elemento in list1:
    if elemento not in resultado:
      resultado.append(elemento)
  return resultado
      
lista = input('Introduzca una lista de números separados por espacios: ')
print('Su lista sin repetidos es: ', lista_sin_duplicados(lista))

def eliminar_duplicados(lista):      
   return list(set(lista))   
 
print(eliminar_duplicados([1, 2, 2, 3, 4, 4])) 