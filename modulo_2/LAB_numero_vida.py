#Alguns dizem que o Número de Vida é um número avaliado usando a data de nascimento de alguém. É simples, basta somar todos os números da data. Se o resultado contiver mais de um número, será necessário repetir a soma até obter apenas um número. Por exemplo:

#1 de janeiro de 2017 = 2017 01 01
#2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
#1 + 2 = 3
#3 é o número que estávamos procurando.

#Sua tarefa é criar um programa que:

#solicite a data de aniversário do usuário (no formato AAAAMMDD, AAAADDMM ou MMDDAAAA; na realidade, a ordem dos dígitos não importa)
#mostre o Número de Vida resultante.

date = input("Digite sua data de nascimento (no formato AAAAMMDD ou AAAAYDDMM, 8 dígitos): ")
if len(date) != 8 or not date.isdigit():
    print("Invalid date format.")
#Garante que:
#A entrada tenha exatamente 8 caracteres.
#Todos os caracteres sejam dígitos.    
else:
    while len(date) > 1:
        the_sum = 0
        for dig in date:
            the_sum += int(dig)
        print(date)
        date = str(the_sum)
    print("Seu número de vida é: " + date)

#Esse é o núcleo do cálculo:

#Enquanto date tiver mais de um dígito:
#Soma todos os seus dígitos (the_sum).
#Mostra o valor atual da date antes de reduzir.
#Atualiza date com a soma, convertida de volta para string.	
