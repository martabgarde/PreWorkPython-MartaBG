''' 22. Ejercicio:  Define una función que reciba una lista de números y retorne la suma acumulada de los números '''

def suma_acumulada (lista):
  suma =0
  for elemento in lista:
    suma += elemento
  resultado_2 = suma 
  return resultado_2
  

lista_numeros = [int(x) for x in input('Introduce una lista de números separados por espacios: ').split()]
print('La suma acumulada de su lista es: ', suma_acumulada(lista_numeros))