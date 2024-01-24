def suma (x, y):
  resultado = x + y
  return resultado

def resta (x, y):
  resultado = x - y
  return resultado

def multiplicación (x, y):
  resultado = x * y
  return resultado

def división (x, y):
  resultado = x / y
  return resultado


def calculadora ():
  print ('¡Bienvenido a tu calculadora')
  x = float(input('Introduce el primer número'))
  operación = input('Introduce qué operación quieres realizar ')
  y = float(input('Introduce el segundo número'))
  if operación == 'suma':
    return suma (x, y)
  if operación == 'resta':
    return resta (x, y)
  if operación == 'multiplicación' or 'multiplicacion':
    return multiplicación (x,y)
  if operación == 'división' or 'division':
    return división (x,y)
  else:
    print ('¡Operación invalida! Por favor, inténtalo de nuevo')
    
print (calculadora)

  
    
    
  
  