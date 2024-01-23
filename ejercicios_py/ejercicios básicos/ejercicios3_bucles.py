''' 
Bucles 
  1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for. 
  
  2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while. 
  
  3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
'''

''' ejercicio 1 '''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
  print(numero)
  
''' ejercicio 2 '''

numeropar = 2

while numeropar <= 20:
  print(numeropar)
  numeropar +=2

''' ejercicio 3 '''
suma = 0
primer_numero = 1

while primer_numero <= 100:
  suma += primer_numero
  primer_numero += 1
  
print( 'la suma de tus números es:', suma)