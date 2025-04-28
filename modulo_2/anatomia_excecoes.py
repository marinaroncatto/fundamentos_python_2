###  RESUMO DA SEÇÃO ###

######### 1. Não é possível incluir mais de uma ramificação except anônima (sem nome) após as nomeadas.

# Código que é sempre executado sem problemas.
#:
#try:
#    :
#    # Código arriscado.
#    :
#except Except_1:
#    # O gerenciamento de crise acontece aqui.
#except Except_2:
#    # É aqui que salvamos o mundo.
#except:
#    # Todos os outros problemas se encaixam aqui.
#:
# De volta ao normal.
#:
 
##### 2. Todas as exceções predefinidas formam uma hierarquia, ou seja, algumas são mais gerais (BaseException é a mais geral), enquanto outras são mais ou menos concretas (por ex., IndexError é mais concreta que LookupError).
#Não se deve colocar exceções mais concretas antes das mais gerais dentro da mesma sequência de ramificação except . Por exemplo, você pode fazer isso:

#try:
    # Código arriscado.
#except IndexError:
    # Lidando com listas maltratadas
#except LookupError:
    # Lidando com outras consultas incorretas
 
#mas não faça isso (a não ser que tenha certeza absoluta em querer que parte do seu código seja inútil)

#try:
    # Código arriscado.
#except LookupError:
    # Lidando com outras consultas incorretas
#except IndexError:
#     Você nunca chegará até aqui
 

######3. A instrução Python raise ExceptionName pode gerar uma exceção sob demanda. A mesma instrução, mas sem ExceptionName, pode ser usada apenas dentro da ramificação except e gera a mesma exceção que está sendo processada no momento.

print("Ex raise")

def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except ArithmeticError:
    print("O que aconteceu? Um erro?")

print("FIM.")

print("Ex raise 2")

def bad_fun(n):
    try:
        return n / 0
    except:
        print("Consegui de novo!")
        raise


try:
    bad_fun(0)
except ArithmeticError:
    print("Entendi!")

print("FIM.")
    

#######4. A instrução Python assert expression avalia a expressão e gera a exceção AssertError quando a expressão for igual a zero, uma string vazia ou None. Ela pode ser usada para proteger partes críticas de seu código contra dados devastadores.

print("Ex: assert")
import math

x = float(input("Digite um número: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)
