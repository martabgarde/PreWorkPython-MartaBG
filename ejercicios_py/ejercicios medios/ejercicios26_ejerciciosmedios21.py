''' 21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene '''

def numeros_letras (cadena):
  letras = []
  numeros = []
  for elemento in cadena:
   if elemento.isalpha():
      letras.append(elemento)
   elif cadena.isalnum():
      numeros.append(elemento)
  return letras, numeros

cadena_1 = input('Introduce una cadena: ')
print(numeros_letras(cadena_1))