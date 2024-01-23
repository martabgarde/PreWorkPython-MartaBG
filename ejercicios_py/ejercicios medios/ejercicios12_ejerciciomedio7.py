''' 7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena. '''

mayusculas = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ'
minusculas = 'abcdefghijklmnñopqrstuvwxyzáéíóú'

def mayus_minus (cadena):
  mayusculas_en_palabra = ''
  minusculas_en_palabra = ''
  for letra in cadena:
    if letra in mayusculas:
      mayusculas_en_palabra += letra 
    else:
      minusculas_en_palabra += letra
  return minusculas_en_palabra, mayusculas_en_palabra
  

palabra = input ('Introduzca una palabra con mayúsculas y minúsculas: ')
mayusculas, minusculas = mayus_minus(palabra)  
print ('Las mayusculas son:', mayusculas, 'y las minúsculas son:', minusculas)

def contar_mayus (cadena):
  return sum(1 for letra in cadena if letra in mayusculas), sum(1 for letra in cadena if letra in minusculas)
mayusculas_contadas, minusculas_contadas = contar_mayus(palabra)
print ('Hay', mayusculas_contadas, 'mayúsculas en su palabra y ', minusculas_contadas, 'minúsculas.')

  
    
  
    