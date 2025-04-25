# Cifra de César.


#Esta cifra foi (provavelmente) criada e usada por Caio Júlio César e suas tropas durante as Guerras Gálicas. A ideia era bastante simples: cada letra da mensagem é substituída pela letra que se apresenta abaixo dela no alfabeto (A torna-se B, B torna-se C e assim or diante). A única exceção é Z, que se torna A.

#ele aceita apenas letras do alfabeto latino (observação: os romanos não usavam espaços ou dígitos)
#todas as letras da mensagem estão em maiúsculas (observação: os romanos só conheciam maiúsculas)

text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)


#Vamos analisar o código:

#linha 02: pedir ao usuário para inserir a mensagem aberta (não criptografada) de uma linha;
#linha 03: preparar uma string para uma mensagem criptografada (vazia por enquanto)
#linha 04: começar a interação pela mensagem;
#linha 05: se o caractere atual não for alfabético...
#linha 06: ...ignore-o;
#linha 07: converter a letra para maiúscula (é melhor fazê-lo independente de confirmar se é necessário ou não)
#linha 08: obter o código da letra e incrementá-lo em um;
#linha 09: se o código resultante tiver "deixado" o alfabeto latino (caso seja maior que o código Z )...
#linha 10: ... mudar para o código A;
#linha 11: anexar o caractere recebido ao fim da mensagem criptografado;
#linha 13: imprimir a cifra.    
