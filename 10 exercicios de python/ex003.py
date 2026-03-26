# Faça um programa que leia o salário de uma pessoa e informe se ela recebe acima de 2000 reais ou 2000 reais ou menos.

salario = int(input('Qual seu salário?: '))

if salario == 2000:
    print('Seu salário é 2000')
elif salario > 2000:
    print('Seu salário é maior que 2000')
else:
    print('Seu salário é menor que 2000')