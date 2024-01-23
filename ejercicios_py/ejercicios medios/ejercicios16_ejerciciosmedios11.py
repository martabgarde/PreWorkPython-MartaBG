''' 11. Ejercicio:  Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda). '''
def es_palindromo (palabra):
  palabra = palabra.lower()
  return palabra == palabra[::-1]

palabrita = input('Ingrese una palabra para saber si es un palíndromo: ')
print(es_palindromo(palabrita))