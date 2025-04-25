# Validador IBAN.

#Um número de conta em conformidade com IBAN é composto por:

#código de país com duas letras, retirado do padrão ISO 3166-1 (por ex., FR para França, GB para Grã-Bretanha, DE para Alemanha e assim por diante)
#dois dígitos usados para realizar as confirmações de validade, simples e rápido, mas não é totalmente confiável: executa um teste, indicando se um número é inválido (distorcido por erro de digitação) ou se está correto;
#O número da conta em si (até 30 caracteres alfanuméricos, o comprimento depende do padrão do país)
#O padrão diz que a validação requer as seguintes etapas (de acordo com a Wikipedia):

#(etapa 1) Verifica se o comprimento total do IBAN está correto de acordo com o país (este programa não fará isso, mas você pode modificar o código para atender esse requisito, se desejar; no entanto, observe que você precisará ensinar ao código todos os comprimentos usados na Europa)
#(etapa 2) Move os quatro caracteres iniciais para o fim da string (ou seja, o código do país e os dígitos de verificação)
#(etapa 3) Substitui cada letra na string com dois dígitos, expandindo a string, em que A = 10, B = 11 ... Z = 35;
#(etapa 4) Interpreta a string como número inteiro decimal e calcula o resto desse número com operação módulo, dividindo por 97; Se o resto for 1, ele passou o teste do dígito de verificação e talvez o IBAN seja válido.

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")
    
#linha 03: pedir ao usuário para digitar o IBAN (o número pode conter espaços, pois aumentar a legibilidade do número consideravelmente...
#linha 04: ...mas os remove imediatamente)
#linha 06: o IBAN digitado deve ser composto apenas por dígitos e letras, caso não seja...
#line 07: ...mostrar a mensagem;
#linha 08: o IBAN não pode ser menor que 15 caracteres (esta é a menor variação, usada na Noruega)
#linha 09: caso seja menor, o usuário será avisado;
#linha 10: além disso, o IBAN não pode ser maior que 31 caracteres (esta é a maior variação, usada em Malta)
#linha 11: caso seja maior, exibir um aviso;
#linha 12: iniciar o processamento de fato;
#linha 13: move os quatro caracteres iniciais para o fim do número e converte todas as letras para maiúsculas (etapa 02 do algoritmo)
#linha 14: esta é a variável usada para completar o número, criada ao substituir as letras com dígitos (de acordo com a etapa 03 do algoritmo)
#linha 15: repetir no IBAN;
#linha 16: se o caractere for um dígito...
#linha 17: apenas o copia;
#linha 18: caso contrário...
#line 19: ...convertê-lo em dois dígitos (observe a maneira como é feito aqui)
#linha 20: a forma convertida do IBAN está pronta, criar um inteiro a partir dela;
#linha 21: o resto da divisão de iban2 por 97 é igual a 1?
#linha 22: Caso seja, temos uma situação de êxito;
#linha 23: caso contrário...
#linha 24: ... o número é inválido.
#Vamos incluir dados de teste (todos esses números são válidos, basta alterar qualquer caractere para invalidá-los).

#Inglês: GB72 HBZU 7006 7212 1253 00
#Francês: FR76 30003 03620 00020216907 50
#Alemão: DE02100100100152517108
