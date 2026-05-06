#AULA COMPLETA: NUMEROS EM PYTHON

"""  ""
1 - Tipos númericos
2 - conversão de tipos
3 - Hierarquia
4 - Operação matemática
5 - coerção de tipos
6 - vericação de tipos
7 - entrada de dados
"""  ""
############################
# PASSO 01 - TIPOS NÚMERICOS
############################
#int -> números inteiros
#float -> números com casas decimais
#complex -> números complexos (usado em matemática/ engenharia)

print("======= TIPOS NÚMERICOS ======")

#EXEMPLO 01 - NUMERO INTEIRO

#ciramos uma variável chamada "numero_inteiro"
numero_inteiro = 10

#mostramos o valor
print ("Valor:", numero_inteiro)

#Type() mostra qual é o tipo da variável
print("Tipo:",type(numero_inteiro) )

print("--------------------------------------")

# EXEMPLO 02 - NUMERO DECIMAL

#Float é um número com ponto decimal
numero_decimal = 3.14

print ("Valor:", numero_decimal)
print ("Tipo:", type(numero_decimal))

print("---------------------------------")

#EXEMPLO 03 - NÚMEROS COMPLEXOS

#Um número complexo possui duas partes:
#Parte real (numero normal)
#Parte Imaginaria (multiplicada por j)

#Estrutura Geral:
# número = a + bj

# a = parte real
# b = parte Imaginaria
# j = unidadde Imaginaria 

numero_complexo = 2 + 3j

print("Valor:", numero_complexo)
print("Tipo:", type(numero_complexo))

print("---------------------------------")
