'''' 32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.'''

def cadena_inversa (cadena):    
    return cadena [::-1]
  
  
cadena = ('filete', 'salchicha', 'perro')
print(cadena_inversa(cadena))


def cadena_inversa_dos (cadena):
  palabras_inversas = []
  for palabra in cadena:
    palabra = palabra [::-1]
    palabras_inversas.append(palabra)
  return palabras_inversas
  
print (cadena_inversa_dos(cadena))