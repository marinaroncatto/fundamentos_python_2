#A cifra de César original troca os caracteres um a um: a se torna b, z se torna a e assim por diante. Vamos torná-lo um pouco mais complexo e permitir o valor alterado esteja no intervalo 1..25, inclusive.

#Além disso, iremos permitir que o código preservar a caixa das letras (minúsculas permanecerão dessa maneira, por exemplo) e todos os caracteres não alfabéticos devem ser mantidos, sem alterações.

#Sua tarefa é criar um programa que:

#peça ao usuário uma linha de texto para criptografar;
#solicita ao usuário um intervalo de troca (um número inteiro de 1..25 - observação: você deve forçar o usuário a digitar um valor de troca válido (não desista e não deixe dados ruins o enganem!)
#mostra o texto codificado.




# Insira o texto que deseja criptografar.
text = input("Enter message: ")

# Insira um valor válido de shift (repetir até o êxito).
shift = 0

while shift == 0:
    try:    
        shift = int(input("Enter the cipher shift value (1..25): "))
        if shift not in range(1,26):
        	raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Incorrect shift value!")

cipher = ''

for char in text:
    # É uma letra?
    if char.isalpha():
        # Shift its code.
        code = ord(char) + shift
        # Localizar o código da primeira letra (maiúscula ou minúscula)
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        # Fazer correção.
        code -= first
        code %= 26
        # Anexar o caractere codificado na mensagem.
        cipher += chr(first + code)
    else:
        # Anexar o caractere original na mensagem.
        cipher += char

print(cipher)


#1. Entrada da mensagem
#text = input("Enter message: ")
#Aqui o programa pede ao usuário que insira uma mensagem para ser criptografada.

#2. Entrada do valor de deslocamento (shift)

#shift = 0

#while shift == 0:
#    try:    
#        shift = int(input("Enter the cipher shift value (1..25): "))
#        if shift not in range(1,26):
#        	raise ValueError
#    except ValueError:
#        shift = 0
#    if shift == 0:
#        print("Incorrect shift value!")

#Esse trecho garante que o usuário só possa digitar um número entre 1 e 25.

#Se ele digitar algo fora desse intervalo (ou um valor não numérico), o programa repete a pergunta até receber uma entrada válida.

#3. Inicialização da variável de saída

#cipher = ''

#Vai guardar o texto criptografado.

#4. Loop para criptografar cada caractere

#for char in text:
#Vai verificar cada caractere da mensagem digitada.

#5. Verificação se é uma letra

#if char.isalpha():

#Se for uma letra (maiúscula ou minúscula), ela será criptografada.
#Se for número, espaço, pontuação etc., ela é mantida como está.

#6. Cálculo do novo caractere

#        code = ord(char) + shift
#ord(char) transforma a letra em número (código ASCII).

#Adiciona o valor do shift.


#        if char.isupper():
#           first = ord('A')
#        else:
#            first = ord('a')
#Determina se deve começar do código da letra A (maiúscula) ou a (minúscula).


#        code -= first
#        code %= 26
#        cipher += chr(first + code)
#Isso garante que, ao ultrapassar o "Z" ou "z", ele volte ao começo do alfabeto (efeito circular).

#chr() transforma de volta o número em letra e adiciona à string cipher.

#7. Se não for letra

#    else:
#        cipher += char
#Mantém o caractere original (espaços, números, pontuação etc.).

#8. Exibe o texto criptografado

#print(cipher)    
