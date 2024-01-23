''' 1. Crea una función para verificar si un número es par o impar y devuelva “El número es par” o “El número es impar” según corresponda. '''
def es_par (numero):
  return numero %2 == 0 
num = int(input('Ingresa un número: ')) 
if es_par (num): 
  print ('Es un número par.')
else:
  print ('Es un número impar')
  
  
  ''' 2. Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado. '''
a = int(input('Ingresa un número: '))
def factorial (a):
    if a == 0 or a == 1:
      return 1
    else:
      resultado = 1
      while a > 1:
          resultado *= a
          a -= 1
      return resultado
    
print ('El factorial de tu número es:', factorial(a))
  
''' 3. Crea una función a la que se le pase un número como argumento, calcule la cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado total de dígitos.'''
  
b = int(input('Ingresa un número: '))
  
def total_digitos (b):
    cadena_numero = str(b)
    longitud = len(cadena_numero)
    return longitud
  
print ('Tú número tiene', total_digitos(b), 'dígitos') 

''' 4. Dada una lista de números, crea una función que devuelva el número máximo de la lista. '''

lista_de_numeros = [6, 9, -4, 90, 123, 5, 7, -78]

def maximo_lista (lista_de_numeros):
  maximo = 0
  for numero in lista_de_numeros:
    if numero > maximo:
      maximo = numero
  return maximo

print ('el número más alto de tu lista es', maximo_lista(lista_de_numeros))

''' 5. Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado.'''
c = 36789
def suma_digitos (c):
  cadena_numero = str(c)
  suma=0
  for numero in cadena_numero:
    suma += int(numero)
  return suma

numc = int(input('Ingrese un número de varios dígitos: '))
print ('La suma de los digitos es', suma_digitos(numc))
    
''' 6. Dados dos números, crea una función para encontrar el mínimo común múltiplo (MCM) de los dos números, que se les pasarán como argumento a la función, y devuelva el MCM.'''

def mcm (d, e):
  if d == 0 or e == 0:
    return 0  
  maximo = max(d,e)
  while True: 
    if maximo % d == 0 and maximo % e == 0:
     return maximo
    else: maximo += 1 
    
num1 = int(input('Ingrese el primer número: '))
num2 = int (input( 'Ingrese el segundo número '))

print('El MCM es: ', mcm (num1, num2) )

''' 7. Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo'''

def base_triangulo (f, g):
  return (f*g)/2
  
numf = int(input('Ingrese la base del triángulo: '))
numg = int(input('Ingrese la altura del triángulo: '))

print (' El área del triángulo es: ', base_triangulo (numf, numg))

''' 8. Crea una función que, dado un número, verifique si un número es positivo, negativo o cero.'''

def numero_natural (h):
  if h < 0:
   return 'negativo'
  elif h == 0:
    return 'es cero'
  else:
    return 'positivo'
  
numh = int(input('Ingrese un número: '))

print ('El número ingresado es', numero_natural(numh))

''' 9. Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra. '''

def cuenta_la_palabra (cadena):
  longitud = len (cadena)
  return longitud

palabrita = input('Ingresa una palabra: ')

print('Tu palabra tiene', cuenta_la_palabra(palabrita), 'letras.')

''' 10. Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto. '''

def valor_absoluto (lista):
  for i in range (len(lista)):
    lista [i] = abs (lista [i])
  return lista 
  
numeros = [7, 9, -9, 10, -67]

print ('El valor absoluto de tus números es: ', valor_absoluto (numeros))

''' 11. Crea una función que, dado un número, verifique si un número es primo. '''

def primo (j):
  
  if j < 2:
    return 'un número que no se considera primo ya que la definición de número primo es un número mayor a 1 que puede ser dividido solo por si mismo y por 1'
  elif j == 2:
    return 'primo'
  else:
    if j%2 == 0:
      return 'compuesto'
    else:
      resto = j//2 + 1
      while resto > 2:
        if j%resto == 0:
          return 'compuesto'
        resto -=1
    return 'primo'
    
numero_aportado = int(input('Ingrese un número: '))
resultado = primo (numero_aportado)

print ('El número es', resultado)

''' 12. Dados dos números, crea una función para encontrar el máximo común divisor (MCD) de esos dos números.'''
def mcd (k, l):
  if k == 0 or l == 0:
    return 0  
  else:
    while k:
      l, k=k, l%k
    return l
  
numk = int(input ('Ingresa el primer número '))
numl = int(input ('Ingresa el segundo número: '))

print ('El MCD de tus dos número es', mcd(numk, numl))
