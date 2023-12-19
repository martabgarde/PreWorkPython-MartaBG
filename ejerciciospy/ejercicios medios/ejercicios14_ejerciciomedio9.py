''' 9. Ejercicio: Define una función que reciba un número y retorne su representación en binario. '''

def binario (n):
  return bin(n).replace('0b','')

numn = int(input('Ingrese un número: '))
print('Su número en binario es: ', binario(numn))