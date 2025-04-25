#Sua tarefa é criar um programa que:

#solicite que o usuário insira um texto;
#verifica se o texto digitado é um palíndromo e mostra o resultado.
#Observação:

#supõe-se que uma string vazia não é um palíndromo;
#trata-se maiúsculas e minúsculas igualmente;
#espaços não são levados em conta durante a verificação e são tratados como não existentes;
#existe mais de uma solução correta, tente encontrar várias.

text = input("Digite o texto: ")

# Remove todos os espaços...
text = text.replace(' ','')

# ... e verifica se a palavra é igual à sua versão inversa
if len(text) > 1 and text.upper() == text[::-1].upper():
	print("É palíndromo")
else:
	print("Não é palíndromo")

#explicação:
#len(text) > 1: garante que o texto tenha mais de um caractere (evita que ele diga que uma letra sozinha é um palíndromo).

#text.upper(): converte o texto para maiúsculas, para ignorar diferença entre maiúsculas/minúsculas.

#text[::-1]: inverte a string.

#==: compara o texto com sua versão invertida.


	
