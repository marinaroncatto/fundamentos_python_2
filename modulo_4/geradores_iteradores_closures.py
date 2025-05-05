## RESUMO DA SEÇÃO ##

#1. Um iterador é um objeto de uma classe que fornece pelo menos dois métodos (sem contar o construtor):
#__iter__() é chamado uma vez quando o iterador é criado é retorna o próprio objeto do iterador;
#__next__() é chamado para fornecer o valor da próxima iteração e gera a exceção StopIteration quando a iteração chegar ao fim.

class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")		
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)


#2. A instrução yield pode ser usada apenas dentro das funções. A instrução yield suspende a execução da função e faz com que a função retorne o argumento de yield como resultado. Tal função não pode ser chamada da maneira comum, seu único objetivo é ser usada como um gerador (ou seja, em um contexto que requer uma série de valores, como um loop for).

def fun(n):
    for i in range(n):
        yield i
 
 
for v in fun(5):
    print(v)

#3. Uma expressão condicional é uma expressão criada usando o operador if-else. Por exemplo:


print(True if 0 >= 0 else False)
 

#apresenta o resultado True.


#4. Uma compreensão de lista torna-se um gerador quando é usada entre parênteses (usada entre colchetes, produz uma lista comum). Por exemplo:

for x in (el * 2 for el in range(5)):
    print(x)

#apresenta o resultado 02468.

for v in [1 if x % 2 == 0 else 0 for x in range(10)]: #compreensão de lista
    print(v, end=" ")
print()
 
for v in (1 if x % 2 == 0 else 0 for x in range(10)): #gerador
    print(v, end=" ")
print()

#4. Uma função lambda é uma ferramenta para criação de funções anônimas. Por exemplo:


def foo(x, f):
    return f(x)
 
print(foo(9, lambda x: x ** 0.5))
 

#apresenta o resultado 3.0.


#5. A função map(fun, list) cria uma cópia de um argumento list e aplica a função fun a todos os seus elementos, retornando um gerador que fornece um novo conteúdo de lista, elemento por elemento. Por exemplo:


short_list = ['mython', 'python', 'fell', 'on', 'the', 'floor']
new_list = list(map(lambda s: s.title(), short_list))
print(new_list)
 

#apresenta o resultado ['Mython', 'Python', 'Fell', 'On', 'The', 'Floor'].


#6. A função filter(fun, list) cria uma cópia dos elementos de list, que faz com que a função fun retorne True. O resultado da função é um gerador que fornece o novo elemento de conteúdo de lista, elemento por elemento. Por exemplo:


short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list)
 

#apresenta o resultado ['Python', 'Monty'].


#7. Uma closure é uma técnica que permite o armazenamento de valores apesar do fato que o contexto em que foram criados não existe mais. Por exemplo:


def tag(tg):
    tg2 = tg
    tg2 = tg[0] + '/' + tg[1:]
 
    def inner(str):
        return tg + str + tg2
    return inner
 
 
b_tag = tag('<b>')
print(b_tag('Monty Python'))
 

#apresenta o resultado <b>Monty Python</b>


# OBSERVAÇÃO #

#PEP 8, o Guia de Estilo do Código Python, recomenda que lambdas não devem ser atribuídos a variáveis e sim definidos como funções.
#Isto significa que é melhor usar a instrução def e evitar usar uma instrução de atribuição que vincula uma expressão lambda a um identificador. Analise o código abaixo:


# Recomendado:
def f(x): return 3*x
 
 
# Não recomendado:
f = lambda x: 3*x
 

#Vincular lambdas a identificadores geralmente duplica a funcionalidade da instrução def. O uso de instruções def, por outro lado, gera mais linhas de código.
#É importante entender que a realidade muitas vezes criar seus próprios cenários, que não necessariamente seguem convenções ou recomendações formais. Segui-las ou não vai depender de diversos fatores: suas preferências, outras convenções adotadas, guias internos da sua empresa, compatibilidade com código existente, etc. Sempre tenha isso em mente.

