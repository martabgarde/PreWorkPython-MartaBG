''' 2. Ejercicio: Define una función que tome un número y retorne una lista de sus divisores.  '''

def divisores (n):
  divisores_de_n = []
  d = n
  while d > 0:
    if n%d == 0:
      divisores_de_n.append(d)
    d -=1
  return divisores_de_n

numn = int(input('Ingrese un número: '))

print('Los divisores de su número son: ', divisores(numn))