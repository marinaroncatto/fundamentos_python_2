#Dê uma olhada no Exemplo 1. A função len() usada para strings, retorna vários caracteres contidos nos argumentos. O resultado do snippet (fragmento) é 2.
#Qualquer string pode ser vazia. Portanto, seu comprimento é 0 assim como no Exemplo 2.
#não se esqueça que a barra invertida (\) usada como caractere de escape não é incluída no comprimento total da string. O resultado do código no Exemplo 3, portanto, é 3.

# Example 1

print("Função len() - conta caracteres")
word = 'by'
print(len(word))


# Example 2

empty = ''
print(len(empty))


# Example 3

i_am = 'I\'m'
print(len(i_am))

#Agora é um ótimo momento para mostrar outra maneira de especificar strings dentro do código-fonte Python. Observe que a sintaxe que você já conhece não permitirá usar uma string que ocupe mais de uma linha de texto.

print("Strings multilinhas")

multiline = '''Line #1
Line #2'''

print(len(multiline))

#O resultado do snippet (fragmento) é 15.
#Conte os caracteres com atenção. O resultado está ou não correto? Pode parecer que sim à primeira vista, mas quando contar os caracteres, verá que não está.
#Line #1 contém sete caracteres. Duas linhas dessas representam 14 caracteres. Por acaso perdemos um caractere? Onde? Como?
#Não perdemos.
#O caractere ausente apenas está invisível – ele é um espaço em branco. Ele está localizado entre as duas linhas de texto.
#Ele é representado por: \n.

#Strings multilinhas também podem ser delimitadas por aspas triplas, assim como a maneira seguir:

print("Multilinhas com aspas duplas")
multiline = """Line #1
Line #2"""

print(len(multiline))

print("Strings concatenadas e replicadas")
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

#ord()
#Se desejar saber o valor do ponto de código de um caractere ASCII/UNICODE específico, você poderá usar uma função chamada ord() (como em ordinal).
#A função precisa de uma string de um caractere como argumento – ignorar esse requerimento causará uma exceção TypeError e retornará um número que representa o ponto de código do argumento.

print("Demonstrando a função ord()")

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))

#chr()
#Se você souber o ponto de código (número) e desejar obter o caractere correspondente, é possível usar a função chr().
#A função lê um ponto de código e retorna seu caractere.
#Chamá-la com um argumento inválido (por ex., um ponto de código negativo ou inválido) causa exceções ValueError ou TypeError .

print("Demonstrando a função chr()")

print(chr(97))
print(chr(945))

#Indexação
#Dissemos anteriormente que as strings do Python são sequências. Chegou a hora de mostrar o que isso quer dizer.
#Strings não são listas, mas podem ser tratadas como tal em diversos casos específicos.
#Por exemplo, caso deseje acessar qualquer caractere de uma string, é possível fazê-lo por meio de indexação, como no exemplo a seguir. Execute o programa:

print("Indexando strings")

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()

#Iteração
#A iteração por meio de strings também funciona. Observe o exemplo abaixo:

print("Iterating through a string.")

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()

#2.2.5 Slices
#Além disso, tudo o que você sabe sobre slices(fatias) ainda pode ser usado.
#Reunimos alguns exemplos mostrando como as fatias funcionam no universo das strings. Observe o código no editor, analise-o e em seguida execute-o.

print("Slices em strings")

alpha = "abdefg"

print(alpha[1:3]) #Pegue os caracteres do índice 1 até o índice 3 (mas não inclui o 3).
print(alpha[3:]) #Pegue do índice 3 até o final da string.
print(alpha[:3]) #Pegue do início (índice 0) até o índice 3 (excluindo o 3).
print(alpha[3:-2]) #Pegue do índice 3 até o índice -2 (excluindo o -2).
#Lembrando: -2 conta a partir do fim da string, então -2 é 'f'.
print(alpha[-3:4]) #Pegue do índice -3 (que é 'e') até o índice 4 (sem incluir o 4).
print(alpha[::2]) # Pegue a string inteira, pulando de 2 em 2 caracteres.
print(alpha[1::2]) #Comece do índice 1 e vá até o fim, pulando de 2 em 2.


#O operador in e not in
#O operador in não irá surpreender ninguém quando aplicado a strings: ele simplesmente verifica se o argumento à sua esquerda (uma string) pode ser encontrado em qualquer lugar do argumento à direita (outra string).
#O resultado da verificação é simplesmente True ou False.

print("Operador in com string")

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)

print("Operador not in com string")

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)

