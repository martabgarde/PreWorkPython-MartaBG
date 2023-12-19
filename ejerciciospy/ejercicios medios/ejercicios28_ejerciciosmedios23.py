''' 23. Ejercicio:  Define una función que encuentre el elemento más común en una lista. '''

def conteo_elementos (lista):
   elementos = {}
   for elemento in lista:
    if elemento in elementos:
       elementos[elemento] += 1
    else:
      elementos [elemento] = 1
   for elemento in elementos:
     suma = 0
     if elemento > suma:
       suma = elemento
   return suma


lista = [1, 2, 4, 3, 3, 3, 2, 1]
print('El elemento más común es: ', conteo_elementos(lista))