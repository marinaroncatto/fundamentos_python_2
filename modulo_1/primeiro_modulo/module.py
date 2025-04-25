#!/usr/bin/env python3

#a linha que começa com #! possui diversos nomes: pode ser chamado de shabang, shebang, hashbang, poundbang ou até mesmo hashpling.
#Do ponto de vista do Python, é apenas um comentário pois começa com #. Para SOs Unix e similares (incluindo MacOS), essa linha instrui
#o SO como executar o conteúdo do arquivo (em outras palavras, qual programa precisa ser iniciado para interpretar o texto).
#Em alguns ambientes (especialmente aqueles conectados a servidores da Web),
#a ausência dessa linha causará problemas;
 
#"" module.py - an example of a Python module ""

#uma string (talvez multilinhas) colocada antes de quaisquer instruções do módulo (incluindo importações)
#é chamada de doc-string e deve explicar brevemente o propósito e conteúdo do módulo;

 
__counter = 0
 
 
def suml(the_list):
  global __counter
  __counter += 1
  the_sum = 0
  for element in the_list:
   the_sum += element
  return the_sum
 
 
def prodl(the_list):
  global __counter
  __counter += 1
  prod = 1
  for element in the_list:
   prod *= element
  return prod


#as funções definidas no módulo (suml() e prodl()) estão disponíveis para importação;
 
 
if __name__ == "__main__":
  print("I prefer to be a module, but I can do some tests for you.")
  my_list = [i+1 for i in range(5)]
  print(suml(my_list) == 15)
  print(prodl(my_list) == 120)


#usamos a variável __name__ para detectar quando o arquivo é executado de maneira
#independente e aproveitou a oportunidade para executar alguns testes simples.
