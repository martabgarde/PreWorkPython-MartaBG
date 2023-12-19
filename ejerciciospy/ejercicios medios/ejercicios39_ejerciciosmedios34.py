'''34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.'''

vocales ='aeiouAEIOUáéíóúÁÉÍÓÚ'

def cuantas_vocales (cadena):
  vocales_in_cadena = {}
  for vocal in cadena:
    if vocal in vocales:
     if vocal in vocales_in_cadena:
       vocales_in_cadena[vocal] +=1
     else:
       vocales_in_cadena[vocal] = 1
  for i in vocales_in_cadena:
         cantidad = sum (vocales_in_cadena.values())
  return cantidad

print(cuantas_vocales('patata'))
    