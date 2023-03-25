# Crie um programa que recebe um valor inteiro referente a um determinado ano.
# Imprima na tela se o ano informado é bissexto ou não (para simplificar, você pode utilizar apenas a informação
# de que o ano é divisível por 4 ou não).

def leapYear():
  year = int(input("Digite um ano "))

  if (year % 4 == 0):
    print("Esse ano é bissexto")
  else:
    print("Esse não é um ano bissexto")

leapYear()
