''' 25. Ejercicio:  Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena. '''

def conteo_caracteres (cadena):
  caracteres = {}
  for caracter in cadena:
    if caracter in caracteres:
       caracteres[caracter] += 1
    else:
      caracteres [caracter] = 1
  return caracteres
  
cadena_introducida = input('Introduzca una palabra: ')
print('Los caracteres de su palabra son: ', conteo_caracteres(cadena_introducida))
