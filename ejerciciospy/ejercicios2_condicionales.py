''' 
Condicionales 
  1. Ejercicio: Dado un número, imprime si es positivo o negativo. 
  
  2. Ejercicio: Dado un número, imprime si es par o impar. 
  
  3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos. 

'''

''' Ejercicio 1'''

x = -9
if x < 0:
  print('Este número es negativo')  
else: print('Este número es positivo')

''' Ejercicio 2'''

z = 10
comprobacion = z%2
if comprobacion == 1:
  print('Este número es impar')
else: print ('Este número es par')
  
''' Ejercicio 3'''
numero1 = 9
numero2 = 15
numero3 = 7

if numero1>numero2:
  if numero1 > numero3:
    print('El número', numero1, 'es el mayor de la lista')
elif numero2>numero3: 
    print('El número', numero2, 'es el mayor de la serie')
else:
  print('El número', numero3, 'es el mayor de la serie')