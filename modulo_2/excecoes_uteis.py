## RESUMO DA SEÇÃO ##

#1. Algumas exceções abstratas integradas ao Python são:

# -- ArithmeticError --
#Local: BaseException ← Exception ← ArithmeticError
#Descrição: uma exceção abstrata, incluindo todas as exceções causadas por operações aritméticas como divisão por zero ou o domínio inválido de um argumento

# -- BaseException --
#Local: BaseException
#Descrição: a mais geral (abstrata) de todas as exceções do Python, todas as outras exceções estão inclusas nessa; pode-se dizer que as duas ramificaçõesexcept a seguir são equivalentes: except: e except BaseException:.

# -- LookupError --
#Local: BaseException ← Exception ← LookupError
#Descrição: uma exceção abstrata, incluindo todas as exceções causadas por erros resultantes de referências inválidas a diferentes coleções (listas, dicionários, tuplas, etc.)

#2. Algumas exceções concretas integradas ao Python são:

#-- AssertionError --
#Local: BaseException ← Exception ← AssertionError
#Descrição: uma exceção concreta gerada pela instrução assert quando o argumento for False, None, 0 ou uma string vazia

print("Ex: AsserionError")
from math import tan, radians
angle = int(input('Enter integral angle in degrees: '))
 
# devemos assegurar que o ângulo seja != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))

#-- ImportError --
#Local: BaseException ← Exception ← StandardError ← ImportError
#Descrição: uma exceção concreta, gerada quando ocorre uma falha em uma operação de importação

print("Ex: ImportError")
# Uma dessas importações não funcionará, sabe dizer qual delas?
 
try:
    import math
    import time
    import abracadabra
 
except:
    print('Ocorreu uma falha em uma de suas importações.')

#-- IndexError --

#Local: BaseException ← Exception ← LookupError ← IndexError
#Descrição: uma exceção concreta gerada quando se tenta acessar o elemento não existente de uma sequência (por ex., o elemento de uma lista)

print("Ex: IndexError")
# O código mostra uma forma extravagante
# de sair do loop.
 
the_list = [1, 2, 3, 4, 5]
ix = 0
do_it = True
 
while do_it:
    try:
        print(the_list[ix])
        ix += 1
    except IndexError:
        do_it = False
 
print('Concluído')
    
#-- KeyboardInterrupt --
#Local: BaseException ← KeyboardInterrupt
#Descrição: uma exceção concreta gerada quando o usuário usa um atalho do teclado criado para finalizar a execução de um programa (Ctrl-C na maioria dos S.O.s); se o processamento dessa exceção não levar à finalização do programa, o programa continuará sua execução.
#Observação: essa exceção não é derivada da classe Exception . Execute o programa em IDLE.

# Este código não pode ser finalizado
# pressionando Ctrl-C.
 
from time import sleep
 
seconds = 0
 
while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("Não faça isso!")


#-- KeyError --
#Local: BaseException ← Exception ← LookupError ← KeyError
#Descrição: uma exceção concreta gerada quando você tenta acessar um elemento não existente em uma coleção (por ex., o elemento de um dicionário)

# Como usar o dicionário incorretamente
# e como resolver isso?
 
dictionary = {'a': 'b', 'b': 'c', 'c': 'd'}
ch = 'a'
 
try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print('A chave não existe:', ch)
        
#-- MemoryError --
#Local: BaseException ← Exception ← MemoryError
#Descrição: uma exceção concreta, gerada quando não é possível completar uma operação por falta de memória livre.


# Este código causa a exceção MemoryError.
# Aviso: a execução desse código pode afetar seu SO.
# Não o execute em ambientes de produção!
 
string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('Isso não tem graça!')
    
#-- OverflowError --
#Local: BaseException ← Exception ← ArithmeticError ← OverflowError
#Descrição: uma exceção concreta, gerada quando uma operação produz um número grande demais para ser armazenado com sucesso

# O código resulta em valores
# sucessivos de exp(k), k = 1, 2, 4, 8, 16, ...
 
from math import exp
 
ex = 1
 
try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('O número é grande demais.')
    

## LAB ##

#A função deve ser capaz de:

#aceitar três argumentos: um prompt, um limite inferior aceitável e um limite superior aceitável;
#se o usuário inserir uma string que não seja um valor inteiro, a função deve gerar a mensagem Erro: valor inválido e pedir para o usuário digitar o valor novamente;
#se o usuário inserir um número fora do intervalo especificado, a função deve exibir a mensagem Erro: o valor não está dentro do intervalo permitido (mín..máx) e pedir ao usuário para digitar o valor novamente;
#se o valor inserido for válido, retorná-lo como resultado.

def read_int(prompt, min, max):
    ok = False
    while not ok: #enquanto o ok for falso (not inverte)
        try:
            value = int(input(prompt))
            ok = True
        except ValueError:
            print("Erro: valor inválido")
        if ok:
            ok = value >= min and value <= max
        if not ok:
            print("Erro: o valor está fora do intervalo permitido (" + str(min) + ".." + str(max) + ")")
    return value;


v = read_int("Digite um número de -10 a 10: ", -10, 10)

print("O número é:", v)

