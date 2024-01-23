''' 29. Ejercicio:  Define una función que reciba una lista de números y retorne el promedio de los números en la lista. '''

def media (list1):
  suma =0
  for i in list1:
    suma += i
    f = suma/ len(list1)
  return f

lista = [float (x) for x in input('Ingrese una lista de números separados por espacios: ').split()]
print('La media de los números de su lista es: ', media(lista))