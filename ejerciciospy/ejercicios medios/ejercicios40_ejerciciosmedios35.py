''' 35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False'''

def primo (j):
  if j < 2:
    return True
  elif j == 2:
    return True
  else:
    if j%2 == 0:
      return False
    else:
      resto = j//2 + 1
      while resto > 2:
        if j%resto == 0:
          return False
        resto -=1
    return True
    
numero_aportado = int(input('Ingrese un número: '))
resultado = primo (numero_aportado)

print (resultado)
