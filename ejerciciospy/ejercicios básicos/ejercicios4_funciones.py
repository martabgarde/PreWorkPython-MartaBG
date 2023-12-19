''' 
Funciones
  1. Ejercicio: Define una función que tome dos números y retorne su suma. 
  
  2. Ejercicio: Define una función que tome un número y retorne su factorial. 
  
  3. Ejercicio: Define una función que tome un número y determine si es primo. 
  
  4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos. 
  
  5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa. 
'''

''' ejercicio 1'''

def suma (a, b):
  return a + b

resultado_a = suma (4, 8)

print('El resultado de tu suma es:', resultado_a)


''' ejercicio 2'''

def factorial (a):
  
  if a == 0 or a == 1:
    return 1
  else:
    resultado = 1
    while a > 1:
         resultado *= a
         a -= 1
    return resultado
  
resultado_factorial = factorial (0)
print ('El factorial de tu número es', resultado_factorial)

''' ejercicio 3 '''

def primo (a):
  
  if a < 2:
    return 'un número que no se considera primo ya que la definición de número primo es un número mayor a 1 que puede ser dividido solo por si mismo y por 1'
  elif a == 2:
    return 'primo'
  else:
    if a%2 == 0:
      return 'compuesto'
    else:
      resto = a//2 + 1
      while resto > 2:
        if a%resto == 0:
          return 'compuesto'
        resto -=1
    return 'primo'
    
numero_aportado = 35
resultado = primo (numero_aportado)

print ('El número', numero_aportado, 'es', resultado)

''' ejercicio 4 '''

a = [3, 2, 5, 7, 8, 8, 0]

def suma_num (a):
  b = 0
  for numero in a:
    b += numero
  return b

resultado_b = suma_num (a)
print ('La suma es', resultado_b)

''' ejercicio 5 '''

def inversion_cadena (cadena):
  return cadena [::-1]

cadena = inversion_cadena('Hola mundo!')
print (cadena)