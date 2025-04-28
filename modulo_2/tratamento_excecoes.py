###  RESUMO DA SEÇÃO ###

#1. Uma exceção é um evento durante a execução do programa que é causado por uma situação anormal. A exceção deve ser processada para evitar o encerramento do programa. A parte do seu código que é suspeita de ser a origem da exceção deve ser colocada dentro do bloco try .
#Quando a exceção é gerada, a execução do código não é encerrada; em vez disso, a execução pula para a ramificação except . Este é o local em que deve ocorrer o tratamento da exceção. O esquema geral para essa construção é o seguinte:

# Código que é sempre executado sem problemas.

#try:
#    :
#    # Código arriscado
#    :
#except:
#    :
#    # O gerenciamento de crise acontece aqui
#    :
#:
# De volta ao normal
#:
print("Ex1: try except simples")
first_number = int(input("Digite o primeiro número: "))
second_number = int(input("Digite o segundo número: "))

try:
    print(first_number / second_number)
except:
    print("Não é possível realizar esta operação.")

print("FIM.")
    
 
#2. Se precisar processar mais de uma exceção originada na mesma ramificação try , é possível incluir mais de uma ramificação except , mas é necessário identificá-las com nomes de exceção distintos, como a seguir:

# Código que é sempre executado sem problemas.

#try:
#    :
#    # Código arriscado
#    :
#except Except_1:
#    # O gerenciamento de crise acontece aqui
#except Except_2:
#    # É aqui que salvamos o mundo.
#:
# De volta ao normal

print("Ex2: try com mais de um except")

try:
    x = int(input("Digite um número: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
except ValueError:
    print("Digite um número inteiro.")
except:
    print("Oh não, algo deu errado...")

print("FIM.")
    
 
#No máximo, será executada uma das ramificações except , nenhuma das ramificações será executada quando a exceção gerada não corresponder a nenhuma das exceções especificadas.


#3. Não é possível incluir mais de uma ramificação except anônima (sem nome) após as nomeadas.

# Código que é sempre executado sem problemas.

#try:
#    :
#    # Código arriscado
#    :
#except Except_1:
#    # O gerenciamento de crise acontece aqui
#except Except_2:
#    # É aqui que salvamos o mundo.
#except:
#    # Todos os outros problemas se encaixam aqui.
# De volta ao normal.

print("Ex3 - except anonimo deve ser o último")
try:
    x = int(input("Digite um número: "))
    y = 1 / x
    print(y)
except ValueError:
    print("Digite um número inteiro.")
except:
    print("Oh não, algo deu errado...")

print("FIM.")
    





