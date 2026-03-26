# Faça um programa que leia o nome de um aluno e sua nota, informando se ele foi aprovado ou reprovado.

nome = input('Qual seu nome? ')
nota = float(input('Qual sua nota? '))

print(nome, nota)

if nota >= 7:
    print('Aprovado')
else:
    print('Reprovado')
