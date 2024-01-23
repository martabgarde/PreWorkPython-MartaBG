''' 17. Ejercicio:  Define una función que reciba un número y retorne la suma de sus dígitos al cubo. '''

def suma_al_cubo (n):
  cadena_numero = str(n)
  suma = 0
  for numero in cadena_numero:
    suma += int(numero)
  cubo = suma * suma * suma
  return cubo

numn = int(input('Ingrese un número de varios digitos: '))

print('El resultado es: ',suma_al_cubo(numn))