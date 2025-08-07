'''
print('olá mundo,esse é o meu primeiro script em python')
print(30*"-", "concatenando texto",30*"-")
# comentario de linha 
nome ="cris"
print("nome: ",nome)

idade ="22" 
print("idade: ",idade)

cidade ="taguatinga" 
print("cidade",cidade)

nascimento ="22/08/91"
print("nascimento", nascimento)

#tipos de variaveis 

nome ="demeris"
idade = 25
altura = 1.70
activo = True

print("o tipo de variavel nome é: ", type(nome))
print("o tipo de variavel idade é",type(idade))
print("o tipo de variavel altura é",type(altura))

#operadores
num1 = 2 
num2 = 3
soma = num1 + num2 
divi = num1 / num2 # divisao comum 
divisao_inteira = num1 // num2 #divisao inteira 
multi =num1 * num2
expo = num1 ** num2 
sub = num1 - num2
resto = num1 %2
0
print("Resultado da soma",num1, '+', num2, "é:", soma)
print("resultado da divisão" ,num1, "/", num2, "é", divi)
print("resultado da multiplicação",num1, "*", num2, "é,", multi)
print("resultado da subtração" ,num1, "-", num2, "é,", sub)

print(30* '-', 'operadores de comparação' ,30*'-')
#operadores de comparação 
num1 > num2
num1 < num2 
num1 == num2 
num1 >= num2
num1 <= num2 
num1 != num2

ano = 2025
print("ano atual",ano)
ano += 1 
print('ano acrecido e +1', ano)
ano -= 1
print ( 'Ano decrecido de -1' ,ano)

# operadores lógicos 
# AND, OR, NOT

print()
print(30* '-', 'entrada de dados' ,30*'-')

nome_usuario = input("digite o seu nome: ")
print('seja bem-vindo ao sistema python', nome_usuario)

ano_nascimento = input("Digite seu ano de nascimento")
print(type(ano_nascimento))
# conveertendo para inteiro 
ano_nascimento = int(ano_nascimento)
print(type(ano_nascimento))

n1 = 10
n2 = 20

print("A Soma é:", n1+n2, type(n1), float(n2))
'''
saudacao = input('Digite seu nome: ') 
cpf = input('Digiteseu CPF: ')
telefone = input('Digite seu telefone: ')

print(20* '-', ' Dados pessoais', 20* '-')
print('Nome:', saudacao)
print('CPF:' , cpf, '|Telefone:', telefone)
print(50*'-')
