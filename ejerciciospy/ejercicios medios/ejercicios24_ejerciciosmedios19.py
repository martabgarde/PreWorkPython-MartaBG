''' 19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False. '''

def comparacion_listas (list1, list2):
  for elemento in list1:
    if elemento in list2:
      return True
  else:
    return False
  
lista_1 = input('Introduce una lista de elementos separados por espacios: ').split()
lista_2 = input('Introduce una lista de elementos separados por espacios: ').split()

print (comparacion_listas(lista_1, lista_2))