''' 12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”.  '''

numeros = range(1, 50)
def FizzBuzz (numeros):
  resultado = []
  for numero in numeros:
    if numero%3 == 0 and numero%5 == 0:
      resultado.append('FizzBuzz')
    elif numero%3 == 0:
      resultado.append('Fizz')
    elif numero%5 == 0:
      resultado.append('Buzz')
    else:
      resultado.append(numero)
  return resultado
print(FizzBuzz(numeros))
    