#Strings em Python são imutáveis
#Isto significa principalmente que a semelhança entre strings e listas é limitada. Nem tudo que pode ser feito com uma lista pode ser feito com uma string.
#A primeira diferença importante é que não é permitido usar a instrução del para remover algo de uma string.
#A única coisa que pode ser feita com del e uma string é remover a string por completo.
#As strings Python não possuem o método append() , não é possível expandi-las de maneira alguma.
#sem o método append() , o método insert() também é ilegal:

#A única consequência é que você precisa se lembrar dela e implementá-las de uma maneira ligeiramente diferente em seu código. Observe o exemplo no editor.

print("ex de como expandir uma string no python")

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)

### Operações em strings: continuação ###

#min()
#Agora que você aprender que strings são sequências, podemos mostrar alguns recursos menos óbvios de uso de sequências. Vamos mostrá-las com strings, mas não se esqueça que listas também podem usar os mesmos truques.
#Vamos começar com uma função chamada min().
#A função encontra o elemento mínimo da sequência usado como argumento. Existe uma condição: a sequência (string, lista, não importa) não pode estar vazia, senão será retornada uma exceção ValueError .

print("Função min()")
# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))


# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

#O programa do Exemplo 1 retorna: A
#Observação: É um A maiúsculo. O motivo? Lembre-se da tabela ASCII, quais letras ocupam as primeiras colocações, maiúsculas ou minúsculas?
#Preparamos mais dois exemplos a serem analisados: Exemplos 2 e 3.
#Como podemos ver, eles trazem mais do que strings. O resultado esperado é o seguinte: [ ] e 0
#Observação: usamos colchetes para impedir que o espaço seja ignorado em sua tela.

#max()
#De maneira semelhantes, uma função chamada max() encontra o elemento máximo da sequência.

print("Função max()")

# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))


# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

#O método index() (é um método, não uma função) vasculha a sequência desde seu início em busca do primeiro elemento do valor especificado em seu argumento.
#Observação: o elemento buscado deve ocorrer na sequência, sua ausência causará uma exceção ValueError .
#O método retorna o índice da primeira ocorrência do argumento (que significa que o menor resultado possível é 0, enquanto o maior é o comprimento do argumento reduzido em 1).

print("Demonstrando o método index():")
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

#A função list()
#A função list() usa o seu argumento (uma string) e cria uma nova lista contendo todos os caracteres de uma string, um por elemento.
#Observação: não é estritamente uma função de string, list() é capaz de criar uma nova lista a partir de diversas outras entidades (por ex., a partir de tuplas e dicionários).

print("Demonstrando a função list():")
print(list("abcabc"))

#O método count()
#O método count() conta todas as ocorrências do elemento dentro da sequência. A ausência desses elementos não causa nenhum problema.

print("Demonstrando o método count():")
print("abcabc".count("b"))
print('abcabc'.count("d"))


### RESUMO DA SEÇÃO ###
#1. Strings Python são sequências imutáveis e podem ser indexadas, fatiadas (sliced) e iteradas como qualquer outra sequência, além de estarem sujeitas aos operadores in e not in . Existem dois tipos de strings em Python:

#strings de uma linha, que não podem ultrapassar os limites entre linhas; as declaramos usando apóstrofes ('string') ou aspas ("string")
#strings multilinhas que ocupam mais de uma linha de código fonte, delimitadas por trígrafos:
#'''
#string
#'''

#ou

#"""
#string
#"""

#2. O comprimento de uma string é determinado pela função len() . O caractere de escape (\) não é considerado. Por exemplo:


#print(len("\n\n"))
 
#apresenta o resultado 2.

#3. Strings podem ser concatenadas usando o operador + e replicadas usando o operador * . Por exemplo:


#asterisk = '*'
#plus = "+"
#decoration = (asterisk + plus) * 4 + asterisk
#print(decoration)
 
#apresenta o resultado *+*+*+*+*.

#4. O par de funções chr() e ord() podem ser usadas para criar um caractere usando seu ponto de código e para determinar um ponto de código que corresponda a um caractere. Ambas as expressões a seguir serão sempre verdadeiras:


#chr(ord(character)) == character
#ord(chr(codepoint)) == codepoint
 

#5. Algumas outras funções que podem ser aplicadas a strings são:

#list() : cria uma lista composta por todos os caracteres da string;
#max() : encontra o caractere com o ponto de código mais alto;
#min() : encontra o caractere com o menor ponto de código.

#6. O método chamado index() encontra o índice de uma determinada substring dentro da string.
