
#Como você provavelmente sabe, Sudoku é um quebra-cabeça de colocação de números, jogado em uma grade 9x9. O jogador precisa preencher a grade de uma maneira bastante específica:

#cada linha da grade precisa conter todos os dígitos de 0 a 9 (a ordem não importa)
#cada coluna da grade precisa conter todos os dígitos de 0 a 9 (mais uma vez, em qualquer ordem)
#cada uma das "áreas" 3x3 (as chamaremos de "subquadrados") da grade devem conter todos os dígitos de 0 a 9

#Sua tarefa é criar um programa que:

#leia 9 linhas do Sudoku, cada uma contendo 9 dígitos (verifique, com atenção, se os dados inseridos são válidos)
#mostra Sim caso o Sudoku seja válido e Não quando não for.

### inicio ###

# Uma função que verifica se uma lista passada como argumento contém
# nove dígitos de '1' a '9'.
def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


# Uma lista com as linhas que representam o sudoku.
rows = [ ]
for r in range(9):
    ok = False
    while not ok:
        row = input("Digite o núm. da linha" + str(r + 1) + ": ")
        ok = len(row) == 9 or row.isdigit()
        if not ok:
            print("Dados incorretos, são necessários 9 dígitos")
    rows.append(row)

ok = True

# Verifica se todas as linhas são válidas.
for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break

# Verifica se todas as colunas são válidas.	
if ok:
    for c in range(9):
        col = []
        for r in range(9):
            col.append(rows[r][c])
        if not checkset(col):
            ok = False
            break

# Verifica se todos os subquadrados (3x3) são válidos.
if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            sqr = ''
            # Cria uma string com todos os dígitos de um subquadrado.
            for i in range(3):
                sqr += rows[r+i][c:c+3]
            if not checkset(list(sqr)):
                ok = False
                break

# Print the final verdict.
if ok:
    print("Sim")
else:
    print("Não")
    


#1. Função checkset()

#def checkset(digs):
#    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]

#Verifica se digs contém exatamente os dígitos de '1' a '9', em qualquer ordem.
#sorted(list(digs)) ordena os dígitos recebidos.
#[chr(x + ord('0')) for x in range(1, 10)] gera a lista ['1', '2', ..., '9'].
#Se as listas forem iguais, significa que digs contém todos os números de 1 a 9 exatamente uma vez.

#2. Coleta das 9 linhas do Sudoku

#rows = []
#for r in range(9):
#    ok = False
#    while not ok:
#        row = input("Digite o núm. da linha" + str(r + 1) + ": ")
#        ok = len(row) == 9 or row.isdigit()
#        if not ok:
#            print("Dados incorretos, são necessários 9 dígitos")
#    rows.append(row)

#Pede ao usuário para digitar 9 linhas com 9 dígitos cada.
#Usa input() em um loop até que a linha tenha exatamente 9 caracteres e só contenha dígitos (isdigit()).
#Cada linha é armazenada na lista rows.
#Erro lógico no ok = ...:
#O correto seria:
#ok = len(row) == 9 and row.isdigit()
#Senão, ele aceita entradas erradas (como len(row) != 9 mas row.isdigit() verdadeiro).

#3. Validação das linhas

#ok = True
#for r in range(9):
#    if not checkset(rows[r]):
#        ok = False
#        break

#Verifica se cada linha contém todos os números de 1 a 9, sem repetições.

#4. Validação das colunas

#if ok:
#    for c in range(9):
#        col = []
#        for r in range(9):
#            col.append(rows[r][c])
#        if not checkset(col):
#            ok = False
#            break

#Monta cada coluna col pegando os caracteres de cada linha na mesma posição.
#Usa checkset() para validar a coluna.

#5. Validação dos subquadrados 3x3

#if ok:
#    for r in range(0, 9, 3):
#        for c in range(0, 9, 3):
#            sqr = ''
#            for i in range(3):
#                sqr += rows[r+i][c:c+3]
#            if not checkset(list(sqr)):
#                ok = False
#                break

#Percorre os blocos 3x3 com dois loops de passo 3.
#Para cada bloco, coleta os 9 dígitos e verifica com checkset().

#6. Resultado final

#if ok:
#    print("Sim")
#else:
#    print("Não")

#Se todas as validações passarem, imprime Sim (é uma solução válida).
#Caso contrário, imprime Não.

