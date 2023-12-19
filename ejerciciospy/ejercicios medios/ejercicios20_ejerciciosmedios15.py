'''15. Ejercicio:  Define una función que tome un número y calcule su serie de Fibonacci. '''

def fibonacci_de_n (n):
  secuencia_de_fibonacci_n = []
  a = 0
  b = 1
  for _ in range (n):
    secuencia_de_fibonacci_n.append(a)
    temp = a
    a = b
    b = temp + b
  return secuencia_de_fibonacci_n

numn = int(input('Ingrese un número: '))

print (fibonacci_de_n(numn))