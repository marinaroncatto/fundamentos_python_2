# Processador de números.

#O terceiro programa mostra um método simples que permite inserir uma linha preenchida com números e processá-los de maneira simples. Observação: a função input() combinada com as funções int() ou float() não é adequada para este fim.
#O processamento será extremamente simples, queremos que os números sejam somados.

# Processador de números.

line = input("Enter a line of numbers - separate them with spaces: ").strip()

# Verifica se a linha está vazia
if not line:
    print("Nenhum número foi inserido.")
else:
    strings = line.split()
    total = 0
    try:
        for substr in strings:
            total += float(substr)
        print("The total is:", total)
    except ValueError:
        print(substr, "is not a number.")
    
#linha 03: pedir ao usuário para digitar uma linha com qualquer quantidade de números (os números podem ser floats)
#linha 04: dividir a linha que recebe uma lista de substrings;
#linha 05: iniciar a soma total para zero;
#linha 06: uma vez que a conversão de string para float pode gerar uma exceção, é melhor continuar usando o bloco try-except;
#linha 07: faça a iteração pela lista...
#line 08: ... e tente converter todos os seus elementos em números float; se funcionar, aumente a soma;
#line 09: tudo bem até aqui, então imprimir a soma;
#linha 10: o programa encerra aqui caso ocorra um erro;
#linha 11: imprimir uma mensagem de diagnóstico mostrando o motivo da falha para o usuário.

#O que foi corrigido:
#line.strip() remove espaços extras no início/fim, evitando que uma linha " " (com espaços) seja aceita.
#if not line: detecta se o input está vazio após o strip().
#O except agora captura ValueError, que é o erro apropriado ao converter string para float.
