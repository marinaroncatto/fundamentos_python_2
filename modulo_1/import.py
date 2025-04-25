## importando módulos comletos##
print("Ex: 1")
import math

print(math.sin(math.pi/2))
#output 1.0


print("Ex: 2")
import math


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))#sobrescreve o valor de pi


## importando módulos especídficos ##

#as entidades listadas (e somente essas) serão importadas do módulo indicado;
#os nomes das entidades importadas podem ser acessados sem qualificação.

print("Ex: 3 - import seletivo")

from math import sin, pi

print(sin(pi/2))


print("Ex: 4 - import seletivo")
#executar a importação; os símbolos importados substituem suas definições anteriores dentro do namespace

from math import sin, pi

print(sin(pi / 2))

pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))

#RESUMO #

#1. Se desejar importar um módulo inteiro, use a instrução import nome_módulo. É possível importar mais de um módulo por vez por meio de uma lista separada por vírgulas. Por exemplo:

#import mod1
#import mod2, mod3, mod4
   
#a última forma não é recomendada por motivos estilísticos; além disso, é melhor e mais elegante expressar a mesma intenção de maneira mais detalhada e explícita, como:

#import mod2
#import mod3
#import mod4

##########################

#2. Se um módulo é importado da maneira acima e você desejar acessar qualquer uma de suas entidades, será necessário usar notação de ponto como prefixo do nome da entidade. Por exemplo:

#import my_module
   
#result = my_module.my_function(my_module.my_data)
 
#O snippet (fragmento) utiliza duas entidades provenientes do módulo my_module: uma função chamada my_function() e uma variável chamada my_data. Ambos os nomes devem possuir o prefixo my_module. Nenhum dos nomes de entidades importadas apresentarão conflito com os nomes idênticos existentes no namespace de seu código.


##############################

#3. É possível não só importar um módulo inteiro, como também importar apenas entidades individuais. Neste caso, as entidades importadas não devem ter o prefixo quando usadas. Por exemplo:

#from module import my_function, my_data
  
#result = my_function(my_data)
 
#A maneira acima, embora tentadora, não é recomendada devido ao risco de conflitos com os nomes derivados da importação do namespace do código.

#################################

#4. A forma mais geral da instrução acima permite que você importe todas as entidades oferecidas por um módulo:


#from my_module import *
  
#result = my_function(my_data)
 
#Observação: não é recomendado usar a variação dessa importação devido aos mesmos motivos do método anterior (aqui, o risco de conflitos de nomenclatura é ainda maior).

###############################

#5. É possível alterar o nome da entidade importada "em tempo real" ao usar a frase as de import. Por exemplo:

#from module import my_function as fun, my_data as dat
  
#result = fun(dat)

