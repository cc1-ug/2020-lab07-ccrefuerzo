import random

def displayAlbum(lista):
  for i, x in enumerate(lista):
    print(x, end = ' - ')
    if (i + 1) % 10 == 0:
      print()

def main():
  lista = list(range(1, 101))
  contador = 0

  displayAlbum(lista)

  while True:
    x = random.randint(1, 100)
    print('Numero generado: ' + str(x))
    if lista[x - 1] == 'X':
      print('Ya tengo esta estampita')
    else:
      lista[x - 1] = 'X'
      contador += 1

    displayAlbum(lista)
    if contador == 100:
      print('Album lleno')
      break;
    input()

main()