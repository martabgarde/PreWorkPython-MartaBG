'''8. Ejercicio: Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3'''
divisores_n = []
def divisores (n):
  b =n
  for _ in range(n):
    if n%b == 0:
     divisores_n.append(b)
    b -=1
  return divisores_n

def numero_perfecto (n):
  divisores(n)
  if sum(divisores_n) - n == n:
    return True
  else:
    return False
  
numn = int(input('Ingrese un número: '))
print(numero_perfecto(numn))    
    