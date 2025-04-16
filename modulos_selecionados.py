## função dir() ##

#A função retorna uma lista em ordem alfabética com todos os nomes de entidade disponíveis no módulo
print("Ex 1")
import math
  
for name in dir(math):
  print(name, end="\t")

#Observação: se o nome do módulo recebeu um alias, será necessário usar o alias, não o nome original.

#É possível executar o comando diretamente na IDLE
#import math
#dir(math)

# exemplos de uso módulo math #

print("\nEx math")

from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

print()    
print("Ex math 2")
# e = euler
#exp = exponenciação
#log = logaritmo

from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

## Aleatóriedade ##

#Outro módulo digno de menção é random.
#Ele oferece alguns mecanismos que permite que você trabalhe com números pseudoaleatórios.

#A função mais geral, chamada random() (não deve ser confundida com o nome de módulo) produz um valor flutuante x no intervalo (0.0, 1.0) - em outras palavras: (0.0 <= x < 1.0).

print()
print("Ex random()")

from random import random

for i in range(5):
    print(random())
    
#A função seed() é capaz de definir o seed do gerador diretamente. Mostraremos duas variantes:

#seed() - define o seed com o horário atual;
#seed(int_value) - define o seed com o valor inteiro int_value.

print()
print("Função seed()")

from random import random, seed

seed(0)

for i in range(5):
    print(random())

#Devido ao fato do seed sempre ser definido com o mesmo valor, a sequência dos valores gerado parecerá sempre igual.

#Se deseja retornar valores inteiros aleatórios:

#randrange(end)
#randrange(beg, end)
#randrange(beg, end, step)
#randint(left, right)
#As primeiras três chamadas irão gerar um número inteiro retirado (pseudoaleatoriamente) do intervalo (respectivamente):

#range(end)
#range(beg, end)
#range(beg, end, step)

#Esse programa de exemplo produzirá uma linha que consiste em três zeros e um zero ou um número 1 na quarta posição.

print()
print("Ex randrange e randint 0 e 1")
from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

print()
print("Ex randint 1 a 10")
from random import randint

for i in range(10):
    print(randint(1, 10), end=',')

#Como podemos ver, essa não é uma boa ferramenta para gerar número em uma loteria. Felizmente, existe uma solução melhor do que criar seu próprio código para verificar a exclusividade dos números "sorteados".
#É uma função com nome bem sugestivo - choice:

#choice(sequence)
#sample(sequence, elements_to_choose)

#A primeira variante escolhe um elemento "aleatório" da sequência de entrada e o retorna.
#Já a segunda monta uma lista (uma amostra) composta do elemento elements_to_choose "sorteado" da sequência inserida.
#Em outras palavras, a função escolhe alguns dos elementos de entrada e retorna uma lista com a escolha. Os elementos na amostra são colocados em ordem aleatória. Observação: elements_to_choose não pode ser maior do que o comprimento da sequência de entrada.

print()
print("Função choice() e sample()")

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

### módulo platform ###

#certas vezes, pode ser que você queira saber mais - por exemplo, o nome do SO do Python e algumas características que descrevem o hardware em que o SO está sendo executado.
#Existe um módulo que oferece os meios para saber onde você está e quais componentes estão trabalhando para você. O módulo é platform. Mostraremos algumas das funções que ele oferece.
#O módulo platform permite acessar os dados dos bastidores da plataforma, por exemplo, informações sobre hardware, sistema operacional e versão do interpretador.

#platform(aliased = False, terse = False)

#aliased → quando definida como True (ou qualquer valor diferente de zero) pode fazer com que a função apresente os nomes das camadas básicas subjacentes alternativas em vez das comuns;
#terse quando definida como True (ou qualquer valor diferente de zero) pode fazer com que a função apresente uma forma mais abreviada do resultado (se possível)

print()
print("Função platform()")
from platform import platform
 
print(platform())
print(platform(1))
print(platform(0, 1))

#Às vezes você só quer saber o nome genérico do processador que está executando seu SO, juntamente com o Python e seu código: a função machine() fornece essas informações. Como em outras vezes, a função retorna uma string.

print()
print("Função machine()")

from platform import machine
 
print(machine())


#A função processor() retorna uma string que contém o nome real do processador (se possível).

from platform import processor
 
print(processor())

#A função chamada system() retorna o nome genérico do SO como string.

print()
print("Função system()")
from platform import system
 
print(system())

#A função version() fornece a versão do SO como uma string.
print()
print("Função version()") 

from platform import version
 
print(version())

#As funções python_implementation e python_version_tuple
#Se precisar saber qual a versão do Python que está executando o seu código, você pode confirmar essa informação por meio de diversas funções dedicadas - aqui temos duas delas:

#python_implementation() → retorna uma string que indica a implementação do Python (espere CPython neste caso, a não ser que você decida usar implementações alternativas do Python)
#python_version_tuple() → retorna uma tupla de três elementos, preenchida com:

#a parte principal da versão do Python;
#a parte menor;
#o número de nível do patch.
print()
print("Função python_implementation() e python_version_tuple")

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)

