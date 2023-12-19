''' Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena. '''
vocales = 'aeiouAEIOU'
def vocales_en_palabra (cadena):
  vocales_en_palabra = ""
  for letra in cadena:
    if letra in vocales:
      vocales_en_palabra += letra
  return vocales_en_palabra
   
palabra = input('Ingrese una palabra: ')  

print ('Las vocales de su palabra son: ', vocales_en_palabra(palabra))

def contar_vocales(cadena):     
  return sum(1 for letra in cadena if letra.lower() in 'aeiou')  

print(contar_vocales('Hola Mundo')) 