''' 26. Ejercicio:  Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas '''

lista = []
listb = []

def elementos_no_repetidos (list1, list2):
  resultado = []
  for elemento in list1:
    if elemento not in list2:
     resultado.append(elemento)
  for elemento in list2:
      if elemento not in list1:
        resultado.append(elemento)
  return resultado
  
lista = input('Ingrese la primera lista: ')
listb = input('Ingrese la seguna: ')

print('Los elementos no comunes de su lista son:', elementos_no_repetidos(lista, listb))
        