"""Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como 
resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.
"""

meses = {
  1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}
while True:
  valor = int(input())

  if valor in meses:
    mes_extenso = meses[valor]
    print (mes_extenso)
    break
  else:
    print ("Valor inválido, selecione entre 1-12 e tente novamente.")