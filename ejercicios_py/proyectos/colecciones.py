lista = ['Luis', 'Marta', 'Sergio', 'Silvia', 'Javi', 'Javi', 'Patricia']

tupla = ('Luis', 'Marta', 'Sergio', 'Silvia', 'Javi', 'Javi', 'Patricia')

diccionario = {'alumno1': 'Luis', 'alumno2': 'Marta', 'profesor':'Sergio'}

conjunto = {'Luis', 'Marta', 'Sergio', 'Silvia', 'Javi', 'Javi', 'Patricia'}




resultado = (lista [i] == type(str()) for i in range(len(lista)))
tablero = [['' for i in range (3)] for i in range(3)]

print(tablero)

for i in range(len(tablero)):
  for j in  range (len(tablero[i])):
    tablero [i][j] = 'x'
    
print (tablero)