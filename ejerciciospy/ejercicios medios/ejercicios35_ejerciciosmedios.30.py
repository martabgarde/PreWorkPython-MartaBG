''' 30. Ejercicio:  Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista. '''

def cadena_larga (list1):
  longitudes = {}
  for palabra in list1:
       longitudes [palabra] = len(palabra)
  for larga in longitudes:
    suma = 0
    if longitudes[larga] > suma:
      suma = larga
  return suma

lista = ['patata', 'salchicha', 'cochinillo']
print('La cadena más larga de su lista es: ', cadena_larga(lista))