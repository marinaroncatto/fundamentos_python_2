### RESUMO DA SEÇÃO ###
#1. Alguns dos métodos oferecidos por strings são:

#capitalize() – altera todas as letras da string para maiúsculas;
print("Demonstrando o método capitalize():")
print('aBcD'.capitalize())

#center() – centraliza a string no campo de um comprimento conhecido;
print("Demonstrando o método center():")
print('[' + 'alpha'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
print('[' + 'gamma'.center(20, '*') + ']')

#count() – conta as ocorrências de um determinado caractere;
print("Demonstrando o método count():")
frase = "A vida é bela e cheia de surpresas. A vida nos surpreende!"
quantidade = frase.count("vida")

print(f"A palavra 'vida' aparece {quantidade} vezes na frase.")

frase = "banana"
# Conta quantas vezes "na" aparece do índice 2 até o final
quantidade = frase.count("na", 2)

print(quantidade)

#join() – une todos os itens de uma tupla/lista em uma string;
print("Demonstrando o método join():")
print(",".join(["omicron", "pi", "rho"]))

#lower() – converte todas as letras da string para minúsculas;
print("Demonstrando o método lower():")
print("SiGmA=60".lower())

#lstrip() – remove os caracteres em branco do início da string;
print("Demonstrando o método lstrip():")
print("[" + " tau ".lstrip() + "]")
print("www.cisco.com".lstrip("w."))
print("pythoninstitute.org".lstrip(".org"))

#replace() – substitui uma determinada substring com outra;
print("Demonstrando o método replace():")
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
#A variante de três parâmetros de replace() usa o terceiro argumento (um número) para limitar o número de substituições.
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))


#find() - ele procura por uma substring e retorna o índice da primeira ocorrência desta substring
print("Demonstrando o método find():")
print("Eta".find("ta"))
print("Eta".find("mma"))

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))
print('kappa'.find('a', 2)) #O segundo argumento especifica o índice em que a procura será iniciada (ele não precisa caber na string).

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)

#Também existe uma mutação de três parâmetros do método find() o terceiro argumento aponta para o primeiro índice que não será levado em consideração durante a procura (ele é na verdade o limite superior da procura).

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))    


#rfind() – encontra uma substring a partir do fim da string;
print("Demonstrando o método rfind():")
#As versões de um, dois e três parâmetros do método rfind() fazem praticamente o memos de seus equivalentes(aqueles sem o prefixo r), mas iniciam suas buscas a partir do fim da string e não do início (daí o prefixo r, de right (direita, em inglês). 
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))
    
#rstrip() – remove os espaços em branco do final da string;
print("Demonstrando o método rstrip():")
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))
    
#split() – divide a string em uma substring usando um delimitador específico;
print("Demonstrando o método split():")
print("phi       chi\npsi".split())

#strip() – remove os espaços em branco iniciais e finais;
print("Demonstrando o método strip():")
print("[" + "   aleph   ".strip() + "]")

#swapcase() – transforma as letras maiúsculas em minúsculas e vice-versa
print("Demonstrando o método swapcase():")
print("I know that I know nothing.".swapcase())

print()

#title() – transforma a primeira letra de cada palavra em maiúscula;
print("Demonstrando o método title():")
print("I know that I know nothing. Part 1.".title())

print()

#upper() – converte todas as letras de uma string em maiúsculas.
print("Demonstrando o método upper():")
print("I know that I know nothing. Part 2.".upper())

#2. O conteúdo da string pode ser determinado por meio dos métodos a seguir (todos retornam valores Booleanos):

#endswith() – a string termina com uma determinada substring?
print("Demonstrando o método endswith():")
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")
t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta")) 

#isalnum() – a string é composta apenas por letras e dígitos?
print("Demonstrando o método isalnum():")
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

t = 'Six lambdas'
print(t.isalnum())

t = '&Alpha;&beta;&Gamma;&delta;'
print(t.isalnum())

t = '20E1'
print(t.isalnum())

#isalpha() – a string é composta apenas por letras?
print("Demonstrando o método isapha():")
print("Moooo".isalpha())
print('Mu40'.isalpha())

#isdigit() - a string é composta apenas por números/digitos?
print("Demonstrando o método isdigit():")
print('2018'.isdigit())
print("Year2019".isdigit())

#islower() – a string é composta somente por letras minúsculas?
print("Demonstrando o método islower():")
print("Moooo".islower())
print('moooo'.islower())

#isspace() – a string é composta apenas por espaços em branco?
print("Demonstrando o método isspace():")
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

#isupper() – a string é composta apenas por letras maiúsculas?
print("Demonstrando o método isupper():")
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())
    
#startswith() – a string começa com uma substring específica?
print("Demonstrando o método startswith():")
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()






##LAB##

#Sua tarefa é criar sua própria função, que se comporta quase exatamente como o método split() original, ou seja:

#deve aceitar exatamente um argumento, uma string;
#deve retornar uma lista de palavras criadas a partir da string, divididas nos locais em que a string contém espaços em branco;
#se a string estiver vazia, a função deve retornar uma lista vazia;
#seu nome deve ser mysplit()
#Use o modelo no editor. Teste seu código com atenção.

def mysplit(strng):
    # retorna [] se a string estiver vazia ou possuir apenas espaços em branco
    if strng == '' or strng.isspace():
        return [ ]
    # prepara a lista para ser retornada
    lst = []
    # prepara uma palavra para construir palavras subsequentes
    word = ''
    # verifica se estamos dentro de uma palavra atualmente (ou seja, se a string começa com uma palavra)
    inword = not strng[0].isspace()
    # passa por todos os caracteres na string
    for x in strng:
        # se estivermos em uma string no momento...
        if inword:
            # ... e o caractere atual não for um espaço...
            if not x.isspace():
                # ... atualize a palavra atual
                word = word + x
            else:
                # ... caso contrário, atingimos o fim da palavra, então precisamos anexá-la à lista...
                lst.append(word)
                # ... e sinalizar que agora saímos da palavra
                inword = False
        else:
            # se estivermos fora da palavra e tivermos atingido um caractere diferente de espaço em branco...
            if not x.isspace():
                # ... significa que uma nova palavra e que precisamos lembrá-la e...
                inword = True
                # ... armazenar a primeira letra da nova palavra
                word = x
            else:
                pass
    # if we've left the string and there is a non-empty string in the word, we need to update the list
    if inword:
        lst.append(word)
    # return the list to the invoker
    return lst


print(mysplit("Ser ou não ser, eis a questão"))
print(mysplit("Ser ou não ser,eis a questão"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

