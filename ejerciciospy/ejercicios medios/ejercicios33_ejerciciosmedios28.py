''' 28. Ejercicio:  Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número. '''

def cuadrado_muchísimos (n):
  numeros_pares = []
  cuadrados = []
  for i in range(0, n+1):
    if i%2 == 0:
      numeros_pares.append(i)
  for cuadrado in numeros_pares:
    cuadrados.append(cuadrado**2)
  return sum(cuadrados)

numn = int(input('Ingrese un número positivo: '))
print('El resultado de su número es: ', cuadrado_muchísimos(numn))