''' 14. Ejercicio:  Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n. '''
 
n = int(input('Introduce un número natural: '))
def palabras_largas (lista):
   resultado = []
   maximo = n
   for palabra in lista:
     longitud = len(palabra)
     if longitud > maximo:
       resultado.append(palabra)
   return resultado
 
lista_palabras = input('Introduce una lista de palabras: ').split()
print('Las palabras que tienen más de', n, 'caracteres son:', palabras_largas(lista_palabras))