''' Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos. '''
def suma_digitos (c):
  cadena_numero = str(c)
  suma=0
  for numero in cadena_numero:
    suma += int(numero)
  return suma

numc = int(input('Ingrese un número de varios dígitos: '))
print ('La suma de los digitos es', suma_digitos(numc))