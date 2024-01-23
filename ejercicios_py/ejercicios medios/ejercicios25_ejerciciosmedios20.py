''' 20. Ejercicio:  Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso. '''

def lista_inversa (lista):
  return lista [::-1]

lista_numeros = [int(x) for x in input('Introduce una lista de números separados por espacios: ').split()]
    
print(lista_inversa(lista_numeros))