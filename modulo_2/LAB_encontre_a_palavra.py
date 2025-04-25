
#Vamos participar de um jogo. Daremos duas strings: uma com uma palavra (por ex., "gafe") e a segunda, uma combinação de quaisquer caracteres.
#Sua tarefa é criar um programa que responda à seguinte pergunta: os caracteres da primeira palavra estão presentes na segunda string?

#Dicas:

#recomendamos usar variações das funções pos() com dois argumentos em seu código;
#não se preocupe com maiúsculas ou minúsculas.

word = input("Digite a palavra que deseja encontrar: ").upper()
strn = input("Digite a string onde realizar a busca: ").upper()

found = True
start = 0

for ch in word:
	pos = strn.find(ch, start) 
	if pos < 0:
		found = False
		break
	start = pos + 1
if found:
	print("Sim")
else:
	print("Não")
	   
#1. Entrada e padronização

#word = input("Digite a palavra que deseja encontrar: ").upper()
#strn = input("Digite a string onde realizar a busca: ").upper()

#O usuário digita:
#A palavra que quer encontrar (word)
#A string onde será feita a busca (strn)
#Ambas são convertidas para maiúsculas com .upper(), para tornar a comparação case-insensitive (ignorar maiúsculas/minúsculas).

#2. Inicialização

#found = True
#start = 0

#found começa como True e será alterado se algum caractere não for encontrado na ordem correta.
#start indica onde começar a busca na string (strn). Ele vai sendo atualizado para manter a ordem.

#3. Loop sobre os caracteres da palavra

#for ch in word:
#	pos = strn.find(ch, start)

#Para cada caractere ch da word, o código procura esse caractere dentro de strn, começando da posição start.
#strn.find(ch, start) retorna o índice do caractere encontrado ou -1 se não for encontrado.

#4. Verificação do resultado da busca

#	if pos < 0:
#		found = False
#		break
#	start = pos + 1

#Se o caractere não for encontrado, found é marcado como False e o loop é interrompido (break).
#Se for encontrado, start é atualizado para a próxima posição, garantindo que a ordem dos caracteres seja mantida.

#5. Resultado final

#if found:
#	print("Sim")
#else:
#	print("Não")

#Se todos os caracteres da word foram encontrados na ordem, imprime Sim.
#Caso contrário, imprime Não.
