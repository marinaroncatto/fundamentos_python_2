#anagrama é uma nova palavra formada ao reordenar as letras de uma palavra, usando todas as letras originais exatamente uma vez. Por exemplo, as palavras "terno" e "norte" são anagramas, enquanto "Eu sou" e "você é", não.

#Sua tarefa é criar um programa que:

#peça ao usuário dois textos diferentes;
#verifica se os textos digitados são anagramas e mostra o resultado.
#Observação:

#supõe-se que duas strings vazias não são anagramas;
#trata-se maiúsculas e minúsculas igualmente;
#espaços não são levados em conta durante a verificação e são tratados como não existentes

str_1 = input("Digite a primeira string: ")
str_2 = input("Digite a segunda string: ")

strx_1 = ''.join(sorted(list(str_1.upper().replace(' ',''))))
strx_2 = ''.join(sorted(list(str_2.upper().replace(' ',''))))

#Para cada string:
#1 - str_1.upper() – transforma tudo em maiúsculas, para ignorar diferenças entre letras maiúsculas e minúsculas.

#2 - .replace(' ', '') – remove todos os espaços.

#3 - list(...) – transforma a string em uma lista de letras.

#4 - sorted(...) – ordena as letras em ordem alfabética.

#5 - ''.join(...) – junta as letras novamente em uma única string.

if len(strx_1) > 0 and strx_1 == strx_2:
	print("Anagramas")
else:
	print("Não são anagramas")

#6 - len(strx_1) > 0: garante que a entrada não esteja vazia.
#7 - strx_1 == strx_2: compara as strings ordenadas. Se forem idênticas, são anagramas.
	
	
