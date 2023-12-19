''' 10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).  '''
list1 = []
list2 = []
def interseccion (list1, list2):
  resultado = []
  for elemento in list1:
    if elemento in list2:
      resultado.append(elemento)
  return resultado

lista = input('Ingrese la primera lista: ')
listb = input('Ingrese la seguna: ')

print('Los elementos comunes de su lista son:', interseccion (lista, listb))

def intersection(list1, list2):      
   return list(set(list1) & set(list2))   

print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))