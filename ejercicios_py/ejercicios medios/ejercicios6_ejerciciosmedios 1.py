''' 1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci.  '''

def fibonacci (n):
  secuencia_de_fibonacci = [1, 1, ]
  suma = 0
  a = 1
  b = 1
  for _ in range (n ):
    a, b = secuencia_de_fibonacci[-2], secuencia_de_fibonacci[-1]
    suma = a + b
    secuencia_de_fibonacci.append(suma)
  return secuencia_de_fibonacci

numn = int(input('Ingrese el número ed dígitos que quiera saber de la secuencia de fibonacci: '))

print (fibonacci(numn))