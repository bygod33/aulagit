# Faça um programa que leia dois números e informe qual deles é o maior, ou se eles são iguais.

num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo numero: '))

if num1 > num2:
    print(num1,'é maior')
elif num1 == num2:
    print('os numero sao iguais')
else:
    print(num2,'é maior')
