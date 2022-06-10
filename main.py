#01 Faça um programa em Pyton que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.

print('\t----Tabuada----')
numero = int(input('Informe o numero para ver a tabuada: '))

print('\nTabuada de', numero, ':')

for i in range(1, 11):
  print(numero, 'X', i, '=', (numero * i))
print("\n")

#------------------------------------------------------#
#Praticando Nº2
print('\t----Cálculo do novo salário----')
salario_atual = float(input('Informe o salário atual: '))

if (salario_atual<500):
  salario_novo=salario_atual+(salario_atual*0.15)
  print('Salario com reajuste = ', salario_novo)

if ((salario_atual>=500) and (salario_atual <=1000)):
  salario_novo=salario_atual+(salario_atual*0.10)
  print('Salario com reajuste = ', salario_novo)

if (salario_atual>1000):
  salario_novo=salario_atual+(salario_atual*0.05)
  print('Salario com reajuste = ', salario_novo)
print("\n")

#03 Escreva um programa que mostre todos os números entre 5 e 100 que são divisíveis por 7, mas não são múltiplos de 5. Os números obtidos devem ser impressos em sequência.

print('\t--Números entre 5 e 100 que são divisíveis por 7--')
for num in range(5, 100):
  if (num % 7 == 0 and num % 5 != 0):
    print(num)
print("\n")

#----------------------------------------------------------#
#Praticando Nº4 

print('\t----Soma de 1 até o valor digitado----')
soma_numeros = 0
numero = int(input("Por favor, insira um número: "))
for i in range(1, numero + 1, 1):
  soma_numeros += i
print("A soma é = ", soma_numeros)
print("\n")

#----------------------------------------------------------#
#05 Faça um programa que recebendo um valor inteiro, informe se o número é positivo, negativo, ou neutro.

print('\t----A dança dos números----')
x = int(input("Informe um número para brincar: "))
if x < 0:
        print('É um número negativo ')
elif x == 0:
        print('É um número neutro')
elif x > 0:
        print('É um número positivo')
print("\n") 

#----------------------------------------------------------#
#06 Crie um algoritmo que receba um número, conte o número total de dígitos e mostre o resultado. Por exemplo, se o número é 2021, então a saída deve ser 4.

print('\t----Contagem dos dígitos----')
digitos = int(input("Digite um número para contar seus dígitos: "))
contador = 0
while digitos != 0:
  digitos //= 10
  contador += 1
print("Total de dígitos = ", contador)
print("\n")
