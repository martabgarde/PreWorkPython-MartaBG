def inicializar_partida():
  tablero = [[' ' for i in range(3)] for i in range (3)]
  jugador_actual = 'X'

  return tablero, jugador_actual

def imprimir_tablero(tablero):
  print ('-' * 9)
  for fila in tablero:
    print(' | '.join(fila))
    print('_'* 9)
    
print(imprimir_tablero)