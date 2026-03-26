# Faça um programa que leia a quantidade de faltas de um aluno e informe se ele está dentro do limite ou acima do limite, considerando limite de 10 faltas.

faltas = int(input('quantas faltas voce tem?'))

if faltas == 10:
    print('está no limite')
elif faltas > 10:
    print('está acima do limite')
else:
    print('está dentro do limite')