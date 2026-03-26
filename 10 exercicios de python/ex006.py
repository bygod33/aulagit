# Faça um programa que leia a idade de uma pessoa e informe se ela pode entrar no evento, considerando entrada permitida apenas para maiores de 18 anos.


idade = int(input('Qual sua idade? '))

if idade > 18:
    print('Pode entrar')
else:
    print('Não pode entrar')
