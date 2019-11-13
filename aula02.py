
v1 = input("Digite seu nome e sobrenome: ")
print (v1)
v2 = input('Qual a sua idade?')
if v1 == "Murilo":
    print ('Obrigado, usuario cadastrado')
else:
    print ("Nao encontrei seu cadastro, por favor, refazer operacao")


# Exercicio 1: Faca um programa que peca um numero e imprima esse numero

# v1 = input("Imprima um numero: ")
# print(v1)

# Exercicio 2: Faça um programa que some 3 variáveis

# n1 = 2
# n2 = 3
# n3 = 5

# Soma = v1 + v2 + v3
# print (Soma)


# Exercício 3: Faça um programa que imprima duas variáveis ao mesmo tempo

# Nome = input("Digite seu nome: ")
# Sobrenome = input("Digite seu sobrenome: ")

# print(Nome +' '+Sobrenome)

# Faça um programa que valide uma linguagem
# linguagem = 'python'
# valida = input("Qual a variável?")
# if linguagem == valida:
#     print("Boa sorte")
# else: 
#     print("Desculpe, não é possível prosseguir!")

# Faça um programa que recebe 'F' ou 'M' e mostre Feminino ou Masculino

# Sexo = str(input("Digite o sexo: "))
# Sexo = Sexo.capitalize()

# if Sexo == "F":
#     print ("Feminino")
# elif Sexo == "M":
#     print ("Masculino") 
# else:
#     print ("Sexo Inválido!")

# Faça um programa que peça um valor e mostre na tela se o valor
# é positivo ou negativo

# try:
#     valor = float(input("Digite um número: "))
#     if valor < 0:
#         print ("Valor negativo")
#     elif valor == 0:
#         print ("Valor é zero")
#     else: 
#         valor > 0
# except Exception as e:
#     print ("Desculpe, mas isso não é um número!")

# LISTAS

# lista = ['ameixa','morango','abacaxi','laranja','moto','timao']
# lista2 = [[1,2,3],['carro','moto','bike'],'casa']
# lista3 = [1,2,3,4,5],[6,5,4,3,2,1,],[6,4,3,1,2]

# lista.pop(3) para excluir a terceira posição
# lista.insert(3,'laranja') para incluir laranja na terceira posição
# #lista.append('laranja') para incluir o nome laranja na lista
# lista.sort(reverse=True) para ordenar do maior para o menor
# print(lista3.count(4)) saber a quantidade de vezes que aparece o numero 4
#lista3[0][1]=50 trocar o valor da variável
#print(lista.index('abacaxi')) saber qual a posição da palavra que vc quer

#Exercicios Listas
# Exercicio 1 - Dada a lista ['Corinthians', [1, 2, 3, 4, 5] ,'Palmeiras', 'São Paulo', [10, 11, 12, 13, 14],'Flamengo', 'Vasco']
# print 3 , 13 , vasco 
# print 5, sp, 14
# mudar o valor do 4 para 30
# mudar o valor do 10 para 100
# mudar o valor do 14 para 150
# mudar o valor vasco para bragantino 
# lista = ['Corinthians', [1, 2, 3, 4, 5] ,'Palmeiras', 'São Paulo', [10, 11, 12, 13, 14],'Flamengo', 'Vasco']

# #1
# print(lista[1][2])
# #2
# print(lista[4][3])
# #3
# print(lista[6])
# #4
# print(lista[1][4])
# #5
# print(lista[3])
# #5
# print(lista[4][4])
# #6
# lista[1][3]=30
# print(lista)
# #7
# lista[4][0]=100
# print(lista)
# #8
# lista[4][4]=150
# print(lista)
# #9
# lista[6]='bragantino'
# print(lista)

# TUPLAS
# voce não pode alterar uma tupla depois de criar, mas pode criar novamente com o mesmo nome.
# tupla =(1,2,3,4,6,1,1,1,1,1,1,1,1,1)
# tupla = ('teste')
# print(tupla)

# DICIONARIOS

#dicionario = {'nome':'Murilo', 'sobrenome':'BIazioli', 'idade':'25'}

# print(dicionario)
# print(dicionario['nome'],dicionario['sobrenome'],dicionario['idade'])

#print(dicionario.keys()) para saber quais são as chaves
