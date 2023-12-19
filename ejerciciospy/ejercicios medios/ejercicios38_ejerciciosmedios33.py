''' 33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.'''
tuplas_ejemplo = [(1, 3, 5), (4, 2, 8), (7, 1, 6)]

def ordenar_por_ultimo_elemento(lista_de_tuplas):
  tuplas_al_reves = []
  for i in lista_de_tuplas:
    tuplas_al_reves.append(i [::-1])
  return tuplas_al_reves
  
print(ordenar_por_ultimo_elemento(tuplas_ejemplo))
