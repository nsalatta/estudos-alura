barra = '----------------------'
from IPython.display import clear_output

def limpar_console():
  clear_output(wait=True)

def sair():
  print("Até a próxima")
  exit()

def adição():
  Num1 = float(input('Digite um número: '))
  Num2 = float(input('Digite outro número: '))
  resultado = Num1+Num2
  print(barra)
  if resultado == int(resultado):
    print('O resultado da soma é: ',int(resultado))
  else:
    print('O resultado da soma é: ',resultado)

def subtração():
  Num1 = float(input('Digite um número: '))
  Num2 = float(input('Digite outro número: '))
  resultado = Num1-Num2
  print(barra)
  if resultado == int(resultado):
    print('O resultado da subtração é: ',int(resultado))
  else:
    print('O resultado da subtração é: ',resultado)

def divisão():
  dividendo = float(input('Digite o dividendo: '))
  divisor = float(input('Digite o divisor: '))
  resultado = dividendo/divisor
  print(barra)
  if dividendo == 0:
    print('Dividendo não pode ser 0')
  elif divisor == 0:
    print('Divisor não pode ser 0')
  else:
    print(barra)
    if resultado == int(resultado):
      print('O resultado da divisão é: ',int(resultado))
    else:
      print('O resultado da divisão é: ',resultado)

def multiplicação():
  Num1 = float(input('Digite um número: '))
  Num2 = float(input('Digite outro número: '))
  resultado = Num1*Num2
  print(barra)
  if resultado == int(resultado):
    print('O resultado da multiplicação é: ',int(resultado))
  else:
    print('O resultado da multiplicação é: ',resultado)

def módulo_divisão():
  dividendo = float(input('Digite o dividendo: '))
  divisor = float(input('Digite o divisor: '))
  resultado = dividendo%divisor
  print(barra)
  if dividendo == 0:
    print('Dividendo não pode ser 0')
  elif divisor == 0:
    print('Divisor não pode ser 0')
  else:
    print(barra)
    if resultado == int(resultado):
      print('O módulo da divisão é: ', int(resultado))
    else:
      print('O módulo da divisão é: ', resultado)

def divisão_inteira():
  dividendo = float(input('Digite o dividendo: '))
  divisor = float(input('Digite o divisor: '))
  resultado = dividendo//divisor
  print(barra)
  if dividendo == 0:
    print('Dividendo não pode ser 0')
  elif divisor == 0:
    print('Divisor não pode ser 0')
  else:
    print(barra)
    if resultado == int(resultado):
      print('O módulo da divisão é: ', int(resultado))
    else:
      print('O módulo da divisão é: ', resultado)

def exponenciação():
  Num1 = float(input('Digite um número: '))
  Num2 = float(input('Digite o potencializador: '))
  resultado = Num1**Num2
  print(barra)
  if resultado == int(resultado):
    print('O resultado da exponenciação é: ',int(resultado))
  else:
    print("O resultado da exponenciação é: ",resultado)


while True:
  limpar_console()
  print(barra)
  print('Qual operação irá realizar?\n1 = Adição \n2 = Subtração \n3 = Divisão \n4 = Multiplicação \n5 = Módulo de divisão \n6 = Divisão inteira \n7 = Exponenciação \n8 = Sair')
  Operação = int(input('Digite o número da operação desejada: '))
  print(barra)

  #Operação de adição
  if Operação == 1:
    adição()

  #Operação de subtração
  elif Operação == 2:
    subtração()

  #Operação de divisão
  elif Operação == 3:
    divisão()

  #Operação de multiplicação
  elif Operação == 4:
    multiplicação()

  #Operação de módulo de divisão
  elif Operação == 5:
    módulo_divisão()
    
  #Operação de divisão inteira
  elif Operação == 6:
    divisão_inteira()

  #Operação de exponenciação
  elif Operação == 7:
    exponenciação()

  elif Operação == 8:
    sair()

  #Operação inválida
  else:
    print('Operação inválida')

  if Operação == 1 or Operação == 2 or Operação == 3 or Operação == 4 or Operação == 5 or Operação == 6 or Operação == 7:
    print(barra)
    resposta = input('Deseja realizar outra operação? (Sim/Não):').lower().strip()
    if resposta != 'sim':
      print(barra)
      sair()
  else:
    limpar_console()