''' 31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos. '''

def es_primo (j):
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

def n_numeros_primos (n):
  if n == 1:
    return [2]
  if n == 2:
    return [2, 3]
  numeros_primos = [ ]
  i = 2
  while len(numeros_primos) < n:
   if es_primo(i):
    numeros_primos.append(i)
   i +=1 
  return numeros_primos

print(n_numeros_primos(10))
   

